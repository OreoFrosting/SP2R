from django.shortcuts import render
from .models import Post
def landing_page(request):
    return render(request, 'lp/landing_page.html', {})

# Create your views here.
#def alex_site(request):
#	return render(request, 'blog/Alexsite.html', {})