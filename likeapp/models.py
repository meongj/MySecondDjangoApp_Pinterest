from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')

    # user, article 한 쌍의 모델이 유니크한 항목이 되도록 meta 클래스 지정
    class Meta:
        unique_together = ('user', 'article')