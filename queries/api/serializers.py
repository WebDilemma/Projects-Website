from rest_framework import serializers

from queries.models import ContactModel

class ContactReadSerializer(serializers.ModelSerializer):
    class Meta():
        model = ContactModel
        fields = [
            'id',
            'email',
            'title',
            'text',
        ]
        read_only_fields = ['email']
        
class ContactCreateSerializer(serializers.Serializer):
    email = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    class Meta():
        fields = [
            'email',
            'title',
            'text',
        ]

    