# Generated by Django 3.1.4 on 2022-01-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_core', '0012_auto_20220105_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='thumbnail',
            field=models.ImageField(default=None, null=True, upload_to='research_core/thumbnails'),
        ),
    ]
