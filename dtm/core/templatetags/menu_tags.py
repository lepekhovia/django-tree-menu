from django import template
from core.models import MenuItem
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name, active=None):
    menu_items = MenuItem.objects.prefetch_related('children').filter(menu__name=menu_name)

    if menu_items.count() == 0:
        return _('There is no menu with this name.')

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, item)
                tree.append((item, children))
        return tree

    def find_active_path(active_url):
        path = []
        try:
            active_item = MenuItem.objects.get(url=active_url, menu__name=menu_name)
            path.append(active_item)
            parent = active_item.parent
            while parent:
                path.append(parent)
                parent = parent.parent
        except MenuItem.DoesNotExist:
            print(f"Active element with URL {active_url} not found.")
        return path

    menu_tree = build_menu_tree(menu_items)
    active_path = find_active_path(active)

    def render_menu(menu_tree, level=0):
        html = '<ul>' if level == 0 else '<ul>'
        for item, children in menu_tree:
            active_class = 'active' if item in active_path else ''
            html += f'<li class="{active_class}"><a href="{item.get_absolute_url()}">{item.title}</a>'
            if children:
                html += render_menu(children, level + 1)
            html += '</li>'
        html += '</ul>'
        return html

    return mark_safe(render_menu(menu_tree))
