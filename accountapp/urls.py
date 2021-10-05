from django.urls import path

from accountapp.views import hello_world


app_name = "accountapp"

urlpatterns = [
    # localhost:8000/account/hello_world 주소로 갑니다
    # accountapp:hello_world 이렇게 해도 갑니다(app_name쓰는 이유)
    # hello_world view로 갑니다
    path('hello_world/', hello_world, name='hello_world'),
]