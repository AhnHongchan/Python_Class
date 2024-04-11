from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

# 왜 장고에 내장된 모델폼과 유사할까?
# 외부에서 설치한 것임에도 불구하고
# DRF가 설계를 기존 장고 사용자들을 위해 유사하게 설계함
# DRF를 쓰는 사람들이 django 개발자이므로

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'