from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from rest_framework import filters
from django.db.models import Q

from .serializers import TeamSerializer
from team.models import OurTeam
from .permissions import IsOwnerOrReadOnly

   
class TeamListAPIView(generics.ListAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'about', 'projects__title']
    ordering_fields = '__all__'
    
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
    