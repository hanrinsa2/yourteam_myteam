from tkinter import *

class Scene:
    def __init__(self,window,color="black",width=1000,height=700):
        self.width=width
        self.height=height
        self.color=color

        self.canvas=Canvas(window, bg=self.color,height=self.height, width=self.width)
        self.canvas.pack()

        self.baseback='grassland.png'
        self.Bbackground=PhotoImage(file=self.baseback)

        self.errorback='rain.png'
        self.Ebackground=PhotoImage(file=self.errorback)
        
        self.comboback1='sky.png'
        self.Cbackground1=PhotoImage(file=self.comboback1)

        self.comboback2='thunder.png'
        self.Cbackground2=PhotoImage(file=self.comboback2)

        self.comboback3='universe.png'
        self.Cbackground3=PhotoImage(file=self.comboback3)

        self.gameover='gameover.png'
        self.Obackground=PhotoImage(file=self.gameover)
        
        self.getimages=self.canvas.create_image(width//2, height//2, image=self.Bbackground,anchor=CENTER)
        
        self.font = ("monaco", 30,"bold italic")

        self.scoreposx=800
        self.scoreposy=90
        self.timerfont=("arial", 20,"bold")
        #스코어보드판
        self.scoreboard = self.canvas.create_text(self.scoreposx, self.scoreposy, font=self.font, fill = "blue")
        self.comboboard = self.canvas.create_text(800, 130, font=self.font, fill= "yellow")
        self.timerboard = self.canvas.create_text(130,640, font=self.timerfont, fill="white")
        self.lianImage=PhotoImage(file='lian.png')
        self.tubeImage=PhotoImage(file='tube.png')
        self.peachImage=PhotoImage(file='peach.png')
        self.prodoImage=PhotoImage(file='prodo.png')
        self.itemImage1=PhotoImage(file='item1.png')
        self.itemImage2=PhotoImage(file='item2.png')
        self.timer=PhotoImage(file='timer.png')
    # Canvas에 직사각형을 추가하는 도구:
    def draw_rectangle(self, rectangle):
        x1 = rectangle.posx-(rectangle.size*3//2)
        x2 = rectangle.posx+(rectangle.size*3//2)
        y1 = rectangle.posy-(rectangle.size*3//2)
        y2 = rectangle.posy+(rectangle.size*3//2)
        c = "red"
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
    # Canvas에 라이언 캐릭터를 추가하는 도구:
    def draw_lian(self, lian):
        x = lian.posx    
        y = lian.posy
        return self.canvas.create_image(x, y, image=self.lianImage,anchor=CENTER)

    # Canvas에 튜브 캐릭터를 추가하는 도구:
    def draw_tube(self, tube):
        x = tube.posx    
        y = tube.posy
        return self.canvas.create_image(x, y, image=self.tubeImage,anchor=CENTER)
    def draw_peach(self, peach):
        x = peach.posx    
        y = peach.posy
        return self.canvas.create_image(x, y, image=self.peachImage,anchor=CENTER)
    def draw_prodo(self, prodo):
        x = prodo.posx    
        y = prodo.posy
        return self.canvas.create_image(x, y, image=self.prodoImage,anchor=CENTER)
    def draw_item1(self, item1):
        x = item1.posx    
        y = item1.posy
        return self.canvas.create_image(x, y, image=self.itemImage1,anchor=CENTER)
    def draw_item2(self, item2):
        x = item2.posx    
        y = item2.posy
        return self.canvas.create_image(x, y, image=self.itemImage2,anchor=CENTER)
    def draw_timer(self):
        x = 130    
        y = 640
        return self.canvas.create_image(x, y, image=self.timer,anchor=CENTER)
    # Canvas에 타원을 추가하는 도구:
    def draw_oval(self, oval):
        x1 = oval.posx-(oval.size*3//2)
        x2 = oval.posx+(oval.size*3//2)
        y1 = oval.posy-(oval.size*3//2)
        y2 = oval.posy+(oval.size*3//2)
        c = oval.color
        return self.canvas.create_oval(x1, y1, x2, y2, fill=c)
    #Canvas에 화살표를 추가하는 도구:
    def draw_leftarrow1(self, arrow):
        arrow.leftposx+=20
        xr1 = arrow.leftposx-(arrow.size*3)
        yr1 = arrow.leftposy-(arrow.size*3//2)
        xr2 = arrow.leftposx+(arrow.size*3)
        yr2 = arrow.leftposy-(arrow.size*3//2)
        xr3 = arrow.leftposx+(arrow.size*3)
        yr3 = arrow.leftposy+(arrow.size*3//2)
        xr4 = arrow.leftposx-(arrow.size*3)
        yr4 = arrow.leftposy+(arrow.size*3//2)
        c = arrow.leftcolor
        
        return self.canvas.create_polygon(xr1, yr1, xr2, yr2, xr3, yr3, xr4, yr4,fill=c)
    def draw_leftarrow2(self, arrow):
        arrow.leftposx-=40
        xt1 = arrow.leftposx-(arrow.size*3)
        yt1 = arrow.leftposy
        xt2 = arrow.leftposx+(arrow.size*3//2)
        yt2 = arrow.leftposy+arrow.size*3
        xt3 = arrow.leftposx+(arrow.size*3//2)
        yt3 = arrow.leftposy-arrow.size*3
        c = arrow.leftcolor
        
        return self.canvas.create_polygon(xt1,yt1,xt2,yt2,xt3,yt3,fill=c)

    def draw_rightarrow1(self, arrow):
        arrow.rightposx-=20
        xr1 = arrow.rightposx-(arrow.size*3)
        yr1 = arrow.rightposy-(arrow.size*3//2)
        xr2 = arrow.rightposx+(arrow.size*3)
        yr2 = arrow.rightposy-(arrow.size*3//2)
        xr3 = arrow.rightposx+(arrow.size*3)
        yr3 = arrow.rightposy+(arrow.size*3//2)
        xr4 = arrow.rightposx-(arrow.size*3)
        yr4 = arrow.rightposy+(arrow.size*3//2)
        c = arrow.leftcolor
        
        return self.canvas.create_polygon(xr1, yr1, xr2, yr2, xr3, yr3, xr4, yr4,fill=c)

    def draw_rightarrow2(self, arrow):
        arrow.rightposx+=40
        xt1 = arrow.rightposx+(arrow.size*3)
        yt1 = arrow.rightposy
        xt2 = arrow.rightposx-(arrow.size*3//2)
        yt2 = arrow.rightposy+arrow.size*3
        xt3 = arrow.rightposx-(arrow.size*3//2)
        yt3 = arrow.rightposy-arrow.size*3
        c = arrow.rightcolor
        
        return self.canvas.create_polygon(xt1,yt1,xt2,yt2,xt3,yt3,fill=c)

    def draw_timersecond(self, timer):
        x1 = timer.posx-timer.size
        x2 = timer.posx+timer.size
        y1 = timer.posy-timer.size*3
        y2 = timer.posy+timer.size*3
        c = "purple"
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=c)
    
    # canvas의 아이템을 조작할 수 있는 도구:
    def move_item(self, item, x1, y1, x2, y2):
        self.canvas.coords(item, x1, y1, x2, y2)

    def move_itemCR(self, item, x, y):
        self.canvas.coords(item, x, y)
        
    def remove_item(self, item):
        self.canvas.delete(item)

    def change_item_colour(self, item, c):
        self.canvas.itemconfigure(item, fill=c)

    def draw_score (self, score) :
        score = "현재 점수 :" + str(score)
        self.canvas.itemconfigure(self.scoreboard, text= score)

    def draw_totalscore (self, score) :
        score = "총 점수 :" + str(score)
        self.canvas.itemconfigure(self.scoreboard, text= score)

    def draw_timernumber (self, timernumber) :
        
        if timernumber<20:
            self.timerboard = self.canvas.delete(self.timerboard)
            self.timerfont=("arial", 24,"bold italic")
            self.timerboard = self.canvas.create_text(110,670, font=self.timerfont, fill="red")
            timernumber =str(timernumber)
            self.canvas.itemconfigure(self.timerboard, text= timernumber)
        else:
            self.timerboard = self.canvas.delete(self.timerboard)
            self.timerfont=("arial", 20,"bold")
            self.timerboard = self.canvas.create_text(110,670, font=self.timerfont, fill="white")
            timernumber =str(timernumber)
            self.canvas.itemconfigure(self.timerboard, text= timernumber)

            
    def draw_combo (self, combo) :
        
        
        if(combo < 10) :
            result = str(combo) +"Combo"
            self.comboboard = self.canvas.delete(self.comboboard)
            self.comboboard = self.canvas.create_text(self.width//2, 30, font=self.font, fill= "yellowgreen")
            self.canvas.itemconfigure(self.comboboard, text= result)
            
        elif(combo < 30) :
            result = str(combo) +"Combo!!"
            font = ("mincho", 32, "bold")
            self.comboboard = self.canvas.delete(self.comboboard)
            self.comboboard = self.canvas.create_text(self.width//2, 30, font=font, fill= "yellow")
            self.canvas.itemconfigure(self.comboboard, text= result)
        elif(combo < 50) :
            result = str(combo) +"Perfect~"
            font = ("arial", 34,"bold italic")
            self.comboboard = self.canvas.delete(self.comboboard)
            self.comboboard = self.canvas.create_text(self.width//2, 30, font=font, fill= "red")
            self.canvas.itemconfigure(self.comboboard, text= result)
        else :
            result = str(combo) +"Awesome~!!!"
            font = ("Verdana", 38,"bold italic")
            self.comboboard = self.canvas.delete(self.comboboard)
            self.comboboard = self.canvas.create_text(self.width//2, 30, font=font, fill= "pink")
            self.canvas.itemconfigure(self.comboboard, text= result)
    def redraw_baseback(self):
        self.canvas.itemconfigure(self.getimages,image=self.Bbackground)
        
    def redraw_errorback(self):
        self.canvas.itemconfigure(self.getimages,image=self.Ebackground)
        
    def redraw_comboback1(self):
        self.canvas.itemconfigure(self.getimages,image=self.Cbackground1)
    def redraw_comboback2(self):
        self.canvas.itemconfigure(self.getimages,image=self.Cbackground2)
    def redraw_comboback3(self):
        self.canvas.itemconfigure(self.getimages,image=self.Cbackground3)
        
    def draw_gameover(self):
        self.canvas.create_image(self.width//2, self.height//2, image=self.Obackground,anchor=CENTER)
        self.scoreposx=500
        self.scoreposy=600
        self.scoreboard = self.canvas.create_text(self.scoreposx, self.scoreposy, font=self.font, fill = "blue")
        
