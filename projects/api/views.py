from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from rest_framework import filters
from django.db.models import Q

from projects.models import Project 

from .serializers import ProjectSerializer
from .permissions import IsOwnerOrReadOnly

class ProjectCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProjectSerializer
        

@api_view(['GET'])
@permission_classes([AllowAny])
def project_retirve_api_view(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except:
        return Response({
            'data': {
                'error':'Project Not Found'
                },
        })
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsOwnerOrReadOnly, IsAdminUser])
def project_delete_api_view(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except:
        return Response({
            'data': {
                'error':'Project Not Found'
                },
        })
    try:
        project.delete()
        response = {
            'deleted': True,
        }
        return Response(response, status=200)
    except:
        response = {
            'deleted': False,
        }
        return Response(response, status=401)


class ProjectUpdateAPIView(APIView):
    permission_classes = [IsAdminUser, IsOwnerOrReadOnly]
    serializer_class = ProjectSerializer
    lookup_field = ['slug']
    
    def patch(self, *args, **kwargs):
        slug = self.lookup_field
        project = Project.objects.get(slug=slug)
        serializer = ProjectSerializer(user=project, data=self.request.data, partial=True)
        if serializer.is_valid():
            project = serializer.save()
            
            response = {'success': True, 'message': 'successfully updated your info',
                        'user': ProjectSerializer(project).data}
        
            return Response(response, status=200)
        else:
            response = serializer.errors
            return Response(response, status=401)
    

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
            
            
            
            






