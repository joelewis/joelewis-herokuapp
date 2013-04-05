from django.contrib import admin
from DJPlus.models import *

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':['title']}
	ordering = ['title']
	

class EntryAdmin(admin.ModelAdmin):
		prepopulated_fields = { 'slug': ['title'] }
		ordering = ['-pub_date']
	
class LinkAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':['title']}
	ordering = ['-pub_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Link, LinkAdmin)
