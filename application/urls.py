from django.conf.urls import url
from . import views

app_name = 'application'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^home/$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^last_search/$', views.last_search, name='last_search'),
    url(r'^manage_recruitments/$', views.manage_recruitments, name='manage_recruitments'),
    url(r'^search_result/$', views.search_result, name='search_result'),

]
