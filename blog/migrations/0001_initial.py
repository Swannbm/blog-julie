# Generated by Django 4.0.2 on 2022-02-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='Slug')),
                ('title', models.CharField(max_length=250, verbose_name='Titre')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('tags', models.CharField(max_length=250, verbose_name='Mots clés')),
            ],
        ),
    ]
