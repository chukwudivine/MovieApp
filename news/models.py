
from django.db import models
from django.shortcuts import render


class News(models.Model):
    headline = models.CharField(max_length=200)
    image = models.ImageField(upload_to='news/images/')
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.headline





# Create your models here.