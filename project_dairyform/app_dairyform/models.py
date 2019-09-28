from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('F','Female'),
    ('M', 'Male'),
)


class Farmer(models.Model):
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Female')
    ContactNumber = models.CharField(max_length=10)
    Age = models.IntegerField(default=0)
