# Generated by Django 4.0.2 on 2022-02-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_photo_blogpost_main_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Mots clés'),
        ),
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(max_length=250, null=True, verbose_name='Mots clés'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='height',
            field=models.IntegerField(null=True, verbose_name='Hauteur'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='width',
            field=models.IntegerField(null=True, verbose_name='Largeur'),
        ),
    ]