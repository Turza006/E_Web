from django.db import models

# Create your models here.
class Catagory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    detail = models.TextField()
    url = models.TextField()
    view = models.IntegerField(default=1)
    catagorys = models.TextField(null=True,blank=True)
    seller = models.TextField()
    pub_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name