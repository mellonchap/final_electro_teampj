# Generated by Django 3.2 on 2022-03-17 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Article 작성 목록'},
        ),
    ]