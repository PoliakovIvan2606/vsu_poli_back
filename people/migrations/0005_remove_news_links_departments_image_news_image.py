# Generated by Django 5.0.2 on 2024-04-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_news_links_delete_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='links',
        ),
        migrations.AddField(
            model_name='departments',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]