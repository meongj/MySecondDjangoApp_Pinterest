# 유저 정보 변경시 아이디 정보 비활성화를 위한
# UserCreationForm 상속 받아서 변경

from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    # 초기화 이후에 username칸만 비활성화
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True