# Generated by Django 5.0.6 on 2024-07-16 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadp_polls', '0002_answer_options_poll_participants_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizen',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='citizen',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]