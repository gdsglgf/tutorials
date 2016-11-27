# -*- coding: utf-8 -*-
import chardet
import re

from bs4 import BeautifulSoup

def show(value):
	print(value, type(value))

html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
	<title>Document</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta name="keywords" content="dummy keywords" />
	<meta name="description" content="dummy description" />
</head>
<body>
	
</body>
</html>
'''

print(chardet.detect(html_doc))
# {'confidence': 1.0, 'encoding': 'ascii'}

# soup = BeautifulSoup(open("index.html"))
# soup = BeautifulSoup(markup, from_encoding="utf-8")
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.original_encoding)
# utf-8


title = soup.title
show(title)
# <title>Document</title>, <class 'bs4.element.Tag'>

show(title.name)
# u'title', <type 'unicode'>

show(title.string)
# u'Document', <class 'bs4.element.NavigableString'>

show(title.get_text())
# u'Document', <type 'unicode'>

show(title.text)
# u'Document', <type 'unicode'>

print('--------------')
# show(soup.docno.text)

# 
meta = soup.find('meta')
show(meta.attrs)
# {u'content': u'text/html; charset=utf-8', u'http-equiv': u'Content-Type'}, <type 'dict'>

show(meta['content'])
# u'text/html; charset=utf-8', <class 'bs4.element.ContentMetaAttributeValue'>

show(meta.get('content'))
# u'text/html; charset=utf-8', <class 'bs4.element.ContentMetaAttributeValue'>



keywords = soup.find('meta', attrs={'name': re.compile('keywords',re.IGNORECASE)})['content']
show(keywords)