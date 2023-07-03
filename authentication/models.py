from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

    # def __str__(self):
    #     if self.email:
    #         return self.email
    #     else:
    #         return self.phone_number
    #
    # def get_username(self):
    #     if self.email:
    #         return self.email
    #     else:
    #         return self.phone_number
