from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Type,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name','category']

class Record(models.Model):
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    type = models.ForeignKey(Type,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.SET_NULL,null=True)
    sum = models.CharField(max_length=100)
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.date}"