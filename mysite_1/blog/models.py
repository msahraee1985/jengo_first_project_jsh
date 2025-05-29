from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(
        max_length=250,
        allow_unicode=True,
    )
    body = models.TextField(

    )

    def __str__(self):
        return self.title