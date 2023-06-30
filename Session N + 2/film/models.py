from django.db import models
from utils.models import BaseModel

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=100)
    # name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Film(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    language = models.CharField(max_length=20)
    release_year = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_date = models.DateField()
    category = models.ManyToManyField(Category)


    def __str__(self):
        return self.title
