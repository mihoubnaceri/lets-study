# Generated by Django 2.0.2 on 2018-02-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180225_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
