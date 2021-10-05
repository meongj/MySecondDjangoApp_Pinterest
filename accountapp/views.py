from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    if request.method == "POST":
        # hello_world_input이름의 input태그 값 가져오기
        temp = request.POST.get('hello_world_input')
        # HelloWorld 모델 가져오기
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save() # db에 저장

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
