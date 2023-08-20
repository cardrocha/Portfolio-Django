from django.db import models

class Project(models.Model):
    upload = models.FileField(upload_to="uploads/")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    deploy = models.CharField(max_length=100)
    project = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.none
