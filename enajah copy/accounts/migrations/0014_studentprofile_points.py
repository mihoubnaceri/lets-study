# Generated by Django 2.0.2 on 2018-02-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180225_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]