# Generated by Django 3.1.7 on 2022-12-01 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20221201_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simfiles',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 17, 0, 51, 475077), verbose_name='上传时间'),
        ),
    ]
