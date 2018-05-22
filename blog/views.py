from django.shortcuts import render
from .models import Post
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# Create your views here.
def alex_site(request):
 	return render(request, 'blog/Alexsite.html', {})