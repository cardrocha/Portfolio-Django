from django.db import models

class Project(models.Model):
    upload = models.CharField(max_length=150)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    deploy = models.CharField(max_length=100)
    project = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
