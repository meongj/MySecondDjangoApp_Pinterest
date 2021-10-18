from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # Textarea의 attrs는 미리 class와 style을 지정해줌
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable ',
                                                           'style': 'height:auto;text-align : left'}))

    # 프로젝트 생성시 해당 프로젝트에 해당하는 프로젝트가 나오도록 설정
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']