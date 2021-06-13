from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from rest_framework import filters
from django.db.models import Q

from .serializers import TeamSerializer
from team.models import OurTeam
from .permissions import IsOwnerOrReadOnly

   
class TeamListAPIView(generics.ListAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = TeamSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'name', 'user__first_name']
    ordering_fields = '__all__'
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    
    
@api_view(['GET'])
@permission_classes([AllowAny])
def team_profile_retirve_api_view(request, pk):
    try:
        team_profile = OurTeam.objects.get(pk=pk)
    except:
        return Response({
            'data': {
                'error':'User Not Found'
                },
        })
    serializer =TeamSerializer(team_profile, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser, IsOwnerOrReadOnly])
def team_profile_delete_api_view(request, pk):
    try:
        team_profile = OurTeam.objects.get(pk=pk)
    except:
        return Response({
            'data': {
                'error':'User Not Found'
                },
        })
    try:
        team_profile.delete()
        response = {
            'deleted': True,
        }
        return Response(response, status=200)
    except:
        response = {
            'deleted': False,
        }
        return Response(response, status=401)


class TeamProfileUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = TeamSerializer
    lookup_field = ['pk']
    
    def patch(self, *args, **kwargs):
        pk = self.lookup_field
        team_profile = OurTeam.objects.get(pk=pk)
        serializer = TeamSerializer(user=team_profile, data=self.request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save().user
            
            response = {'success': True, 'message': 'successfully updated your info',
                        'user': TeamSerializer(user).data}
            
            new_email = self.request.data.get('email')
            user = self.request.user
            
        else:
            response = serializer.errors
            return Response(response, status=401)
    