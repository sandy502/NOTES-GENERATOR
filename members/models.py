from django.db import models

# Create your models here.
# start by creating a Members class, and describe the table fields in it:
# A QuerySet is a collection of data from a database.

class Members(models.Model):
    firsname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)