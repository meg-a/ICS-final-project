import turtle
import math



wn = turtle.Screen()
wn.title("game")
wn.bgcolor("black")
wn.setup(1200,800)
wn.tracer(0)


ground_y = -100



#draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()

player = turtle.Turtle()
player.shape("square")
player.color("white")
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
    
    

        
def jump():
    if player.state == "jumping_1":
        player.state = "jumping_2"
        player.dy = 5
    if player.state == "ready":
        player.state = "jumping_1"
        player.dy = 5 
    
    
def move_left():
    player.dx = -2
        
def move_right():
    player.dx = 2
    
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

wn.listen()
wn.onkeypress(jump,"space") 
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeyrelease(stop_left_right, "Left")
wn.onkeyrelease(stop_left_right, "Right")

blocks = []
blocks.append(Block(-600, 0, 2, 800))
blocks.append(Block(0, -370, 1200,2))
blocks.append(Block(-550, 300, 100, 2))
blocks.append(Block(-500, 275, 2, 50))
blocks.append(Block(-550, 250,100, 2))
blocks.append(Block(-550, 175,150, 2))
blocks.append(Block(-476, 136, 2, 75))
blocks.append(Block(-380, 320, 2, 150))
blocks.append(Block(-370, 245, 100, 2))
blocks.append(Block(-190, 245, 100, 2))
blocks.append(Block(-140, 320, 2, 150))
blocks.append(Block(-252, 175,300, 2))
blocks.append(Block(-425, 98,100, 2))
blocks.append(Block(-170, 98,290, 2))
blocks.append(Block(-376, 58,2, 77))
blocks.append(Block(-25, 250, 2, 300))
blocks.append(Block(-314, 23,2,150))
blocks.append(Block(-400, 15,50,2))
blocks.append(Block(-550, 15,100,2))
blocks.append(Block(-402,-50,178,2))
blocks.append(Block(-491,-100,2,100))
blocks.append(Block(-420,-150,140,2))
blocks.append(Block(-500,-250,250,2))
blocks.append(Block(-170,-250,259,2))
blocks.append(Block(-230,-140,2,470))
blocks.append(Block(-140,-120,2,250))
blocks.append(Block(-40,5,200,2))
blocks.append(Block(60,-35,2,680))
blocks.append(Block(160,305,200,2))
blocks.append(Block(-255,-190,40,2))
blocks.append(Block(36,-310,50,2))
blocks.append(Block(36,-200,50,2))
blocks.append(Block(-100,-170,80,2))

#entrance to teleport
entrances = []
entrances.append(Block(-595,-340, 3, 50))
entrances.append(Block(-595,200, 3, 50))
entrances.append(Block(-486,-120, 3, 50))
entrances.append(Block(-135,-145,3,50))
 

for entrance in entrances:
    entrance.color = "red"

#exit of the teleport
exits = []
exits.append(Block(-280,388,50,3))
exits.append(Block(-150,-255,50,3))
for exit in exits:
    exit.color = "blue"

gateways_list = [entrances,exits]

player.goto(-500,400)

while True:
    pen.penup()
    pen.goto(-430, 24)
    pen.pendown()
    pen.forward(120)
    pen.right(1)
    
    
  
    
       
    
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

    
    print(str(player.xcor()) + " " + str(player.ycor()))
    
    
        
    if player.xcor()<=-585 and ((player.ycor()>=180 and player.ycor()<=210)or(player.ycor()>=-360 and player.ycor() <=-330)):
        player.goto(-280,400)
        player.dy = 0
        player.dx = 0
                    
    elif player.xcor() == -480  and (player.ycor()>=-144 and player.ycor()<=-95):
        player.goto(-147,-255)
        player.dy = 0
        player.dx = 0
        
    elif player.xcor() == -129  and (player.ycor()>=-162 and player.ycor()<=-120):
        player.goto(-147,-255)
        player.dy = 0
        player.dx = 0
        
wn.onkeypress(up,"up")




wn.mainloop()

