from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Document

# Create your tests here.

class DocumentTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@example.com", password="secret"
        )

        cls.document = Document.objects.create(
            name="A good title 2",
            description="Nice document content",
            owner=cls.user,
        )

    def test_document_model(self):
        self.assertEqual(self.document.name, "A good title 2")
        self.assertEqual(self.document.description, "Nice document content")
        self.assertEqual(self.document.owner.username, "testuser")
        self.assertEqual(str(self.document), "A good title 2")
        self.assertEqual(self.document.get_absolute_url(), "/documents/1/")

    def test_url_listview_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_detailview_status_code(self):
        response = self.client.get("/documents/1/")
        self.assertEqual(response.status_code, 200)

    def test_document_listview(self):
        response = self.client.get(reverse("document_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title 2")
        self.assertTemplateUsed(response, "document_list.html")

    def test_document_detailview(self):
        response = self.client.get(reverse("document_detail", kwargs={"pk": self.document.pk}))
        no_response = self.client.get("/documents/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title 2")
        self.assertTemplateUsed(response, "document_detail.html")