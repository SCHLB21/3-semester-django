# Generated by Django 3.1.5 on 2021-01-12 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210112_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employees',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
    ]
