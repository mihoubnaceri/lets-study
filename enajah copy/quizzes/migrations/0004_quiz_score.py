# Generated by Django 2.0.2 on 2018-02-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_auto_20180224_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]