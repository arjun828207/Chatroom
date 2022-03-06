from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic= models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200, null=False)
    description=models.TextField(max_length=500,null=True,blank=True)
    #participants=models.ManyToManyField
    updated = models.DateTimeField(auto_now=True)#take snapshot of timestamp updated
    created = models.DateTimeField(auto_now_add=True)#take snapshot of timestamp created
    
    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name

class Messages(models.Model):
    user = models.ForeignKey(User,on_delete=CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)#take snapshot of timestamp updated
    created = models.DateTimeField(auto_now_add=True)#take snapshot of timestamp created
    
    def __str__(self):
        return self.body[0:50]
 


