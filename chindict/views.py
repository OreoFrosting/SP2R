from django.shortcuts import render
def landing_page(request):
    return render(request, 'chindict/landing_page.html', {})
def alexsite(request):
	return render(request, 'chindict/alexsite.html', {})
# Create your views here.
