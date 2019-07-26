from tkinter import *
import character, scene,arrow, gametimer
import random

newchartime=20 #30초에 새로운 캐릭터 등장 
chance1=30 #아이템 1의 1/50 확률로 아이템2 등장
chance2=50 #아이템 2의 1/50 확률로 아이템2 등장 
winH=700
winW=1000

window=Tk()
window.title("정호의 니편내편")
sec=60
itemsec=3
my_scene=scene.Scene(window,color="green",width=winW,height=winH)
my_arrow=arrow.Arrow(my_scene,x_start=winW//2,y_start=winH-100)
my_characters=[]
my_items=[]
my_itemlook=[]
middleID=[]
randIDs=random.sample(range(1,5),4)
for i in range(7):
    itemchance1=random.randint(1,chance1)
    itemchance2=random.randint(1,chance2)
    randID=random.randint(0,1)
    getID=randIDs[randID]
    if itemchance1==7:
        middleID.append(5)
        my_characters.append(character.Character(scene=my_scene,charID=5,size=20, x_start=winW//2,y_start=winH-(100+i*80)))
    elif itemchance2==7:
        middleID.append(6)
        my_characters.append(character.Character(scene=my_scene,charID=6,size=20, x_start=winW//2,y_start=winH-(100+i*80)))
    else:
        middleID.append(getID)
        my_characters.append(character.Character(scene=my_scene,charID=getID,size=20, x_start=winW//2,y_start=winH-(100+i*80)))



left_chararcter=character.Character(scene=my_scene,charID=randIDs[0],size=40, x_start=200,y_start=winH//2)
right_chararcter=character.Character(scene=my_scene,charID=randIDs[1],size=40, x_start=800,y_start=winH//2)

my_scene.draw_timer()
my_timers=[]
for i in range(sec):
    my_timers.append(gametimer.Gametimer(scene=my_scene,index=i))

score = 0
combo = 0
realtime=0 #실제 흘러가는 시간 
def realtimeflow():
    global realtime
    realtime+=1
    #print("r=",realtime)
    if realtime==newchartime:
        left_chararcter2=character.Character(scene=my_scene,charID=randIDs[2],size=40, x_start=200,y_start=winH//2-100)
        right_chararcter2=character.Character(scene=my_scene,charID=randIDs[3],size=40, x_start=800,y_start=winH//2-100)
    if nowtimer!=0:
        window.after(1000,realtimeflow)

def timerflow():
    global nowtimer #아래의 남은 타이머 시간 
    nowtimer=int(len(my_timers))-1
    
    #print(nowtimer)
    my_timers[nowtimer].remove()
    my_timers.pop(nowtimer)
    if nowtimer!=0:
        window.after(1000,timerflow)
    elif nowtimer==0:
        my_scene.draw_gameover()
        my_scene.draw_totalscore(score)
def timergetnum():
    gettimenum=int(len(my_timers))
    #print(gettimenum)
    
    if gettimenum!=0:
        my_scene.draw_timernumber(gettimenum)
        window.after(50,timergetnum)

def button_clear():
    LC=my_arrow.getleftcolor()
    RC=my_arrow.getrightcolor()
    if LC=="magenta":
        my_arrow.initleftbutton()
    if RC=="magenta":
        my_arrow.initrightbutton()
    if nowtimer!=0:    
        window.after(300, button_clear)

def scene_clear():
    
    if(combo<10) :
        my_scene.redraw_baseback()
    elif(combo<30) :
        my_scene.redraw_comboback1()
        
    elif(combo<50) :
        my_scene.redraw_comboback2()
    else :
        my_scene.redraw_comboback3()
    window.after(2000,scene_clear)

def generate_char():
    if int(len(my_characters))!=7:
        itemchance1=random.randint(1,chance1)
        itemchance2=random.randint(1,chance2)
        if realtime<newchartime:
            randID=random.randint(0,1)
        else:
            randID=random.randint(0,3)
        getID=randIDs[randID]
        if itemchance1==7:
            middleID.append(5)
            my_characters.append(character.Character(scene=my_scene,charID=5,size=20, x_start=winW//2,y_start=100))
        elif itemchance2==7:
            middleID.append(6)
            my_characters.append(character.Character(scene=my_scene,charID=6,size=20, x_start=winW//2,y_start=100))
        else:
            middleID.append(getID)
            my_characters.append(character.Character(scene=my_scene,charID=getID,size=20, x_start=winW//2,y_start=100))
    if nowtimer!=0:
        window.after(20, generate_char)
        
def leftmatching(master):
    global score
    global combo
    
    if nowtimer!=0:
        my_arrow.leftbutton()
        #print(randIDs[0],"=?",middleID[0])
        if middleID[0]==randIDs[0] or middleID[0]==randIDs[2] or middleID[0]==5 or middleID[0]==6:
            if middleID[0]==5:
                itemcount=int(len(my_items))
                if itemcount<2:
                    my_items.append(5)
                    my_itemlook.append(character.Character(scene=my_scene,charID=5,size=20, x_start=650+itemcount*30,y_start=500))
            elif middleID[0]==6:
                for i in range(itemsec):
                    plustimer=int(len(my_timers))
                    my_timers.append(gametimer.Gametimer(scene=my_scene,index=plustimer))
            my_characters[0].remove()
            
            for i in range(0,len(my_characters)):
                my_characters[i].move()
            my_characters.pop(0)
            middleID.pop(0)
            score += 10
            my_scene.draw_score(score)
            combo += 1
            my_scene.draw_combo(combo)
            if(combo>10) :
                score += 100
                my_scene.draw_score(score)
            if(combo>30) :
                score += 1000
                my_scene.draw_score(score)
            if(combo>50) :
                score += 10000
                my_scene.draw_score(score)
            if(combo<10) :
                my_scene.redraw_baseback()
            elif(combo<30) :
                my_scene.redraw_comboback1()
            elif(combo<50) :
                my_scene.redraw_comboback2()
            else :
                my_scene.redraw_comboback3()
        else :
            my_scene.redraw_errorback()
            score += 0
            my_scene.draw_score(score)
            combo = 0
            my_scene.draw_combo(combo)
            minustimer=int(len(my_timers))-1
            if minustimer!=0:
                my_timers[minustimer].remove()
                my_timers.pop(minustimer)

def rightmatching(master):
    global score
    global combo
    if nowtimer!=0:
        my_arrow.rightbutton()
        if middleID[0]==randIDs[1] or middleID[0]==randIDs[3] or middleID[0]==5 or middleID[0]==6:
            if middleID[0]==5:
                itemcount=int(len(my_items))
                if itemcount<2:
                    my_items.append(5)
                    my_itemlook.append(character.Character(scene=my_scene,charID=5,size=20, x_start=650+itemcount*30,y_start=500))
            elif middleID[0]==6:
                for i in range(itemsec):
                    plustimer=int(len(my_timers))
                    my_timers.append(gametimer.Gametimer(scene=my_scene,index=plustimer))
            
            my_characters[0].remove()
            for i in range(0,len(my_characters)):
                my_characters[i].move()
            my_characters.pop(0)
            middleID.pop(0)
            score += 10
            my_scene.draw_score(score)
            combo += 1
            my_scene.draw_combo(combo)
            if(combo>10) :
                score += 100
                my_scene.draw_score(score)
            if(combo>30) :
                score += 1000
                my_scene.draw_score(score)
            if(combo>50) :
                score += 10000
                my_scene.draw_score(score)


            if(combo<10) :
                my_scene.redraw_baseback()
            elif(combo<30) :
                my_scene.redraw_comboback1()
            elif(combo<50) :
                my_scene.redraw_comboback2()
            else :
                my_scene.redraw_comboback3()
        else :
            my_scene.redraw_errorback()
            score += 0
            my_scene.draw_score(score)
            combo = 0
            my_scene.draw_combo(combo)
            minustimer=int(len(my_timers))-1
            if minustimer!=0:
                my_timers[minustimer].remove()
                my_timers.pop(minustimer)

def useitem(master):
    itemcount=int(len(my_items))
    if itemcount==1:
        my_itemlook[0].remove()
        my_items.pop(0)
        my_itemlook.pop(0)
        for i in range(7):
            my_characters[0].remove()
            my_characters.pop(0)
            middleID.pop(0)
    
        for i in range(7):
            middleID.append(randIDs[0])
            my_characters.append(character.Character(scene=my_scene,charID=randIDs[0],size=20, x_start=winW//2,y_start=winH-(100+i*80)))

    elif itemcount==2:
        my_itemlook[1].remove()
        my_items.pop(1)
        my_itemlook.pop(1)
        for i in range(7):
            my_characters[0].remove()
            my_characters.pop(0)
            middleID.pop(0)
    
        for i in range(7):
            middleID.append(randIDs[0])
            my_characters.append(character.Character(scene=my_scene,charID=randIDs[0],size=20, x_start=winW//2,y_start=winH-(100+i*80)))

    else:
        pass



        
window.bind("<Left>",leftmatching)
window.bind("<Right>",rightmatching)
window.bind("<space>",useitem)
timerflow()
timergetnum()
realtimeflow()
button_clear()
generate_char()
scene_clear()


window.mainloop()







