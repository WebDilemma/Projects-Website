from django.urls import path

from .views import (
    ContactCreateView,
    ContactListView,
    ContactRetrieveView,
    ContactRetriveUpdateDeleteView
)

app_name = 'contact-api'

urlpatterns = [

    path('list/', ContactListView.as_view(), name='list-api'),
    path('create/', ContactCreateView.as_view(), name='create-api'),
    path('update/<int:pk>', ContactRetriveUpdateDeleteView.as_view(), name='update-api'),
    path('<int:pk>/', ContactRetrieveView.as_view(), name='detail-api'),
    
    
]
