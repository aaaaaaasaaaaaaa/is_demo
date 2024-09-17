# Generated by Django 2.2.13 on 2020-11-01 14:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import its_utils.app_telegram_bot.models.abstract_message


class Migration(migrations.Migration):

    dependencies = [
        ('example_bot', '0003_examplechatparticipant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField()),
                ('text', models.TextField(default='', null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('voice', models.FileField(blank=True, null=True, upload_to=its_utils.app_telegram_bot.models.abstract_message.voice_upload_path)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='example_bot.ExampleUser')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='example_bot.ExampleChat')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'abstract': False,
            },
        ),
    ]
