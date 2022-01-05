# Generated by Django 3.1.4 on 2022-01-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_core', '0008_auto_20220103_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='research_core/thumbnails'),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_img',
            field=models.ImageField(blank=True, null=True, upload_to='research_core/topics/'),
        ),
    ]
