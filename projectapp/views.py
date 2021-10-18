from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


# MultipleObjectMixin : 여러개의 오브젝트들을 다룰 수 있는 Mixin
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        # user가 로그인했는지 확인
        if user.is_authenticated:
            # 구독정보 확인
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None

        # Article 오브젝트가져와서 필터링
        object_list = Article.objects.filter(project=self.get_object())
        # 탬플릿 창에서 object_list를 가져와서 필터링한 게시글들을 사용할 수 있음
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)



class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25
