from rest_framework import generics
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import filters

from queries.models import ContactModel
from .serializers import ContactReadSerializer, ContactCreateSerializer
from .permissions import IsOwnerOrReadOnly

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactCreateSerializer
    

class ContactListView(generics.ListAPIView):
    lookup_field = 'slug'
    queryset = ContactModel.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ContactReadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['email', 'text', 'title']
    ordering_fields = '__all__'
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }

class ContactRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = ContactModel.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = ContactReadSerializer
    
    def get_serializer_context(self, *args, **kwargs):
        return { "request":self.request }
    
class ContactRetriveUpdateDeleteView(generics.UpdateAPIView, DestroyModelMixin, RetrieveModelMixin):
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
    queryset = ContactModel.objects.all()
    serializer_class = ContactReadSerializer
    lookup_field = ['id', 'pk']
    
    def perform_destroy(self, instance):
        instance.delete()