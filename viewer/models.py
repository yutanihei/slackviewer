#　ここに変更加えたら makemigrations→migrate 忘れないように！！！

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # channelと結ぶ
    channel = models.ForeignKey("Channel", on_delete=models.CASCADE)
    # userと結ぶ
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    ts = models.DateTimeField()
    def __str__(self):
        return self.text

class Channel(models.Model):
    # id
    channel_id = models.CharField(max_length=50)
    # name
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class User(models.Model):
    # id
    user_id = models.CharField(max_length=50)
    # nameはemailかな
    name = models.CharField(max_length=50)
    # real_name
    real_name = models.CharField(max_length=50)
    
    # imageもいれたいね

    def __str__(self):
        return self.real_name
    
