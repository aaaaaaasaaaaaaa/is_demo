# Generated by Django 3.0.7 on 2020-06-29 16:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitrixUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitrix_id', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=255)),
                ('last_name', models.CharField(blank=True, default='', max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('work_phone', models.CharField(blank=True, default='', max_length=100)),
                ('personal_mobile', models.CharField(blank=True, default='', max_length=100)),
                ('extranet', models.NullBooleanField(default=None)),
                ('is_admin', models.BooleanField(blank=True, default=False)),
                ('user_created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('user_is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BitrixUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=70)),
                ('refresh_token', models.CharField(blank=True, default='', max_length=70)),
                ('auth_token_date', models.DateTimeField()),
                ('app_sid', models.CharField(blank=True, max_length=70)),
                ('is_active', models.BooleanField(default=True)),
                ('refresh_error', models.PositiveSmallIntegerField(choices=[(0, 'Нет ошибки'), (1, 'Не установлен портал (Wrong client)'), (2, 'Устарел ключ совсем (Expired token)'), (3, 'Инвалид грант (Invalid grant)'), (4, 'Не установлен портал (NOT_INSTALLED)'), (5, 'Не оплачено (PAYMENT_REQUIRED)'), (6, 'Домен отключен или не существует'), (8, 'ошибка >= 500 '), (9, 'Надо разобраться (Unknown Error)'), (10, 'PORTAL_DELETED'), (11, 'ERROR_CORE'), (12, 'ERROR_OAUTH'), (13, 'ERROR_403_or_404'), (14, 'NO_AUTH_FOUND'), (15, 'AUTHORIZATION_ERROR'), (16, 'ACCESS_DENIED'), (17, 'APPLICATION_NOT_FOUND')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bitrix_user_token', to='bitrix24.BitrixUser')),
            ],
        ),
    ]
