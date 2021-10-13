from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    # 이미 구독하고 있는 것 또 구독못하게 설정
    class Meta:
        # user와 project 한쌍이 가지고 있는 Subscription은 오직하나만 설정
        unique_together = ('user', 'project')