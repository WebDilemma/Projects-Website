from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework import filters
from django.db.models import Q

from projects.models import Project 

from .serializers import ProjectSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProjectSerializer
    

        

class ProjectRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'slug'
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    
    

class ProjectListAPIView(generics.ListAPIView):
    permission_classes = []
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    serach_fields = ['title', 'text', 'categorie', 'tools__in']
    ordering_fields = '__all__'

    
    def get_queryset(self, *args, **kwargs):
        qs = self.request.GET.get('q')
        query = Project.objects.all()
        if qs is not None:
            query = query.filter(
                Q(title__icontains = qs)|
                Q(text__icontains = qs)|
                Q(categorie__icontains = qs)|
                Q(tools__in = qs)
                ).distinct()
        return query
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
            
            
            
            






