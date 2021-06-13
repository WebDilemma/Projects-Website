from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from rest_framework import filters
from django.db.models import Q

from django.core.validators import validate_email

from .serializers import ProfileSerializer
from portfolio.models import UserProfile
from .permissions import IsOwnerOrReadOnly


@api_view(['GET'])
@permission_classes([AllowAny])
def profile_retirve_api_view(request, slug):
    try:
        user_profile = UserProfile.objects.get(slug=slug)
    except:
        return Response({
            'data': {
                'error':'User Not Found'
                },
        })
    serializer =ProfileSerializer(user_profile, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile_delete_api_view(request):
    try:
        user_profile = request.user.userprofile
    except:
        return Response({
            'data': {
                'error':'User Not Found'
                },
        })
    try:
        user_profile.delete()
        response = {
            'deleted': True,
        }
        return Response(response, status=200)
    except:
        response = {
            'deleted': False,
        }
        return Response(response, status=401)


class ProfileUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    
    def patch(self, *args, **kwargs):
        user_profile = self.request.user.userprofile
        serializer = ProfileSerializer(user=user_profile, data=self.request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save().user
            
            response = {'success': True, 'message': 'successfully updated your info',
                        'user': ProfileSerializer(user).data}
            
            new_email = self.request.data.get('email')
            user = self.request.user
            
            if new_email is not None:
                email = validate_email(new_email)
                user.email = email
                user.save()
            return Response(response, status=200)
        else:
            response = serializer.errors
            return Response(response, status=401)
        

            
    
class ProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'about', 'projects__title']
    ordering_fields = '__all__'
    
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    

    

    