from rest_framework import generics

from .serializers import ProfileSerializer
from portfolio.models import UserProfile

class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = ProfileSerializer    
    
    def get_queryset(self):
        return UserProfile.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    
class ProfileUpdateAPIView(generics.UpdateAPIView):
    lookup_field = 'slug'
    serializer_class = ProfileSerializer
    