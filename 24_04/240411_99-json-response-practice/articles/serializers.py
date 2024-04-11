from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'

# ModelForm이랑 똑같이 생김
# ModelForm 상속 받듯이 ModelSerializer를 상속받는다.
# 이제 Json 형태로 준다.
# 페이지처럼 보이지만 이건 라이브러리 하나를 설치해서 생긴 것이다.
# 실제로는 데이터 자체를 클라이언트에 응답하는 걸 확인할 수 있다.
# http://127.0.0.1:8000/api/v1/articles/
