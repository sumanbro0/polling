# Generated by Django 5.0.6 on 2024-05-24 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_vote_choice_remove_vote_question_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AlterField(
            model_name='submission',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]