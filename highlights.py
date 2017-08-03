# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:07:01 2017

@author: Yatish H R
"""
# -*- coding: utf-8 -*-
import json
import urllib
import re
import time
#from availaible_matches import *
mtchid=18459
def highlights1(mtchid):
    url="http://www.cricbuzz.com/match-api/"+str(mtchid)+"/highlights.json"
    jhand=urllib.request.urlopen(url).read()
    data=json.loads(jhand.decode())
    cmntry=[]
    for i in data['comm_lines'] :
        try:
            cmntry.append(i['o_no']+' '+i['comm'])
    #            print(i['o_no'],i['comm'])
    #            print('\n')
        except: 
            try:
                cmntry.append('blank '+i['comm'])
    #                print(i['comm'])
            except:
                continue
    #        print(i.keys())
    #    print(cmntry)
    
    
    def filtery(List):
        newlist=[]
        for items in List:
            if '<div' in items:
                continue
            newlist.append(re.sub('\\\'','',re.sub('<.*?>', '', items)))
        return newlist
    
    newlist1=filtery(cmntry)
    newlist1.reverse()
    return newlist1
    
def displaycmntry(newlist1):
    for item in newlist1:
        try:
            splitem=item.split()
            ind=item.index(' ')
            print(float(splitem[0]),' ',item[ind+1:],'\n')
    
        except:
            ind=item.index(' ')
            print(item[ind+1:])
            print('\n')
    
    
    

def highlights(mtchid):
    old=[]
    while True:
        new=highlights1(mtchid)
        if new!=old :
            displaycmntry(new)
            old=new
        time.sleep(40)
    
    
    


