from django.db import models


class BlogPost(models.Model):
    slug = models.SlugField("Slug", unique=True, primary_key=True)
    title = models.CharField("Titre", max_length="250")
    content = models.TextField("Contenu")
    tags = models.CharField("Mots clés", max_length="250")
