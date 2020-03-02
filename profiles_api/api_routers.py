from rest_framework import routers
from profiles_api import api_views

router = routers.DefaultRouter()
router.register('hello-viewset',api_views.HelloViewSet, basename='hello-viewset')
router.register('profile', api_views.UserProfileViewSet)
