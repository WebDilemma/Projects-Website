from rest_framework import serializers

from queries.models import ContactModel

class ContactSerializer(serializers.ModelSerializer):
    class Meta():
        model = ContactModel
        fields = [
            'id',
            'email',
            'title',
            'text',
        ]
        read_only_fields = ['email']
    