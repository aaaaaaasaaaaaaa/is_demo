# Generated by Django 3.1.5 on 2022-12-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrix24', '0003_alter_bitrixuser_extranet_alter_bitrixuser_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitrixuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bitrixusertoken',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
