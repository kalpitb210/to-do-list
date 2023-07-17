from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ToDoItem(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.title
