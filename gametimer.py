import scene
class Gametimer:
    def __init__(self, scene, color="purple" , size=4,index=0, pos_x=150,pos_y=680):
        
        self.scene=scene
        self.color=color
        self.size=size
        
        self.posx=pos_x+(size+7)*(index+1)+4
        self.posy=pos_y
        self.shape=self.scene.draw_timersecond(self)

            
    def remove(self):
        self.scene.remove_item(self.shape)
