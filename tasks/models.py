from django.db import models

# Create your models here.

class Tasktodo(models.Model):
    title = models.CharField(max_length=122, default='task1')
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title