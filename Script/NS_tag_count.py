# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 15:53:15 2020

@author: syful
"""

import xml.etree.ElementTree as et
import re
import pandas as pd
from datetime import datetime
start = datetime.now()
from tqdm.auto import tqdm
import numpy as np
import collections

Id=[]
CreationDate=[]
Score=[]
ViewCount=[]
Title=[]
Body=[]
Tags=[]



Tag_list=[]

df2 = pd.read_csv("F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/01_NS_posts_initial_simulator_tag.csv")


for element in df2['Tags']:
    res = re.findall(r'\<(.*?)\>', element)
    
    for tag_element in res:
        Tag_list.append(tag_element)

tag=[]
count=[]
final_tag=collections.Counter(Tag_list)
for i in final_tag : 
    tag.append(i)
    count.append(final_tag[i]) 
    
dict={'tag':tag, 'count':count}
df1=pd.DataFrame(dict)

df1.to_csv("F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/tag_count.csv")

"""
Filter_list=[]

for element in Final_Tags:
    if "update" in element:
        Filter_list.append(element)
    elif "library" in element:
        Filter_list.append(element)
    elif "dependen" in element:
        Filter_list.append(element)
    elif "semantic" in element:
        Filter_list.append(element)
    elif "third-party" in element:
        Filter_list.append(element)
    elif "Break" in element:
        Filter_list.append(element)
    elif "compatibility" in element:
        Filter_list.append(element)
    elif "incompatibility" in element:
        Filter_list.append(element)
    elif "migration" in element:
        Filter_list.append(element)
    elif "Go" in element:
        Filter_list.append(element)
    elif "NuGet" in element:
        Filter_list.append(element)
    elif "Cocoa" in element:
        Filter_list.append(element)
    elif "clojar" in element:
        Filter_list.append(element)
    elif "atom" in element:
        Filter_list.append(element)
    elif "puppet" in element:
        Filter_list.append(element)
    elif "cathage" in element:
        Filter_list.append(element)
    elif "conda" in element:
        Filter_list.append(element)
    elif "Nimble" in element:
        Filter_list.append(element)
    elif "Inqlude" in element:
        Filter_list.append(element)
    elif "npm" in element:
        Filter_list.append(element)
    elif "maven" in element:
        Filter_list.append(element)
    elif "wordpress" in element:
        Filter_list.append(element)
    elif "cran" in element:
        Filter_list.append(element)
    elif "pub" in element:
        Filter_list.append(element)
    elif "Emacs" in element:
        Filter_list.append(element)
    elif "julia" in element:
        Filter_list.append(element)
    elif "racket" in element:
        Filter_list.append(element)
    elif "jam" in element:
        Filter_list.append(element)
    elif "shards" in element:
        Filter_list.append(element)
    elif "rubygems" in element:
        Filter_list.append(element)
    elif "cpan" in element:
        Filter_list.append(element)
    elif "hackage" in element:
        Filter_list.append(element)
    elif "hex" in element:
        Filter_list.append(element)
    elif "homebrew" in element:
        Filter_list.append(element)
    elif "sublime" in element:
        Filter_list.append(element)
    elif "elm" in element:
        Filter_list.append(element)
    elif "alcatraz" in element:
        Filter_list.append(element)
    elif "pypi" in element:
        Filter_list.append(element)
    elif "bower" in element:
        Filter_list.append(element)
    elif "cargo" in element:
        Filter_list.append(element)
    elif "meter" in element:
        Filter_list.append(element)
    elif "platformio" in element:
        Filter_list.append(element)
    elif "swiftpm" in element:
        Filter_list.append(element)
    elif "dub" in element:
        Filter_list.append(element)
    elif "haxelib" in element:
        Filter_list.append(element)
    elif "purescript" in element:
        Filter_list.append(element)
   
    
        
print("-------------------------------------\n")
        
print("Total number of tags:%s"%len(Final_Tags))

df = pd.DataFrame(Final_Tags) 
df.to_csv('C:/Users/syful/Documents/stackoverflow/3_Tag_list.csv', header=True, index=False, encoding='utf-8') 

"""