# Generated by Django 5.0.6 on 2024-07-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadp_contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
