from django.db import models
from root.models import BaseModel

# Create your models here.

class Category(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.name
    

class Publisher(BaseModel):
    name = models.CharField(max_length=256)
    

class Book(BaseModel):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.CharField(max_length=256)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    pub_year = models.IntegerField(verbose_name="Nashr qilingan yili")

    def __str__(self) -> str:
        return self.title
    

# class Review(BaseModel):
#     book = models.ForeignKey(Book,on_delete=models.CASCADE)
#     author = models.ForeignKey()