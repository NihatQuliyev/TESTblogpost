# Generated by Django 4.0.2 on 2023-01-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]