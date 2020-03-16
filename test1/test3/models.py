from django.db import models
from django.utils import timezone

# Create your models here.

# each model represent a table in the database 
# and ID will be generated automatically
class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return "<Name: {}>".format(self.name)