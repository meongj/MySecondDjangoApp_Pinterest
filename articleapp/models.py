from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    # SET_NULL : User 탈퇴시에도 게시글은 삭제되지 않음 (알수없음)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    title = models.CharField(max_length=200, null=True)
    # 이미지는 article/ 경로 밑에 저장
    # 이미지는 항상 넣도록 하기
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)
    # 생성됬을 때 자동으로 생성시간 저장됨
    created_at = models.DateField(auto_now_add=True, null=True)
