from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class CreateUser(models.Model):
    genders = (('male', 'male'), ('female', 'female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    gender = models.CharField(choices=genders, max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail = models.EmailField()
    image = models.ImageField(blank='True', default='anonym.png')

    def __str__(self):
        return self.first_name + self.last_name
