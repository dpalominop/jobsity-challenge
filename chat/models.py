from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}: {} - {}".format(self.author, self.message, self.created)


class Room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
