from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

     url(r'^grappelli/', include('grappelli.urls')),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^blog/categories/', include('DJPlus.urls.categories')),
	 url(r'^blog/links/', include('DJPlus.urls.links')),
	 url(r'^blog/tags/', include('DJPlus.urls.tags')),
	 url(r'^blog/', include('DJPlus.urls.entries')),
	 url(r'^media/(?P<path>.*)$','django.views.static.serve',{ 'document_root': settings.MEDIA_ROOT }),
)
