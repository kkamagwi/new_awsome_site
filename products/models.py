from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Product(models.Model):
    tag = models.ManyToManyField(Tag, related_name='tags')
    price = models.IntegerField(default=0)
    author = models.CharField(max_length=63)
    phone_number = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
