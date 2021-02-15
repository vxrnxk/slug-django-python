from django.db import models
from django.utils.text import slugify

class Page(models.Model):
    title = models.CharField(max_length=200)
    uri = models.SlugField(max_length=200, blank=True, unique=True)

    class Meta:
        verbose_name = "page"
        verbose_name_plural = "pages"

    def save(self, *args, **kwargs):
        self.uri = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
        