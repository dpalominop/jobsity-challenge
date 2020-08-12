from django.db import models


class Post(models.Model):
    room = models.ForeignKey('Room',on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.created, self.message)


class Room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
