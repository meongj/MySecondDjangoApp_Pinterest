from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [
    # 장고지정 TemplateView
    # 템플릿만 지정해주면 알아서 만들어줌
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]