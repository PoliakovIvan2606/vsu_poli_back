# Generated by Django 5.0.2 on 2024-04-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_links_news_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='links',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]