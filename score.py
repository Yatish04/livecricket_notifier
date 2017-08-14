import json
import urllib
players={}

def score1(mtchid):
    url="http://www.cricbuzz.com/match-api/"+str(mtchid)+"/commentary.json"
    jhand=urllib.request.urlopen(url).read()
    data=json.loads(jhand.decode())
    listofplayers=data['players']
    
    
    """players list"""
    
    for i in listofplayers:
        players[int(i['id'])]=i['f_name']
    #print(data['score'])
    
    """some useful data"""
    crr=data['score']['crr']
    previous_overs=data['score']['prev_overs']
    lstwicket=players[int(data['score']['last_wkt'])]
    partnership=data['score']['prtshp']
    
    """batsmen stats in this game"""
    """================================================================================================================"""
    class batsmen(object):
        """ note all are strings"""
        def __init__(self,name,balls,runs,fours,sixs):
            self.name=name
            self.balls=balls
            self.runs=runs
            self.fours=fours
            self.sixs=sixs
        def getscore(self,status=None):
            if status==None :
                print(self.name,self.runs+'('+self.balls+')','4s :'+self.fours,'6s :'+self.sixs)
            else:
                print(self.name+"*",self.runs+'('+self.balls+')','4s :'+self.fours,'6s :'+self.sixs)
    
    
    try:
        balls1=data['score']['batsman'][0]['b']
        name1=players[int(data['score']['batsman'][0]['id'])]
        fours1=data['score']['batsman'][0]['4s']
        sixs1=data['score']['batsman'][0]['6s']
        runs1=data['score']['batsman'][0]['r']
        strikebatsman=batsmen(name1,balls1,runs1,fours1,sixs1)
    except:
        pass
    
    try:
        name2=players[int(data['score']['batsman'][1]['id'])]
        fours2=data['score']['batsman'][1]['4s']
        sixs2=data['score']['batsman'][1]['6s']
        runs2=data['score']['batsman'][1]['r']
        balls2=data['score']['batsman'][1]['b']
        nonstrikebatsman=batsmen(name2,balls2,runs2,fours2,sixs2)
    except:
        pass
    """======================================================================================================"""
    """bowler stats in this game"""
    
    class bowler(object):
        """ note all are strings"""
        def __init__(self,name,overs,runs,maidens,wickets):
            self.name=name
            self.overs=overs
            self.runs=runs
            self.maidens=maidens
            self.wickets=wickets
        def getstatus(self,status=None):
            if status == None:
                print(self.name,self.runs+'('+self.overs+')','maidens :'+self.maidens,'wickets :'+self.wickets)
    
    
    
    overs1=data['score']['bowler'][0]['o']
    name1=players[int(data['score']['bowler'][0]['id'])]
    m1=data['score']['bowler'][0]['m']
    wickets1=data['score']['bowler'][0]['w']
    runs1=data['score']['bowler'][0]['r']
    
    strikebowler=bowler(name1,overs1,runs1,m1,wickets1)
    
    team1name=data['team1']['name']
    team1id=data['team1']['id']
    team1shrt=data['team1']['s_name']
    
    
    team2name=data['team2']['name']
    team2id=data['team2']['id']
    team2shrt=data['team2']['s_name']
    
    teamlist={}
    teamlist[team1id]=team1name+'('+team1shrt+')'
    teamlist[team2id]=team2name+'('+team2shrt+')'
    """============================================================================================================="""
    """team items"""
    class team(object):
        def __init__(self,name,score,innings):
            self.name=name
            self.score=score
            if innings=='1':
                self.innings='first'
            elif innings=='2' :
                self.innings='second'
            elif innings=='yet to bat' :
                self.innings=innings
            else:
                raise ValueError('bad thing happened')
                quit()
        def getscore(self):
            if self.innings=='yet to bat' :
                print(self.name,'yet to bat')
            else:
                print(self.name,self.innings,'innings','\n','score',self.score)
        def getbowlingteamscr(self):
            try:
                print(self.name,self.score)
            except:
                raise ValueError('no such thing')
        def __str__(self):
            return self.name
    
    battingteamid=data['score']['batting']['id']
    
    if team1id==battingteamid:
        bowlingteamid=team2id
    else:
        bowlingteamid=team1id
    
        
    battingteam=teamlist[data['score']['batting']['id']]
    battingteamscr=data['score']['batting']['score']
    battingteamin=str(len(data['score']['batting']['innings']))
    
    bowlingteam=teamlist[bowlingteamid]
    try:
        bowlingteamscr=data['score']['bowling']['score']
        bowlingteamin=str(len(data['score']['bowling']['innings']))
    except:
        bowlingteamscr='yet to bat'
        bowlingteamin='yet to bat'
        print(bowlingteam,'yet to bat')
        pass
    
    battingteams=team(battingteam,battingteamscr,battingteamin)
    bowlingteams=team(bowlingteam,bowlingteamscr,bowlingteamin)
    
    try:
        target=data['score']['target']
    except:
        target=''
    """display section begins"""
    print('==========batsmen info =================')
    strikebatsman.getscore()
    try:
        nonstrikebatsman.getscore()
    except:
        pass
    print('==========bowler info====================')
    strikebowler.getstatus()
    print('========================team info===================')
    battingteams.getscore()
    bowlingteams.getscore()
    print('')
    print('=========================================================')
    print('previous overs:',previous_overs)
    print('lastwicket :',lstwicket)
    print('partnership :',partnership)
    print('crr :',crr)
    if target!='' :
        print('target :',target)




















