# Generated by Django 4.1.2 on 2023-07-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callsuploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='callinfo',
            old_name='record_url',
            new_name='file',
        ),
        migrations.AddField(
            model_name='callinfo',
            name='messages',
            field=models.TextField(blank=True, null=True),
        ),
    ]
