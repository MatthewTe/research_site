# Generated by Django 3.1.4 on 2022-01-02 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_core', '0003_auto_20220101_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='lastname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='middlename',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
