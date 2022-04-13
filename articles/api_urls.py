from django.urls import path
from .api_views import ArticleList, ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view(), name='api_article_list'),
    path('<int:pk>/', ArticleDetail.as_view(), name='api_article_detail'),
]