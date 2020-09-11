# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:48:16 2020

@author: SE
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:54:20 2020

@author: syful
"""

import re
import pandas as pd
import numpy as np
from collections import Counter
import statistics


df1=pd.read_csv("F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/LDA/01_NS_posts.csv",low_memory=False )

df2=pd.read_csv("F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/LDA/01_NS_posts.csv",low_memory=False)

#"""
Topic=[]
number_per_topic=[]
score_=[]
view_=[]
FavCount_=[]
AnsCount_=[]
AccpAnsCount_=[]
CommentCount_=[]



for i in range(0, 8):
    Topic.append(i)
    score_0=[]
    view_0=[]
    FavCount_0=[]
    AnsCount_0=[]
    AccpAnsCount_0=[]
    CommentCount_0=[]
    number=0
    for index, j in enumerate(df1['Dominant_Topic']):
        if j==i:
            number=number+1
            if df2['AcceptedAnswerId'][index]>0:
                AccpAnsCount_0.append(1)
            score_0.append(df2['Score'][index])
            view_0.append(df2['ViewCount'][index])
            FavCount_0.append(df2['FavoriteCount'][index])
            AnsCount_0.append(df2['AnswerCount'][index])
            CommentCount_0.append(df2['CommentCount'][index])
    
    number_per_topic.append(number)
    score_.append(statistics.median(score_0))
    view_.append(statistics.median(view_0))
    FavCount_.append(statistics.median(FavCount_0))
    AnsCount_.append(statistics.median(AnsCount_0))
    AccpAnsCount_.append(sum(AccpAnsCount_0)/len(score_0))
    CommentCount_.append(statistics.median(CommentCount_0))
    
dict = {'Topic': Topic, 'number_per_topic':number_per_topic, 'score_avg':score_, 'view_avg':view_, 'FavCount_avg':FavCount_, 'AnsCount_avg':AnsCount_, 'AccpAnsCount_avg':AccpAnsCount_, 'CommentCount_avg':CommentCount_}  
df3 = pd.DataFrame(dict) 
df3.to_csv('F:/1_NAIST_Research_SE/SE_meeting/Network-simulators/LDA/01_NS_posts_statistics.csv', header=True, index=False)


#"""