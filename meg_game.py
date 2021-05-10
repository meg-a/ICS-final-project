import turtle
import math
import os
import time



wn = turtle.Screen()
wn.title("game")
wn.bgcolor("sky blue")
wn.setup(1220,800)
wn.tracer(0)

wn.bgpic('introduction.gif')
wn.update()
time.sleep(6)
wn.bgpic("")

#ground_y = -100



#draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("circle")
pen.color("green")
pen.penup()
pen.hideturtle()




#life
# ~ life = turtle.Turtle()
# ~ life.speed(0)
# ~ life.pensize(3)
# ~ life.shape()
# ~ life.color("white")
# ~ life.penup()
# ~ life.hideturtle()

wn.addshape('sprite.gif')
#draw sprite
player = turtle.Turtle()
player.shape('sprite.gif')
player.speed(0)
player.penup()
player.width = 20
player.height = 20
player.dx = 0
player.dy = 0
player.state = "ready"
player.goto(0, 0)



GRAVITY = -0.3

#class for the ground
class Block(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        self.color = "green"
    
        
        
        
    def render(self, pen):
        pen.penup()
        pen.goto(self.x - self.width/2.0, self.y+self.height/2.0)
        pen.pendown()
        pen.pencolor(self.color)
        pen.goto(self.x + self.width/2.0, self.y+self.height/2.0)
        pen.goto(self.x + self.width/2.0, self.y-self.height/2.0)
        pen.goto(self.x - self.width/2.0, self.y-self.height/2.0)
        pen.goto(self.x - self.width/2.0, self.y+self.height/2.0)
    
    

#make the user jump        
def jump():
    if player.state == "jumping_1":
        player.state = "jumping_2"
        player.dy = 5
        os.system("afplay jump2.mp3&")
    if player.state == "ready":
        player.state = "jumping_1"
        player.dy = 5 
        os.system("afplay jump1.mp3&")
    
#make the user move to left    
def move_left():
    player.dx = -2

#make the user move to right        
def move_right():
    player.dx = 2

#make the user stop    
def stop_left_right():
    player.dx = 0


    
def stop_down(ground,player_height):
    player.sety(ground_y+player.height/2) 
    player.dy = 0
    player.state = "ready"
    
def is_collision(player, block):
    # Axis Aligned Bounding Box
    x_collision = (math.fabs(player.xcor() - block.x) * 2) < (player.width + block.width)
    y_collision = math.fabs(player.ycor() - block.y) * 2 < (player.height + block.height)
    return (x_collision and y_collision)

def teleport_sound():
    os.system('afplay teleport.mp3&')
    

#make available for user to input
wn.listen()
wn.onkeypress(jump,"space") 
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeyrelease(stop_left_right, "Left")
wn.onkeyrelease(stop_left_right, "Right")


#place the boxes


level1 = (
    (-600, 0, 2, 800),
    (600, 0, 2, 800),
    (0, -370, 1200,2),
    (-550, 300, 100, 2),
    (-500, 275, 2, 50),
    (-550, 250,100, 2),
    (-550, 175,150, 2),
    (-476, 136, 2, 75),
    (-380, 320, 2, 150),
    (-370, 245, 100, 2),
    (-190, 245, 100, 2),
    (-140, 320, 2, 150),
    (-252, 175,300, 2),
    (-425, 98,100, 2),
    (-170, 98,290, 2),
    (-376, 58,2, 77),
    (-25, 250, 2, 300),
    (-314, 23,2,150),
    (-400, 15,50,2),
    (-550, 15,100,2),
    (-402,-50,178,2),
    (-491,-100,2,100),
    (-420,-150,140,2),
    (-500,-250,250,2),
    (-170,-250,259,2),
    (-230,-140,2,470),
    (-140,-120,2,245),
    (-40,5,200,2),
    (60,-35,2,680),
    (159,308,200,2),
    (-255,-190,40,2),
    (-264,-100,60,2),
    (36,-310,50,2),
    (36,-200,50,2),
    (41,150,40,2),
    (-5,308,40,2),
    (-100,-170,80,2),
    (20,-110,80,2),
    (240,230,200,2),
    (340,230,2,155),
    (200,150,280,2),
    (415,308,150,2),
    (490,210,2,190),
    (575,230,50,2),
    (335,50,550,2),
    (460,115,60,2),
    (370,180,60,2),
    (270,-270,2,195),
    (210,-310,120,2),
    (122,-240,120,2),
    (290,-170,270,2),
    (540,-170,110,2),
    (475,-310,250,2),
    (440,-240,180,2),
    (350,-275,2,70),
    (280,-100,436,2),
    (450,-30,300,2),
    (200,-25,2,150)

)

blocks = []

for block in level1:
    x = block[0]
    y = block[1]
    width = block[2]
    height = block[3]
    blocks.append(Block(x, y, width, height))


# ~ pen.goto(50,-20)
# ~ pen.down()
# ~ pen.shape('goal.gif')
# ~ pen.up()



#entrance to teleport
entrances = []
entrances.append(Block(-595,-340, 3, 50))
entrances.append(Block(-595,200, 3, 50))
entrances.append(Block(-486,-120, 3, 50))
entrances.append(Block(-135,-145,3,50))
entrances.append(Block(55,-85,3,50))
entrances.append(Block(-185,-245,50,3))
entrances.append(Block(335,179,3,50))
entrances.append(Block(344,208,3,50))
entrances.append(Block(355,-280,3,50))
entrances.append(Block(595,-340,3,50))
entrances.append(Block(595,-5,3,50))

for entrance in entrances:
    entrance.color = "red"

#exit of the teleport
exits = []
exits.append(Block(-280,388,50,3))
exits.append(Block(-150,-255,50,3))
exits.append(Block(-272,93,50,3))
exits.append(Block(100,388,50,3))
exits.append(Block(264,-345,3,50))
for exit in exits:
    exit.color = "blue"

gateways_list = [entrances,exits]


# ~ player.goto(-500,400)
player.goto(-500,400)

# ~ def playerlife()
    # ~ life.setposition(300,300)
    # ~ life.write(life)

player_life = 50
while True:
    
    
    
    # ~ pen_x = [-425,550]
    # ~ pen_y = [15,230]
    # ~ pen_length = [100,50]
    
    # ~ for i in range(2):
        # ~ pen.penup()
        # ~ pen.goto(pen_x[i],pen_y[i])
        # ~ pen.pendown()
        # ~ pen.forward(pen_length[i])
        # ~ pen.right(0.5)
        
        # ~ pen.shape("circle")
        # ~ pen.color("red")
        # ~ pen.stamp() 
        # ~ pen.color("green")
        # ~ # Check for collision with player
        # ~ if player.distance(pen) < 20:
            # ~ player_life = player_life - 1
            # ~ print(player_life)
        # ~ else:
            # ~ print("")
        
    
  
    
       
    
    #Gravity
    player.dy += GRAVITY
    
    #Move the player
    y = player.ycor()
    y += player.dy
    player.sety(y)  
    
    x = player.xcor()
    x += player.dx
    player.setx(x)
    
    for gateways in gateways_list:
        for gateway in gateways:
            gateway.render(pen)
            
        
        
    
    #Deal with the ground
    for block in blocks:
        block.render(pen)
        if is_collision(player, block):
            
             # Player is to the left
            if player.xcor() < block.x - block.width/2.0 and player.dx > 0:
                player.dx = 0
                player.setx(block.x - block.width/2.0 - player.width/2.0)
            # Player is to the right
            elif player.xcor() > block.x + block.width/2.0 and player.dx < 0:
                player.dx = 0
                player.setx(block.x + block.width/2.0 + player.width/2.0)
            # Player is above
            elif player.ycor() > block.y:
                player.dy = 0
                player.sety(block.y + block.height/2.0 + player.height/2.0 - 1)
            # Player is below
            elif player.ycor() <= block.y:
                player.dy = 0
                player.sety(block.y - block.height/2.0 - player.height/2.0)

            player.state = "ready"
                
                
    wn.update()
    pen.clear()

    
    # ~ print("x:"+str(player.xcor()) + " y: " + str(player.ycor()))
    
    
        
    if player.xcor()<=-585 and ((player.ycor()>=180 and player.ycor()<=210)or(player.ycor()>=-360 and player.ycor() <=-330)):
        player.goto(-280,400)
        player.dy = 0
        player.dx = 0
        teleport_sound()
                    
    elif player.xcor() == -480  and (player.ycor()>=-144 and player.ycor()<=-95):
        player.goto(-147,-255)
        player.dy = 0
        player.dx = 0
        teleport_sound()
        
    
        
    elif player.xcor() == 49  and (player.ycor()>=-100 and player.ycor()<=-80):
        player.goto(100,400)
        player.dy = 0
        player.dx = 0
        teleport_sound()
        
    elif (player.xcor() >= -220 and player.xcor() <= -151) and player.ycor() ==-240:
        player.goto(-272,80)
        player.dy = 0
        player.dx = 0
        teleport_sound()
    
    elif player.xcor() == -129  and (player.ycor()>=-162 and player.ycor()<=-120):
        player.goto(-272,80)
        player.dy = 0
        player.dx = 0
        os.system('afplay goal.mp3&')
        
    elif player.xcor() == 329  and (player.ycor()>=160 and player.ycor()<=200):
        player.goto(100,400)
        player.dy = 0
        player.dx = 0
        teleport_sound()
        
    elif player.xcor() == 589  and (player.ycor()>=-360  and player.ycor()<=-320):
        player.goto(257,-350)
        player.dy = 0
        player.dx = 0
        teleport_sound()
            
    elif player.xcor() == 351  and (player.ycor()>=190 and player.ycor()<=230):
        player.goto(257,-350)
        player.dy = 0
        player.dx = 0
        teleport_sound()
    
    elif player.xcor() == 361  and (player.ycor()>=-300  and player.ycor()<=-260):
        player.goto(160,-30)
        player.dy = 0
        player.dx = 0
        teleport_sound()
        
    elif player.xcor() == 589  and (player.ycor()>=-20  and player.ycor()<=20):
        player.goto(-280,400)
        player.dy = 0
        player.dx = 0
        teleport_sound()
        

wn.mainloop()
