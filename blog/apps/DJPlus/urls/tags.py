from django.conf.urls import *
from tagging.models import Tag
from DJPlus.models import Entry, Link

urlpatterns = patterns('',
	url(r'^$','django.views.generic.list_detail.object_list', { 'queryset':Tag.objects.all() },'DJPlus_tag_list'),
	url(r'^entries/(?P<tag>[-\w]+)/$', 'DJPlus.views.tag_detail', name='DJPlus_tag_detail'),
	url(r'^links/(?P<tag>[-\w]+)/$', 'tagging.views.tagged_object_list.', {'queryset_or_model':Link, 'template_name':'links_by_tag.html'}),
)
