from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostsSerializer
from .models import Posts
import requests

from requests import request


# Create your views here.

class PostViewerSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('regions')
    serializer_class = PostsSerializer
    
def home(request):
    response = requests.get('http://127.0.0.1:8000/posts/')
    data = response.json()
    return render(request, 'home.html', {'data':data})
    