from django.urls import path
from .views import (
    DocumentListView,
    DocumentUpdateView,
    DocumentDetailView,
    DocumentDeleteView,
    DocumentCreateView,
)

urlpatterns = [
    path("<int:pk>/", DocumentDetailView.as_view(), name="document_detail"),
    path("<int:pk>/edit/", DocumentUpdateView.as_view(), name="document_edit"),
    path("<int:pk>/delete/", DocumentDeleteView.as_view(), name="document_delete"),
    path("new", DocumentCreateView.as_view(), name="document_new"),
    path('', DocumentListView.as_view(), name='document_list'),
]