# Generated by Django 5.0.1 on 2024-01-29 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_alter_category_options_alter_media_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='Media',
            new_name='media',
        ),
        migrations.RemoveField(
            model_name='media',
            name='date_added',
        ),
    ]
