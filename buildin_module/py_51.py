#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from xml.parsers.expat import ParserCreate


# build-in: xml_parser -- SAX
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def character_data(self, text):
        if text.strip() != '':
            print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

if __name__ == '__main__':
    sax_handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = sax_handler.start_element
    parser.EndElementHandler = sax_handler.end_element
    parser.CharacterDataHandler = sax_handler.character_data
    parser.Parse(xml)
