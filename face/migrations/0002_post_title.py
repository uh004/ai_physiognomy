# Generated by Django 5.0.6 on 2024-06-04 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]