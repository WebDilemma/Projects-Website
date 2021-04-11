from django.urls import path

from .views import (
    ContactCreateView,
    ContactListView,
    ContactRetrieveView,
)

app_name = 'project-api'

urlpatterns = [

    # path('profile/<slug:slug>/delete/', profile_delete_view, name='delete'),
    path('<slug:slug>', ProfileRetrieveAPIView.as_view(), name='detail-api'),
    # path('profile/<slug:slug>/edit/', profile_edit_view, name='edit'),

]
