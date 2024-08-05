# Generated by Django 5.0.7 on 2024-07-20 19:51

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_image_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Makaleye Fotoğraf Ekleyin'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='İçerik'),
        ),
    ]
