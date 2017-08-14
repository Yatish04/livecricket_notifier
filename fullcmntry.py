# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import urllib
import re
import time
import score
f=1
thisover={}
old=[]
def infinite(mtchid):
    global f
    global old
    url="http://www.cricbuzz.com/match-api/"+str(mtchid)+"/commentary.json"
    jhand=urllib.request.urlopen(url).read()
    data=json.loads(jhand.decode())
    cmntry=[]

    def previous_over(ono,det):
        
#        print(det.split('|'),'{{{{{{{')
        det1=det.split('|')
        try:
            print(ono,det1[-1])
            thisover[ono]=det1[-1]
        except:
            thisover[ono]=''
            pass
        try:
            thisover[ono-1]=det1[-2]
        except:
            thisover[ono]=''
            pass

        try:
            thisover[ono-2]=det1[-3]
        except:
            thisover[ono]=''
            pass
#        print(thisover)
    for i in data['comm_lines'] :
        try:
            cmntry.append(i['o_no']+' '+i['comm'])
        except:
            try:
                cmntry.append('blank '+i['comm'])
            except:
                continue
    
    
    def filtery(List):
        newlist=[]
        for items in List:
            if '<div' in items:
                continue
            newlist.append(re.sub('\\\'','',re.sub('<.*?>', '', items)))
        return newlist
    
    newlist1=filtery(cmntry)
    newlist1.reverse()
    
    def displaycmntry(newlist1):
        for item in newlist1:
            try:
                splitem=item.split()
                ind=item.index(' ')
                itm=splitem[0]
                print(float(splitem[0]),' ',item[ind+1:],'\n')
                if itm[-1]=='6' :
                    score.score1(mtchid)
                    try:
                        print('     ','This Over',thisover[round(float(itm))])
                        print('=================================================================================================')
                    except:
                        print(' ssvfsdv')
                        previous_over(round(float(data['score']['batting']['innings'][-1]['overs'])),data['score']['prev_overs'])
                        print('     ','This Over -',thisover[round(float(itm))])
                        print('=================================================================================================')
    
            except:
                ind=item.index(' ')
                print(item[ind+1:])
                print('\n')
    if cmntry!=old:
        old=cmntry
        displaycmntry(newlist1)
    time.sleep(24)

def fllcmntry(mtchid) :   
    while True:
        infinite(mtchid)
