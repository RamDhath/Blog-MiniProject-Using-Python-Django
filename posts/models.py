from django.db import models
from ckeditor.fields import RichTextField


class NewPost(models.Model):
    OPTIONS = [
        ('View-All', 'View-All'),
        ('Social', 'Social'),
        ('Current-Affairs', 'Current-Affairs'),
        ('Newspaper-cuts', 'Newspaper-cuts'),
        ('Travel', 'Travel'),
        ('Others', 'Others'),
    ]

    heading = models.CharField(max_length=100, default=None)
    category = models.CharField(max_length=40, choices=OPTIONS, default=None)
    tags = models.CharField(max_length=100, default=None)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.heading
