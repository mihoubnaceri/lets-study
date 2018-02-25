# Generated by Django 2.0.2 on 2018-02-24 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20180223_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='result',
            new_name='pourcentage',
        ),
        migrations.AddField(
            model_name='quiz',
            name='number_of_questions',
            field=models.IntegerField(default=1),
        ),
    ]
