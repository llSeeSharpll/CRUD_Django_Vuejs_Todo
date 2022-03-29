from django.db import models

# Create your models here.
class Todo(models.Model):
    Task = models.CharField(max_length=100)
    Description = models.TextField()
    Completed = models.BooleanField(default=False)
    Toggle = models.BooleanField(default=False)

    def __str__(self):
        return self.title
