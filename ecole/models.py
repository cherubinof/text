from django.db import models

# Create your models here.

class Inscription(models.Model):
    nom = models.CharField(max_length=50)
    email = models.EmailField()
    numero = models.IntegerField()

    
