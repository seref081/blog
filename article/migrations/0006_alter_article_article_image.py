# Generated by Django 5.0.7 on 2024-07-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_article_image_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin'),
        ),
    ]
