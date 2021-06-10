from django.urls import path

from .views import ProfileRetrieveUpdateDestroyAPIView, ProfileListAPIView

app_name = 'profile-api'

urlpatterns = [

    path('list/', ProfileListAPIView.as_view(), name='list-api'),
    path('<slug:slug>/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='detail-api'),

]
