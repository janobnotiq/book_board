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

    def __str__(self) -> str:
        return self.name
    

class Book(BaseModel):
    title = models.CharField(max_length=256)
    categories = models.ManyToManyField(Category,related_name="books")
    author = models.CharField(max_length=256)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    pub_year = models.IntegerField(verbose_name="Nashr qilingan yili")

    def __str__(self) -> str:
        return self.title
    

# class Review(BaseModel):
#     book = models.ForeignKey(Book,on_delete=models.CASCADE)
#     author = models.ForeignKey()