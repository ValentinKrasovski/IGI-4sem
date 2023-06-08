from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    custom user
    """
    first_name = models.CharField(max_length=200,
                                  help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                 help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'email',
                       'date_of_birth',
                       'phone_number']
