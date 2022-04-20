from django.db import models


# Create your models here.


class ToDo(models.Model):
    todo = models.TextField()
    user = models.CharField(max_length=300)

    def __str__(self):
        return self.todo
