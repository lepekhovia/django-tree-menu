from django import template
from ..models import MenuItem
from django.utils.safestring import mark_safe
register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, item)
                tree.append((item, children))
        return tree

    menu_tree = build_menu_tree(menu_items)

    def render_menu(menu_tree, level=0):
        html = '<ul>' if level == 0 else '<ul style="display:none;">'
        for item, children in menu_tree:
            active_class = 'active' if item.get_absolute_url() == current_url else ''
            html += f'<li class="{active_class}"><a href="{item.get_absolute_url()}">{item.title}</a>'
            if children:
                html += render_menu(children, level + 1)
            html += '</li>'
        html += '</ul>'
        return html

    return mark_safe(render_menu(menu_tree))
