# Generated by Django 4.0 on 2021-12-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_newpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='category',
            field=models.CharField(choices=[('View-All', 'View-All'), ('Social', 'Social'), ('Current-Affairs', 'Current-Affairs'), ('Newspaper-cuts', 'Newspaper-cuts'), ('Travel', 'Travel'), ('Others', 'Others')], default=None, max_length=40),
        ),
    ]
