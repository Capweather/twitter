# Generated by Django 4.2.1 on 2023-06-09 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='like'),
        ),
    ]
