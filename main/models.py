from django.db import models

# Create your models here.
class Record(models.Model):
    date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    sum = models.CharField(max_length=100)
    comment = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.date}"