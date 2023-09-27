from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    dateOfBirth = models.DateField(null=True)
    picture = models.ImageField(upload_to='profile/')
    def __str__(self):
        return self.firstName

class Room(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    roomMembers = models.ManyToManyField(User, related_name='rooms')

    def __str__(self):
        return self.name

class RoomMessages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender.username}: {self.content}'