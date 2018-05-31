from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing_page, name='landing_page'),
    url(r'alexsite/$', views.alexsite, name='alexsite'),
    url(r'alexscope/$', views.alexscope, name='alexscope'),
    url(r'brycesite/$', views.brycesite, name='brycesite'),
    url(r'nick_index/$', views.nick_index, name='nick_index'),
    url(r'fortnite_home/$', views.fortnite_home, name='fortnite_home')
    url(r'fortnite_home/fortnite_skins/$', views.fortnite_skins, name='fortnite_skins')
]