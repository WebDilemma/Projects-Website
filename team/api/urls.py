from django.urls import path

from .views import TeamMemberRetrieveUpdateDestroyAPIView, TeamListAPIView

app_name = 'team-api'

urlpatterns = [

    path('list/', TeamListAPIView.as_view(), name='list-api'),
    path('<int:pk>/', TeamMemberRetrieveUpdateDestroyAPIView.as_view(), name='detail-api'),
    
]