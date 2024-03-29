from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User, PermissionsMixin


class User(User, PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
