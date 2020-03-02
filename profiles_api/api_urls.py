from django.urls import path
from profiles_api import api_views

urlpatterns = [
    path('v1/',api_views.HelloApiView.as_view()),
]
