from rest_framework import serializers

from team.models import OurTeam

class TeamSerializer(serializers.ModelSerializer):
    url  = serializers.SerializerMethodField(read_only=True)
    slug = serializers.SerializerMethodField(read_only=True)
    class Meta():
        model = OurTeam
        fields = [
            'url',
            'pk',
            'user',
            'slug'     
        ]
        read_only_field = [ 'pk', 'user', ]
        
    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request) 
    
    def get_slug(self, obj):
        slug = self.user.slug
        return slug   
    
    def validate_github(self, value):
        qs = OurTeam.objects.filter(user__github__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("link must be potani hovi joie")
    