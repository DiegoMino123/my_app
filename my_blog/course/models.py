from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Course: {self.name} | code: {self.code}"


class Homework(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()

    def __str__(self):
        return f"{self.name} | fecha: {self.due_date}"
