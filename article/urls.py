from django.conf.urls import url
from .views import article_list,article_publish

urlpatterns = [
	url(r'^list/(?P<block_id>\d+)',article_list),
	url(r'^publish/(?P<block_id>\d+)',article_publish),
]