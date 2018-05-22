from django.shortcuts import render
from .models import Post
def post_list(request):
    return render(request, 'blog/post_list.html', {})

 def alex_site(request):
 	return render(request, 'blog/Alexhome.html', {})
# Create your views here.
