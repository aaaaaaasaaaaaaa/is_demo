# Generated by Django 4.1.2 on 2023-07-17 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bitrix24', '0005_alter_bitrixuser_id_alter_bitrixusertoken_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRobot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_token', models.CharField(blank=True, max_length=255, null=True)),
                ('params', models.JSONField()),
                ('dt_add', models.DateTimeField(auto_now=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('is_success', models.BooleanField(default=False)),
                ('result', models.JSONField(blank=True, null=True)),
                ('is_hook_request', models.BooleanField(default=False)),
                ('send_result_response', models.TextField(blank=True, null=True)),
                ('token', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bitrix24.bitrixusertoken')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
