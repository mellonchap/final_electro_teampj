# Generated by Django 3.2 on 2022-04-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_auto_20220321_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-mdate',), 'verbose_name_plural': '아티클 작성하기'},
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
