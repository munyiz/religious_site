# Generated by Django 5.0.1 on 2025-02-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_question_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='BibleVerse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=50)),
                ('chapter', models.IntegerField()),
                ('verse', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
    ]
