from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld

# 컨트롤러 단,,


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
