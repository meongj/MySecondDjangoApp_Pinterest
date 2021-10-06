from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.models import HelloWorld

# 컨트롤러 단,,
from accountapp.templates.accountapp.forms import AccountUpdateForm


def hello_world(request):

    if request.method == "POST":
        # hello_world_input이름의 input태그 값 가져오기
        temp = request.POST.get('hello_world_input')
        # HelloWorld 모델 가져오기
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        # db에 저장
        new_hello_world.save()

        # db에 저장한 데이터 불러오기
        # hello_world_list = HelloWorld.objects.all()
        # HttpResponseRedirect는 새로고침해도 기존정보 불러오지 않게 방지
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


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


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm # 수정한 form으로 변경
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'