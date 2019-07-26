import scene
class Arrow:
    def __init__(self,scene,color="beige", size=10,x_start=0,y_start=0):
        self.scene=scene
        self.leftcolor=color
        self.rightcolor=color
        self.size=size
        self.x_start=x_start
        self.y_start=y_start
        self.leftposx=x_start-200
        self.leftposy=y_start
        self.rightposx=x_start+200
        self.rightposy=y_start
        
        self.leftarrow1=self.scene.draw_leftarrow1(self)
        self.leftarrow2=self.scene.draw_leftarrow2(self)

        self.rightarrow1=self.scene.draw_rightarrow1(self)
        self.rightarrow2=self.scene.draw_rightarrow2(self)

    def initleftbutton(self):
        self.leftcolor="beige"
        self.scene.change_item_colour(self.leftarrow1, self.leftcolor)
        self.scene.change_item_colour(self.leftarrow2, self.leftcolor)
        
    def initrightbutton(self):
        self.rightcolor="beige"    
        self.scene.change_item_colour(self.rightarrow1, self.rightcolor)
        self.scene.change_item_colour(self.rightarrow2, self.rightcolor)        
    def leftbutton(self):
        self.leftcolor="magenta"
        self.scene.change_item_colour(self.leftarrow1, self.leftcolor)
        self.scene.change_item_colour(self.leftarrow2, self.leftcolor)
        
    def rightbutton(self):
        self.rightcolor="magenta"
        self.scene.change_item_colour(self.rightarrow1, self.rightcolor)
        self.scene.change_item_colour(self.rightarrow2, self.rightcolor)  
        
    def getleftcolor(self):
        return self.leftcolor
    
    def getrightcolor(self):
        return self.rightcolor
    
