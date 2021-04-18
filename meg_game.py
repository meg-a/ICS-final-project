import turtle
import math



wn = turtle.Screen()
wn.title("game")
wn.bgcolor("black")
wn.setup(1000,1000)
wn.tracer(0)


ground_y = -100



#draw ground
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

player = turtle.Turtle()
player.shape("square")
player.color("white")
player.speed(0)
player.penup()
player.width = 10
player.height = 10
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
        
        
    def render(self, pen):
        pen.penup()
        pen.goto(self.x - self.width/2.0, self.y+self.height/2.0)
        pen.pendown()
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
    
def is_collision(sprite, block):
    # Axis Aligned Bounding Box
    x_collision = (math.fabs(sprite.xcor() - block.x) * 2) < (sprite.width + block.width)
    y_collision = (math.fabs(sprite.ycor() - block.y) * 2) < (sprite.height + block.height)
    return (x_collision and y_collision)

wn.listen()
wn.onkeypress(jump,"space") 
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeyrelease(stop_left_right, "Left")
wn.onkeyrelease(stop_left_right, "Right")

blocks = []
blocks.append(Block(0, -50, 100, 2))
blocks.append(Block(-100, -100, 100, 2))
blocks.append(Block(100, -100, 100, 2))
blocks.append(Block(200, -150, 150, 2))
blocks.append(Block(200, -120, 100, 2))

for block in blocks:
    block.render(pen)

while True:
    
    #Gravity
    player.dy += GRAVITY
    
    #Move the player
    y = player.ycor()
    y += player.dy
    player.sety(y)  
    
    x = player.xcor()
    x += player.dx
    player.setx(x)
    
    #Deal with the ground
    for block in blocks:
        if is_collision(player, block):
            player.sety(block.y+block.height/2.0 + player.height/2.0) 
            player.dy = 0
            player.state = "ready"
            
    
    

    
    wn.update()


                       

    
def stay():
    while True:
        x = player.xcor()
        player.setx(x+1)
        
        



wn.onkeypress(up,"up")




wn.mainloop()
