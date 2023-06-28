from django.db import models


# Create your models here.
class Categorys(models.Model):
    Name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f"{self.Name.lower()}"


