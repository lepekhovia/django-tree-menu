from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


class MenuItem(models.Model):

    objects = models.Manager()

    title = models.CharField(max_length=100, verbose_name=_('Title'))
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('URL'))
    named_url = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Named URL'))
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE, verbose_name=_('Parent'))
    menu_name = models.CharField(max_length=50, verbose_name=_('Menu name'))

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return f'/{self.url.strip("/")}/'
        return f'/{self.url.strip("/")}/' if self.url else '/'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Menu Item')
        verbose_name_plural = _('Menu Items')
