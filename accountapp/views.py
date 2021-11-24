from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.migrations import writer
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required

# 컨트롤러 단,,
from accountapp.forms import AccountUpdateForm


# 배열에 담기
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    # 장고에서 제공한 User테이블 불러오기
    model = User
    # 장고에서 제공하는 UserCreationForm 불러오기, 인증 검증작업
    form_class = UserCreationForm

    # reverse : 함수내에서 사용불가로
    # reverse_lazy로 사용함, 링크연결 위함 / 라우팅
    success_url = reverse_lazy('accountapp:hello_world')
    # 어느 app에서 볼껀지 설정, 사용자화면단
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        # 필터링한 article 정보 object_list로 넘겨주기
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)



@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm # 수정한 form으로 변경
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'