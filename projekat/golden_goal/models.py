from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


# class User(AbstractUser):
#     type = models.CharField(max_length=20)
#     score = models.IntegerField()
#     double_prediction_counter = models.IntegerField()
#     image = models.IntegerField()
#
#     class Meta:
#         db_table = 'user'
#
#
# class News(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_time = datetime.datetime.now()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'news'
#
#
# class Comment(models.Model):
#     text = models.TextField()
#     date_time = datetime.datetime.now()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     news = models.ForeignKey(News, on_delete=models.CASCADE)
#     comment_reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
#
#     class Meta:
#         db_table = 'comment'
#
#
# class Present(models.Model):
#     type = models.CharField(max_length=45)
#     image = models.IntegerField(null=True)
#     points = models.IntegerField(null=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'present'
#
#
# class Prediction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     game = models.IntegerField()
#     type = models.CharField(max_length=2)  # 1, X, 2, 1X, 2X, 12
#
#     class Meta:
#         db_table = 'prediction'
#         models.UniqueConstraint(fields=['user', 'game'], name='prediction_primary_key')
#
#
# class UserImage(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.IntegerField()
#
#     class Meta:
#         db_table = 'user_image'
#         models.UniqueConstraint(fields=['user', 'image'], name='user_image_primary_key')