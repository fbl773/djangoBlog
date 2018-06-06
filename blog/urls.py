from django.urls import path,re_path
from . import views

urlpatterns = [
	re_path(r'^post/(?P<pk>\d+)/$',views.entry_detail,name='entry_detail'),
	path('',views.post_list,name='post_list'),
]
