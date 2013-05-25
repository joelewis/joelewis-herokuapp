import json
import sqlite3
import datetime
import markdown
import urllib2
import re

j = json.load(urllib2.urlopen('https://api.github.com/users/joelewis/gists'))

def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1)

conn = sqlite3.connect('/home/joe/Documents/workstage/joelewis/blog.db')
c = conn.cursor()
postid = int(urllib2.urlopen('http://joelewis.herokuapp.com/getpid').read())

postid = postid+5

i=j[0]
title = convert(i['files'].keys()[0]).split('.')[0]
extension = convert(i['files'].keys()[0]).split('.').pop()
excerpt = ""
global body
body = ""
if extension == 'md':
	
	body =  urllib2.urlopen(i['files'].values()[0]['raw_url']).read()
else:
		
	body = "<a href='" + i['html_url'] + "'>" + i['html_url'] + "</a>"
md = markdown.Markdown()
body_html = md.convert(body)
pub_date = i['created_at'].replace("T"," ").replace("Z","")
slug = i['files'].keys()[0].split('.')[0]
author_id = 1
enable_comments = 1
featured = 0
status = 1
if i['public'] == True :
	status = 1
else:
	status = 2
tags = ""
excerpt_html = ""
c.execute("INSERT INTO djplus_entry values (?,?,?,?,?,?,?,?,?,?,?,?,?)",(postid,title,excerpt,body,pub_date,slug,author_id,enable_comments,featured,status,tags,excerpt_html,body_html))
conn.commit()
