from django.conf.urls import *
from DJPlus.models import Link,Entry,Category
from tagging.models import Tag
link_info_dict = {
	'queryset': Link.objects.all(),
	'date_field': 'pub_date',
	'extra_context' : {"month_list" : Entry.objects.filter().dates('pub_date','month'),
					   "category_list" : Category.objects.all(),
					   "tag_list" : Tag.objects.all()}
			       	  }

urlpatterns = patterns('',
	url(r'^$', 'django.views.generic.date_based.archive_index',link_info_dict,'DJPlus_link_archive_index'),
	url(r'^(?P<year>\d{4})/$','django.views.generic.date_based.archive_year',link_info_dict,'DJPlus_link_archive_year'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$','django.views.generic.date_based.archive_month',link_info_dict,'DJPlus_link_archive_month'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$','django.views.generic.date_based.archive_day',link_info_dict,'DJPlus_link_archive_day'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$','django.views.generic.date_based.object_detail',link_info_dict,'DJPlus_link_detail'),
	)
