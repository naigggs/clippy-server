# Generated by Django 4.2.10 on 2024-03-03 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0003_rename_youtubelink_transcipt'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Transcipt',
            new_name='Transcript',
        ),
    ]
