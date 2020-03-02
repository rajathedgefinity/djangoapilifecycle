from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import api_permissions
from profiles_api import serializers
from profiles_api import models


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most contral over you application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a Hello Message with our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating an Object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle Partial Update of an Object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API for Django ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello World Message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'viewset':a_viewset})

    def create(self, request):
        """Create a New hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by it's ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle Updating an Object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle Updating part an Object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an Object"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
      """Handle creating and updating Users Profile"""
      serializer_class = serializers.UserProfileSerializer
      queryset = models.UserProfile.objects.all()
      authentication_classes = (TokenAuthentication,)
      permission_classes = (api_permissions.UpdateOwnProfile,)
      filter_backends = (filters.SearchFilter,)
      search_fields = ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle Creating User Authentication Tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
