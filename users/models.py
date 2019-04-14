from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from PocketService.abstract_models import TimeStampModel
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone numbers must be 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)

    def user_display_name(self):
        return self.first_name + ' ' + self.last_name

# Signals
# @receiver(models.signals.post_save, sender=User)
# def execute_after_save(sender, instance, created, *args, **kwargs):
#     if created:


class Client(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)


    @classmethod
    def create(cls, user):
        client = cls(user=user)
        return client

class ServiceWorker(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    @classmethod
    def create(cls, user_id):
        worker = cls(user_id=user_id)
        return worker


# This one may not be used due to django already having a default admin interface/management
# Though this might be useful for the mobile side to manage everything on the phone while on the go
class PsAdmin(TimeStampModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

