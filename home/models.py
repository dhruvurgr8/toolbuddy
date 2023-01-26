from django.db import models

# Create your models here.
class Myfiles(models.Model):
    file = models.ImageField(upload_to='media',blank=True,null=True)

    def __str__(self):
        return self.file