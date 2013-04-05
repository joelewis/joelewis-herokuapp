from django.db import models
from django.contrib.auth.models import User
#from tagging.fields import TagField
#from tagging.models import Tag
import markdown 
import datetime

# Data model for the category
class Category(models.Model):
	title = models.CharField(max_length=250, help_text='Keep within 250 Chars')
	slug = models.SlugField(unique=True)
	description = models.TextField()
	
	class Meta:
		verbose_name_plural = "Categories"
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return ('DJPlus_category_detail', ('slug'), {'slug':self.slug})
	get_absolute_url = models.permalink(get_absolute_url)

# Data model for posts
class Entry(models.Model):
	title = models.CharField(max_length=250, help_text='Keep within 250 Chars')
	excerpt = models.TextField(blank=True)
	body = models.TextField()
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(unique_for_date='pub_date')
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	LIVE_STATUS=1
	DRAFT_STATUS=2
	STATUS_CHOICES = (
	(1, 'Live'),
	(2, 'Draft'),
	)
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	categories = models.ManyToManyField(Category)
	#tags = TagField()
	excerpt_html = models.TextField(editable=False, blank=True)
	body_html = models.TextField(editable=False, blank=True)
	class Meta:
		ordering = ['-pub_date']
	def save(self,force_insert=False,force_update=False):
		md = markdown.Markdown()
		self.body_html = md.convert(self.body)
		if self.excerpt:
			self.excerpt_html = md.convert(self.excerpt)
		super(Entry, self).save(force_insert, force_update)
    
	#def get_tags(self):
	#	return Tag.objects.get_for_object(self)

	class Meta:
		verbose_name_plural = "Posts"
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return ('DJPlus_entry_detail', (), {'year':self.pub_date.strftime('%Y'), 
										   'month':self.pub_date.strftime('%b').lower(),
										    'day':self.pub_date.strftime('%d'),
										    'slug':self.slug })
	get_absolute_url = models.permalink(get_absolute_url)
	
	def get_root_url(self):
		return ('DJPlus_entry_archive_year', (), {})
	get_root_url = models.permalink(get_root_url)
	
	
#Data Model for Links
class Link(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	description_html = models.TextField(editable=False, blank=True)
	url = models.URLField(unique=True)
	posted_by = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(unique_for_date='pub_date')
	enable_comments = models.BooleanField(default=True)
	post_elsewhere = models.BooleanField('Post to Delicious', default=True)
	via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person who gave you this')
	via_url = models.URLField('Via URL', blank = True, help_text = 'The url of the site of the link')
	
	class Meta:
		ordering = ['-pub_date']
	def __unicode__(self):
		return self.title
		
	def save(self):
		if self.description:
			md = markdown.Markdown()
			self.description_html = md.convert(self.description)
		super(Link, self).save()
	def get_absolute_url(self):
		return ('DJPlus_link_detail',(),{'year':self.pub_date.strftime('%Y'), 
										   'month':self.pub_date.strftime('%b').lower(),
										    'day':self.pub_date.strftime('%d'),
										    'slug':self.slug })
	get_absolute_url = models.permalink(get_absolute_url)
	def get_root_url(self):
		return ('DJPlus_root_url', (), {})
	get_root_url = models.permalink(get_root_url)	
