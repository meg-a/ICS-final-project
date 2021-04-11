import turtle



wn = turtle.Screen()
wn.title("game")
wn.bgcolor("black")
wn.setup(1000,1000)





player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.speed(0)
player.penup()


ground = turtle.Turtle()
ground.shape("square")
ground.color("green")




                       
def move_left():
    while True:
        player.backward(2)
        
    
    

def move_right():
    while True:
        player.forward(2)
    
def stay():
    while True:
        player.setheading(0)
        player.forward(0)
        


can_jump = False
 



def jump():
    time=0
    position = player.position()
    start_y = position[1]
    t_or_f = True
    while t_or_f:
        time=time+0.5
        player.setheading(90)
        player.forward(5*time-(time**2))
        if start_y < position[1]:
            t_or_f = False
    
            
    
        
        
    
        

    

        

    



wn.listen()
wn.onkeypress(move_left,"Left")
wn.onkeypress(move_right,"Right")
wn.onkeypress(jump,"Up")

commands = ["Left","Right","Up"]

for command in commands:
    wn.onkeyrelease(stay,command)

# ~ wn.onkeypress(up,"up")










wn.mainloop()

