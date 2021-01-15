from django.db import models

# Create your models here.
class Job(models.Model):
    loaction = models.CharField(max_length = 30)
    lastdate   = models.CharField(max_length = 20)
    sal  = models.IntegerField()
    discri = models.CharField(max_length = 30)
    def __str__(self):
        return self.discri