from django.db import models
from django.contrib.auth.models import AbstractUser
from PocketService.abstract_models import TimeStampModel


# Create your models here.
class User(AbstractUser):

    def user_display_name(self):
        return self.first_name + ' ' + self.last_name



class Client(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class ServiceWorker(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


# This one may not be used due to django already having a default admin interface/management
# Though this might be useful for the mobile side to manage everything on the phone while on the go
class PsAdmin(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

