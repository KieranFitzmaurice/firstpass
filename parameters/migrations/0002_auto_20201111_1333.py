# Generated by Django 2.2.5 on 2020-11-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='Date_published',
            field=models.DateField(help_text='yyyy-mm-dd', verbose_name='Date published'),
        ),
    ]
