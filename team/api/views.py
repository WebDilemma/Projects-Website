from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import TeamSerializer
from team.models import OurTeam
from .permissions import IsOwnerOrReadOnly

   
class TeamListAPIView(generics.ListAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser ]
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    
    
class TeamMemberRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TeamSerializer    
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser ]
    
    def get_queryset(self):
        return OurTeam.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    