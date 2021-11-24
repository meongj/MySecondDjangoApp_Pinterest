from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        # 따옴표('') 앞에 f를 붙이면 직접 변수 출력 가능
        # model의 pk : 글 제목 (프로젝트 create에서 프로젝트 목록 선택시 보이도록)
        return f'{self.pk} : {self.title}'