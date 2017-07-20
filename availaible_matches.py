"""imports a json and returns the availaible matches and id as a dictionary
in cricbuzz"""
import json 
import urllib
from bs4 import BeautifulSoup
import re
def get_ids():
    service_url='http://www.cricbuzz.com/api/html/homepage-scag'
    fhand=urllib.request.urlopen(service_url).read()
    strin=fhand.decode()
    soup=BeautifulSoup(strin,'html.parser')
    anchors=soup('a')
    mydict={}
    for i in anchors:
        l=i.get('href',None)
        try:
            keys1=l.split('/')[3]
            vals1=int(l.split('/')[2])
            mydict[keys1]=vals1
        except:
            continue
    if(len(mydict)==0):
        print("......ID ERROR ..... or .....AVAILAIBLE MATCHES=0.....")
        quit(0)
    return mydict
print(get_ids())