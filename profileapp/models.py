from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    # 1:1 매칭
    # OneToOneField은 장고제공 1:1 매칭해주는 함수
    # 테이블 연결된 테이블도 DELETE되도록 설정
    # related_name는 바로 연결할 수 있도록 name지정한 것
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # upload_to는 이미지를 다른 서버 어디에 저장할 껀지
    # media/profile 경로로 추가되어짐
    image = models.ImageField(upload_to='profile/', null=True)

    # nickname은 유일해야함
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)