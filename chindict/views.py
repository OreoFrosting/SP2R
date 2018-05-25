from django.shortcuts import render
def landing_page(request):
    return render(request, 'chindict/landing_page.html', {})
def alexsite(request):
	return render(request, 'chindict/alexsite.html', {})
def alexscope(request):
	return render(request, 'chindict/alexscope.html', {})
# Create your views here.
def brycesite(request):
	return render(request, 'chindict/brycesite.html', {})
def nick_index(request):
	return render(request, 'chindict/nick_index.html', {})	