# Generated by Django 3.2 on 2022-03-17 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrydata',
            options={'verbose_name_plural': '각 나라별 인구 데이터'},
        ),
    ]
