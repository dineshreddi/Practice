from django.db import models

# Create your models here.
class person(models.Model):
    name=models.CharField(max_length=20,unique=True)
    age=models.IntegerField()
    email=models.CharField(max_length=20,unique=True)
    phone=models.CharField(max_length=10, unique=True)
    gender=models.CharField(max_length=10)
    locations=[('ind',"india"),('aus',"AUS")]
    location=models.CharField(max_length=10,choices=locations)
    marital_status=models.CharField(max_length=10)
    def __unicode__(self):
        return self.name
