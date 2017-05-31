#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Python提供了HTMLParser来非常方便地解析HTML
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)
    def handle_endtag(self, tag,):
        print('</%s>' % tag)
    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)
    def handle_data(self, data):
        print('data')
    def handle_comment(self, name):
        print('<!-- -->')
    def handle_entityref(self, name):
        print('&%s;' % name)
    def handle_chareff(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>') 
