# Generated by Django 5.0.7 on 2024-07-24 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
    ]