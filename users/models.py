from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128, null=False)
    phone_number = models.BigIntegerField(blank=True, null=True)

    def user_display_name(self):
        return self.first_name + ' ' + self.last_name