# Generated by Django 4.2.1 on 2023-06-10 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(blank=True, db_index=True, default='Anonymous', max_length=14, null=True, verbose_name='Name'),
        ),
    ]
