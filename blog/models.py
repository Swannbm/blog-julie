from markdown import markdown
from random import randrange
import re

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.utils.text import slugify


class Photo(models.Model):
    title = models.CharField("Titre", max_length=250, blank=True, null=True)
    tags = models.CharField("Mots clés", max_length=250, blank=True, null=True)
    photo_file = models.ImageField(
        "Fichier photo", height_field="height", width_field="width"
    )
    height = models.IntegerField("Hauteur", null=True)
    width = models.IntegerField("Largeur", null=True)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f"Photo n° {self.id}"

    def image_url(self):
        if self.photo_file:
            return self.photo_file.url
        else:
            return ""
    image_url.short_description = "Url de l'image"
    image_url.allow_tags = True

    def image_tag(self):
        if self.photo_file:
            return mark_safe(f'<img src="{self.photo_file.url}" />')
        else:
            return "-"
    image_tag.short_description = "Aperçu de l'image"
    image_tag.allow_tags = True


class BlogPost(models.Model):
    slug = models.SlugField("Slug", unique=True, primary_key=True)
    title = models.CharField("Titre", max_length=250)
    content = models.TextField("Contenu")
    tags = models.CharField("Mots clés", max_length=250, null=True)
    is_published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    main_photo = models.ForeignKey(Photo, on_delete=models.DO_NOTHING, null=True)

    @property
    def content_html(self):
        content_html = markdown(self.content)
        content_html = self.process_tag_image(content_html)
        return mark_safe(content_html)

    def process_tag_image(self, content_html):
        r = re.compile(r"{img (?P<src>[\S]+)( )?((?P<width>[\d]+)\*(?P<height>[\d]+))?( )?(?P<float>left|right)?}")

        def repl(m):
            data = m.groupdict()
            tag = f"<img src={data['src']}"
            if "width" in data:
                tag += f" width={data['width']}"
            if "height" in data:
                tag += f" width={data['height']}"
            if "float" in data:
                if data["float"] == "right":
                    tag += ' class="float-end"'
                else:
                    tag += ' class="float-start"'
            tag += " />"
            return tag
        return r.sub(repl, content_html)

    def save(self, *args, **kwargs):
        self.content = escape(self.content)
        if not self.slug:
            base_slug = slug = slugify(self.title)
            while self.__class__.objects.filter(slug=slug).exists():
                slug = base_slug + str(randrange(1000, 10000))
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_post:detail", kwargs={"slug": self.slug})
