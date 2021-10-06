from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # form 데이터 가져와서 임시저장
        # user정보는 가져오지 않음, 제외시켰음
        temp_profile = form.save(commit=False)
        # temp의 user정보가져와서 당사자인 user로 request보냄
        temp_profile.user = self.request.user
        # 정상적으로 저장
        temp_profile.save()
        # 작성한 form 리턴
        return super().form_valid(form)