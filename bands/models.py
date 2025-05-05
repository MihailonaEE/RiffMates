from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()
    def __srt__(self):
        return f"Musician(id={self.id}, last_name={self.last_name})"
