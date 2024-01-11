from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(
        validators=[EmailValidator(message="Invalid email address")]
    )
    birthday = models.DateField(null=True, blank=True)
    pic = models.ImageField(upload_to="profiles", default="")
    notes = models.TextField()

    def __str__(self):
        return str(self.name)
