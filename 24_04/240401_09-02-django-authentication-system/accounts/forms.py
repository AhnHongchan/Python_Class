from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # 현재 django 프로젝트에 활성화된 User 객체를 반환하는 함수
        model = get_user_model()
        # 왜 직접 참조하지 않는가?
        # Usermodel의 이름이 바뀐다던가, User model이 갈아끼워지거나 등
        # 변화가 생길 때마다 직접 바꿔줘야 함
    
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)