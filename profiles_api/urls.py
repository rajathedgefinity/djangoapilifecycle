from django.urls import path, include
from . import api_urls

urlpatterns = [
    path('api/',include('profiles_api.api_urls')),
]
