# Generated by Django 4.2.3 on 2023-08-03 17:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import intagration_utils_candidate.app_telegram_bot.models.abstract_message


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenAiBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('auth_token', models.CharField(default='', max_length=100)),
                ('last_update_id', models.IntegerField(blank=True, default=0)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenAiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=100)),
                ('username', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=127, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=127, null=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenAiUserChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=100)),
                ('telegram_type', models.CharField(blank=True, choices=[('private', 'private'), ('group', 'group'), ('supergroup', 'supergroup')], default='', max_length=25, null=True)),
                ('secret', models.CharField(blank=True, default='', max_length=50)),
                ('bot', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tg_openai_bot.openaibot')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenAiUserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField()),
                ('text', models.TextField(default='', null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('voice', models.FileField(blank=True, null=True, upload_to=intagration_utils_candidate.app_telegram_bot.models.abstract_message.voice_upload_path)),
                ('caption', models.TextField(default='', null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tg_openai_bot.openaiuser')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='tg_openai_bot.openaiuserchat')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OpenAiChatParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='tg_openai_bot.openaiuserchat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participated_chats', to='tg_openai_bot.openaiuser')),
            ],
            options={
                'verbose_name': 'Участник чата',
                'verbose_name_plural': 'Участники чатов',
                'abstract': False,
                'unique_together': {('chat', 'user')},
            },
        ),
    ]
