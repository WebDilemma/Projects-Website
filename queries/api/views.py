from rest_framework import generics

from queries.models import ContactModel


class ContactCreateView(generics.CreateAPIView):
    pass

class ContactListView(generics.createAPIView):
    pass

class ContactRetrieveView(generics.RetrieveView):
    pass