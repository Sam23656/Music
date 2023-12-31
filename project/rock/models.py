from django.db import models
from category.models import Categorys


# Create your models here.


class Rock(models.Model):
    Category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    Author_Name = models.CharField(max_length=50)
    Author_Sure_Name = models.CharField(max_length=50)
    Author_Age = models.PositiveIntegerField()
    Info = models.TextField()

    def __str__(self):
        return f"{self.Author_Name} - {self.Author_Sure_Name}"