import scene
class Character:
    def __init__(self, scene, charID=0, color="yellow" , size=10, x_start=0,y_start=0):
        
        self.scene=scene
        self.charID=charID
        self.color=color
        self.size=size
        self.x_start=x_start
        self.y_start=y_start
        self.posx=x_start
        self.posy=y_start
        if charID==1:
            #self.shape=self.scene.draw_rectangle(self)
            self.shape=self.scene.draw_lian(self)
        elif charID==2:
            self.shape=self.scene.draw_tube(self)
        elif charID==3:
            self.shape=self.scene.draw_peach(self)
        elif charID==4:
            self.shape=self.scene.draw_prodo(self)
        elif charID==5:
            self.shape=self.scene.draw_item1(self)
        elif charID==6:
            self.shape=self.scene.draw_item2(self)
            
    def move(self):
        
        self.posy+=80
        x=self.posx
        y=self.posy
        #x1= self.posx-(self.size*3//2)
        #x2 = self.posx+(self.size*3//2)
        #y1 = self.posy-(self.size*3//2)
        #y2 = self.posy+(self.size*3//2)
        #self.scene.move_item(self.shape, x1, y1, x2, y2)
        self.scene.move_itemCR(self.shape,x,y)
        
            
    def remove(self):
        self.scene.remove_item(self.shape)
