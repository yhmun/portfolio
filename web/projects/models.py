from django.db import models

def project_upload_to(instance, filename):
    return 'projects/{0}/{1}'.format(instance.id, filename);

class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=128)
    description = models.TextField()
    framework = models.CharField(max_length=64)
    image = models.ImageField(upload_to=project_upload_to) 

    def __str__(self):
        return f"Project(id={self.id}, title={self.title})"