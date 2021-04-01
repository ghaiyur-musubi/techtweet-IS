"""
user - FK
body - CharField - max L 255
created_at - DateTimeField
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary


# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User,
                             related_name='tweets',
                             on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=255)
    image = CloudinaryField('Image attached to the tweet', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Desc Sort the tweets
    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return "{0} at {1}: {2}...".format(self.user,self.created_at,self.body[:20])