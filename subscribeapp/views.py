from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # project와 user정보 취합
        # 단축함수 get_object_or_404
        # Project_pk를 가지고 있는 애를 찾는데 없으면 404 에러뜸
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # user가 우리가 찾은 user인지
        # project가 우리가 찾은 Project인지 구독정보 찾는다
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)

        # 그러한 구독정보 있으면
        if subscription.exists():
            # 구독정보 삭제
            subscription.delete()
        else:
            # 없으면 만들어주고 저장
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    # 가져오는 게시글의 조건 바꿀 수 있음
    def get_queryset(self):
        # values_list는 Subscription의 project가져온 값들을 list화 시킨다.
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # list화 시킨 projects를 Field Lookups 형태로 만들어줌
        article_list = Article.objects.filter(project__in=projects)
        return article_list