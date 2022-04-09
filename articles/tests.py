from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Article

# Create your tests here.

class ArticleTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@example.com", password="secret"
        )

        cls.article = Article.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user,
        )

    def test_article_model(self):
        self.assertEqual(self.article.title, "A good title")
        self.assertEqual(self.article.body, "Nice body content")
        self.assertEqual(self.article.author.username, "testuser")
        self.assertEqual(str(self.article), "A good title")
        self.assertEqual(self.article.get_absolute_url(), "/articles/1/")

    def test_url_listview_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_detailview_status_code(self):
        response = self.client.get("/articles/1/")
        self.assertEqual(response.status_code, 200)

    def test_article_listview(self):
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "article_list.html")

    def test_article_detailview(self):
        response = self.client.get(reverse("article_detail", kwargs={"pk": self.article.pk}))
        no_response = self.client.get("/articles/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "article_detail.html")