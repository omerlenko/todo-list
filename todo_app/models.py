from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
