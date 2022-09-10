from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class myUser(AbstractUser):
    class myUserClasses(models.TextChoices):
        SUPER_USER = 'super', 'Superuser'
        TEST_USER = 'test', 'Test User'
        CAMS_USER = 'cams', 'Cams App Manager'
        CAMPENDIUM_USER = 'campendium', 'Hypershrub Forest Account'
        DEFAULT_USER = 'default', 'Default user class'

    user_class = models.CharField(
        max_length=30, 
        choices=myUserClasses.choices, 
        default=myUserClasses.DEFAULT_USER
        )