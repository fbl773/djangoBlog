from django.urls import path,re_path
from . import views

urlpatterns = [
	re_path(r'^entry/(?P<pk>\d+)/$',views.entry_detail,name='entry_detail'),
	re_path(r'^entry/new/$', views.entry_new, name="entry_new"),
	path('',views.entry_list,name='entry_list'),
]
