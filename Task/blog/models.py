from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    # id = integer fieald on delete primary key true
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title + ' - ' + str(self.user)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
