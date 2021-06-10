from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import ProfileSerializer
from portfolio.models import UserProfile
from .permissions import IsOwnerOrReadOnly

class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = ProfileSerializer    
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser ]
    
    def get_queryset(self):
        return UserProfile.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    
class ProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser ]
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    

    

    