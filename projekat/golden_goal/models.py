# autori:
# Dejan Kovacevic 0167/2019
# Srdjan Kuzmanovic 0169/2019

from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


# Klasa koja predstavlja tabelu User u bazi i sluzi za objektno relaciono mapiranje
class User(AbstractUser):
    type = models.CharField(max_length=20, default='administrator')
    score = models.IntegerField(default=0)
    double_prediction_counter = models.IntegerField(default=0)
    presents = models.IntegerField(default=0)
    image = models.CharField(max_length=250, default='images/image_0.png')

    class Meta:
        db_table = 'user'


# Klasa koja predstavlja tabelu News u bazi i sluzi za objektno relaciono mapiranje
class News(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(default='')
    content = models.TextField()
    date_time = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'news'


# Klasa koja predstavlja tabelu Comment u bazi i sluzi za objektno relaciono mapiranje
class Comment(models.Model):
    text = models.TextField()
    date_time = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'comment'


# Klasa koja predstavlja tabelu Present u bazi i sluzi za objektno relaciono mapiranje
class Present(models.Model):
    type = models.CharField(max_length=45)
    image = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'present'


# Klasa koja predstavlja tabelu Prediction u bazi i sluzi za objektno relaciono mapiranje
class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.IntegerField()
    type = models.CharField(max_length=2)  # 1, X, 2, 1X, 2X, 12

    class Meta:
        db_table = 'prediction'
        constraints = [models.UniqueConstraint(fields=['user', 'game'], name='prediction_primary_key')]


# Klasa koja predstavlja tabelu UserImage u bazi i sluzi za objektno relaciono mapiranje
class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.IntegerField()

    class Meta:
        db_table = 'user_image'
        constraints = [models.UniqueConstraint(fields=['user', 'image'], name='user_image_primary_key')]
