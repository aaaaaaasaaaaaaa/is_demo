# Generated by Django 3.0.7 on 2021-03-11 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_bot', '0003_hrcheckpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='hruser',
            name='checkpoint',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
