# Generated by Django 5.1.1 on 2024-10-09 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name': 'Menu Item', 'verbose_name_plural': 'Menu Items'},
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='sort_order',
        ),
    ]
