from bs4 import BeautifulSoup
import sqlite3

import markdown 
import datetime

file= open("myxml.xml","r")
data = file.read()

soup = BeautifulSoup(data)

itemlist = soup.findAll('item')

conn = sqlite3.connect('blog.db')
c = conn.cursor()
postid=3
for item in itemlist:
    postid = postid+1  
    title = item.find('title').text
    excerpt = ""
    body = item.find('content:encoded').text
    md = markdown.Markdown()
    body_html = md.convert(body)
    pub_date = item.find('wp:post_date').text  
    slug = item.find('wp:post_name').text  
    author_id = 1
    enable_comments = 1
    featured = 0
    status = 1
    if item.find('wp:status').text=='publish' :
	  status = 1
    else:
	  status = 2
    tags = ""
    excerpt_html = ""
    c.execute("INSERT INTO djplus_entry values (?,?,?,?,?,?,?,?,?,?,?,?,?)",(postid,title,excerpt,body,pub_date,slug,author_id,enable_comments,featured,status,tags,excerpt_html,body_html))
    conn.commit()
  
	
	
	
		
    
    
    

