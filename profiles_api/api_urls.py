from django.urls import path, include
from profiles_api import api_views
from profiles_api import api_routers

urlpatterns = [
    path('v1apiview/',api_views.HelloApiView.as_view()),
    path('login/', api_views.UserLoginApiView.as_view()),
    path('v1viewset/',include(api_routers.router.urls)),
]
