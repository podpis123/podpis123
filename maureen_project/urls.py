"""maureen_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

api_docs = include_docs_urls(title='Maurren API', description="Signig web portal.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('documents/', include('documents.urls')),
    path('api/v1/articles/', include('articles.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/docs/', api_docs, name='api_docs'),
    path('api/v1/schema/', get_schema_view(), name='api_schema'),
    path('', include('pages.urls')),
]
