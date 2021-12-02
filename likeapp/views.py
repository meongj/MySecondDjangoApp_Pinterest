from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


# 트랜잭션
@transaction.atomic
def db_transaction(user, article):
    # LikeRecord 값이 있는 지 확인
    if LikeRecord.objects.filter(user=user, article=article).exists():
        # 에러 처리
        raise ValidationError('Like already exists!')
    else:
        LikeRecord(user=user, article=article).save()

    # 없으면 like 값 1추가
    article.like += 1
    article.save()


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):

        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        try:
            db_transaction(user, article)
            # django message 구현
            messages.add_message(self.request, messages.SUCCESS, '좋아요가 반영되었습니다.')
        except:
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다.')
            # 있으면 다시 보내고
            return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})


        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
