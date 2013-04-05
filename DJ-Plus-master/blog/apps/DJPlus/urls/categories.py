from django.conf.urls import *
from DJPlus.models import Category

urlpatterns = patterns('',
    url(r'^$','django.views.generic.list_detail.object_list',{ 'queryset' : Category.objects.all() },'DJPlus_category_list'),
    url(r'^(?P<slug>[-\w]+)/$','DJPlus.views.category_detail',name='DJPlus_Category_detail'),
)
