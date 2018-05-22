from django.shortcuts import render
from .models import Post
def post_list(request):
    return render(request, 'blog/post_list.html', {})

 def alex_site(request):
 	return render(request, 'blog/Alexhome.html', {})
 url(r'^alex_site/$', views.alex_site, name="Alex's Site"),
# Create your views here.
