# Generated by Django 2.2.5 on 2020-11-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parameters', '0006_auto_20201104_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='status',
            field=models.CharField(choices=[('Current', 'Current'), ('Outdated', 'Outdated')], default='Current', max_length=225, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='type',
            field=models.CharField(choices=[('Probability', 'Probability'), ('Rate', 'Rate'), ('Cost', 'Cost'), ('Numeric value', 'Numeric value'), ('Integer value', 'Integer value'), ('Boolean value', 'Boolean value - TRUE, FALSE, or NA'), ('Numeric list', 'Numeric list - separate values with commas'), ('Integer list', 'Integer list - separate values with commas'), ('Boolean list', 'Boolean list - separate values with commas')], max_length=255, verbose_name='Type'),
        ),
    ]
