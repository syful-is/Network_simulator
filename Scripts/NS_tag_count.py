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

