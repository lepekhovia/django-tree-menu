from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.urls.exceptions import NoReverseMatch


class Menu(models.Model):

    objects = models.Manager()

    name = models.CharField(max_length=255, unique=True, verbose_name=_('Menu Name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')


class MenuItem(models.Model):
    DOMEN = 'http://127.0.0.1:8000'

    objects = models.Manager()

    title = models.CharField(max_length=255, verbose_name=_('Menu Item Title'))
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE, verbose_name=_('Menu'))
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE, verbose_name=_('parent'))
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('URL'))
    named_url = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Named URL'))

    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')

    def get_absolute_url(self):
        try:
            return reverse(self.named_url)
        except NoReverseMatch:
            return self.DOMEN + '/' + self.menu.name + '/' + str(self.url)

    def __str__(self):
        return self.title
