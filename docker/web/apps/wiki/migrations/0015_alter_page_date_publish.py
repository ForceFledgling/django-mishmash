# Generated by Django 4.0.2 on 2022-03-15 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_alter_page_date_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='date_publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 15, 10, 34, 4, 696808), null=True, verbose_name='Дата публикации'),
        ),
    ]
