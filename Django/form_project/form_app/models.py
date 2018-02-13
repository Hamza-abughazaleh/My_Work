from django.db import models

# Create your models here.
class form_submit(models.Model):
    name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264,unique="True")
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.name
