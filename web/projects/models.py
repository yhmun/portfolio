from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.CharField(max_length=100)
    image = models.FilePathField(path="")

    def __str__(self):
        return f"Project(id={self.id}, title={self.title})"
