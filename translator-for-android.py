#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:13:38 2019

@author: anony
"""

from bs4 import BeautifulSoup
from googletrans import Translator
import sys

input_file = sys.argv[1]
lang = sys.argv[2]
out_file = sys.argv[3]

#input_file = 'strings.xml'
#lang = 'fr'
#out_file = 'strings-fr.xml'

file = open(input_file,'r')

bs = BeautifulSoup(file)

translator = Translator()

names = []
texts = []
translations = []

for text in bs.find_all('string',attrs={'translatable':None}):
    if text.string is None or text.attrs['name'] is None:
        continue
    
    names.append(text.attrs['name'])
    texts.append(text.string)

translations = translator.translate(texts,dest=lang)

out = BeautifulSoup()

for i in range(len(names)):
    t = out.new_tag('string',attrs={'name':names[i]})
    t.string = translations[i].text
    out.append(t)
f = open(out_file, "w")
f.write(out.prettify())
f.close()

#print(translations)
    


