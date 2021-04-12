from rest_framework import serializers

from projects.models import Project

from portfolio.api.serializers import ProfileSerializer

class ProjectSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    author = ProfileSerializer(many=True)
    class Meta():
        model = Project
        fields = [
            'url',
            'title',
            'img',
            'author',
            'text',
            'like',
            'categorie',
            'link',
            'tools',
        ]
        read_only_field = [ 'pk', 'user' ]
        depth = 1
    
    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)
    