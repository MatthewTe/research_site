# Generated by Django 3.1.4 on 2022-01-02 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_core', '0006_auto_20220102_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='takeaway',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='source',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]