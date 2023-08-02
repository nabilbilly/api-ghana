from rest_framework import serializers
from .models import Posts

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('regions', 'districts')

# meta is to tell the system/erializers about our module/ data






