from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.
class post(models.Model):
    class Status(models.TextChoices):
        DRAFT = ('DF','Draft')
        PUBLISHED = ('PB','Published')
    title = models.CharField(
        max_length=250,
    )
    slug = models.SlugField(
        max_length=250,
        allow_unicode=True,
    )
    body = models.TextField(

    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='blog_post',
    )
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    published = models.DateTimeField(
        default=timezone.now,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )
    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(
                fields=['-published'],
            )
        ]


    def __str__(self):
        return self.title
