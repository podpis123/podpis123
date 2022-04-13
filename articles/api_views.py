from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Article
from .api_permissions import IsAuthorOrReadOnly
from .serializers import ArticleSerializer


class ArticleList(ListCreateAPIView):
    """
    get:
    Return a list of all the existing articles.

    post:
    Create a new article instance.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    """
    get:
    Return current artiicle.

    put:
    Update current article.
    """
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
