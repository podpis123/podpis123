from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Document


# Create your views here.
class DocumentListView(LoginRequiredMixin,ListView):
    model = Document
    template_name = "document_list.html"
    login_url = 'login'
    paginate_by = 20

    def get_queryset(self):
        return Document.objects.filter(owner=self.request.user)


class DocumentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Document
    template_name = "document_detail.html"
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class DocumentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Document
    fields = ("name", "description", )
    template_name = "document_edit.html"
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user

class DocumentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Document
    template_name = "document_delete.html"
    login_url = 'login'
    success_url = reverse_lazy("document_list")

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user


class DocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    template_name = "document_new.html"
    login_url = 'login'
    fields = ("name", "description",)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)