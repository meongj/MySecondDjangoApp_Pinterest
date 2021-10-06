from django.db.models import fields
from django.forms import ModelForm

from profileapp.models import Profile


# ModelForm으로 model-> form으로 만들기
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']