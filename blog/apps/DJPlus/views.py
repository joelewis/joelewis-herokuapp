from django.shortcuts import render_to_response
from DJPlus.models import *
import datetime, time
from django.views.generic.list_detail import object_list
#from tagging.views import tagged_object_list
from django.views.generic.dates import YearArchiveView
#from tagging.models import TaggedItem
def entries_index(request):
	return render_to_response('entry_index.html',{ 'entry_list': Entry.objects.filter(status==LIVE_STATUS) })
def entry_detail(request, year, month, day, slug):
	date_stamp = time.strptime(year+month+day, "%Y%b%d")
	pub_date = datetime.date(*date_stamp[:3])
	return render_to_response('entry_detail.html',
								{ 'entry': Entry.objects.get(pub_date__year=pub_date.year,
									pub_date__month=pub_date.month,
									pub_date__day=pub_date.day,
									slug=slug) })



def category_list(request):
	return render_to_response('category_list.html',{'object_list':Category.objects.all() })

def category_detail(request, slug):
	try:
		category = Category.objects.get(slug=slug)
	except Category.DoesNotExist:
		raise Http404
	return object_list(request, queryset=category.entry_set.all(), extra_context={"month_list" : Entry.objects.filter().dates('pub_date','month'),"category_list": Category.objects.all(), "ct":category})

#def tag_detail(request, tag):
#	return tagged_object_list(request, queryset_or_model=Entry.objects.all(), tag=tag, extra_context={"month_list" : Entry.objects.filter().dates('pub_date','month'),"category_list": Category.objects.all(), },template_name="DJPlus/tag_list.html")
		
def get_postid(request):
	return HttpResponse(len(Entry.objects.all()))
														
class EntryByYearView(YearArchiveView):
    template_name = "DJPlus/archive_year.html"
    queryset = Entry.objects.all()
    date_field = 'pub_date'
    context_object_name = 'object_list'	
    make_object_list = True													
