# Generated by Django 5.0.6 on 2024-07-04 07:43

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('views_count', models.IntegerField(default=0, editable=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('views_count', models.IntegerField(default=0, editable=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', tinymce.models.HTMLField()),
                ('category', models.CharField(choices=[('center', 'Center News'), ('uzbekistan', 'Uzbekistan News'), ('international', 'International News')], default='center', max_length=20)),
                ('links', models.URLField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('views_count', models.IntegerField(default=0, editable=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
