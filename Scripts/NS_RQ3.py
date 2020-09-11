# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 02:50:50 2020

@author: SE
"""

import pandas as pd
topic=[]
how=[]
what=[]
why=[]
others=[]

df1=pd.read_csv("F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/LDA/01_NS_posts.csv")

for i in range(0, 8):
    ho=0
    wha=0
    wh=0
    ot=0
    for j in range(0, len(df1)):
        if df1['Dominant_Topic'][j]==i:
            if "how" in df1['Title'][j] or "how" in df1['Body'][j] or "is there a way" in df1['Title'][j] or "is there a way" in df1['Body'][j] or "error" in df1['Title'][j] or "error" in df1['Body'][j] :
                ho=ho+1
            elif "what" in df1['Title'][j] or "what" in df1['Body'][j] or "should" in df1['Title'][j] or "should" in df1['Body'][j]:
                wha=wha+1
            elif "why" in df1['Title'][j] or "why" in df1['Body'][j]:
                wh=wh+1
            else:
                ot=ot+1
    topic.append(i)
    how.append(ho)
    what.append(wha)
    why.append(wh)
    others.append(ot)

dict={'Topic':topic, 'how':how, 'what':what, 'why':why, 'others':others}
df2=pd.DataFrame(dict)

df2.to_csv("F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/LDA/Questions.csv")
        
                
                
    