from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'$', views.alexsite, name='alexsite'),
    url(r'$', views.alexscope, name='alexscope'),
]