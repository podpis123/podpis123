from rest_framework import serializers

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title', 'body', 'author', 'created_at', 'updated_at')
        model = Article