# Generated by Django 3.1 on 2020-11-12 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0002_auto_20201111_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.JSONField(default={'name': 'Kieran', 'net worth': 10, 'occupation': 'Researcher'})),
            ],
        ),
    ]