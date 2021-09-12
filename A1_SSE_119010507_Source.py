import turtle
import time
import random

delay = 200                            

screen = turtle.Screen()                 
contact = 0
second = 0
screen.title(f'Snake Game | Contacted: {contact} Time: {second}')
screen.bgcolor("black")
screen.setup(width=500, height=500)
screen.tracer(0)


contact_check = False                   


intro = turtle.Turtle()                  
intro.speed(0)
intro.shape("square")
intro.color("white")
intro.penup()
intro.goto(0,140)
context ="""
    Welcome to Ryan's Snake Game!
    Please use arrow key to move the snake.
    In order to win, consume all the food without head-contact with monster
            
    Click anywhere on the screen to start the game..."""
intro.write(context, align="center", font=("Verdana", 10, "normal"))
intro.hideturtle()

head = turtle.Turtle()            
head.speed(0)
head.color("red")
head.shape("square")
head.penup()
head.goto(0,0)
headDirection = "stop"
preDirection = "stop"


body = []       
for i in range (0,5):
    new_segments = turtle.Turtle()
    new_segments.speed(0)
    new_segments.color("white","grey")
    new_segments.shape("square")
    new_segments.penup()
    new_segments.goto(-10000,-10000)
    body.append(new_segments)


monster = turtle.Turtle()               
monster.speed(0)
monster.color("purple")
monster.shape("square")
monster.penup()
xcoor = random.randint(-230,230)
ycoor = random.randint(-230,-180)
monster.goto(xcoor,ycoor)
monster_headdirection = "stop"


food_list = []                          
total = 0                            
temp = delay                            
E_delay = delay + 100
counter = 0                       
check = False                    
timepause = 0                        
nopause = 0
stopgame = False                      


def go_up():                         
    global headDirection    
    headDirection = "up"
def go_down():
    global headDirection
    headDirection = "down"
def go_left():
    global headDirection    
    headDirection = "left"
def go_right():
    global headDirection
    headDirection = "right"
def stop():
    global headDirection
    headDirection = "stop"
    

def game_key(x):                         
    if x == True: 
        screen.listen()
        screen.onkeypress(go_up,"Up")
        screen.onkeypress(go_down,"Down")
        screen.onkeypress(go_left,"Left")
        screen.onkeypress(go_right,"Right")


def start_screen(x,y):                         
    global counter, headDirection
    intro.clear()
    if counter < 1:
        for i in range (1,10):          
            food = turtle.Turtle()
            food.speed(0)
            food.color("white")
            food.penup()
            food.hideturtle()
            x = 0
            y = 0
            x = random.randint(-240,230)
            y = random.randint(-240,230)
            food.goto(x,y)
            food.write(i, align="center",font = ("Arial",9,"normal"))
            food_list.append(food)
            headDirection = "stop"
            monster_headdirection != "stop"
        counter += 1
    snake_move()
    monster_move()
    game_key(True)

def snake_move():                  
    global stopgame, headDirection, timepause, check
    if stopgame == False:
        if (headDirection == "up" and head.ycor() < 240) or (headDirection == "down" and head.ycor() > -240) or (headDirection == "left" and head.xcor() > -240) or (headDirection == "right" and head.xcor() < 240):
            for i in range (len(body)-1,0,-1):           
                x = body[i-1].xcor()
                y = body[i-1].ycor()
                body[i].goto(x,y)
                body[i].showturtle()

            x = head.xcor()
            y = head.ycor()
            body[0].goto(x,y)
            body[0].showturtle()

        if headDirection == "up" and head.ycor() < 240:
            y = head.ycor()
            head.sety(y + 20)
        if headDirection == "down" and head.ycor() > -240:
            y = head.ycor()
            head.sety(y - 20)
        if headDirection == "left" and head.xcor() > -240:
            x = head.xcor()
            head.setx(x - 20)
        if headDirection == "right" and head.xcor() < 240:
            x = head.xcor()
            head.setx(x + 20)
        if check == False:
            second = int(time.time() - time_start)         
            screen.title(f'Snake Game | Contacted: {contact} Time: {second}')

        screen.ontimer(snake_move,delay)

def monster_move():                    
    global contact, contact_check, temp, stopgame, headDirection, monster_headdirection
    if stopgame == False:
        if monster_headdirection == "stop":
            xcorsnake = head.xcor()
            ycorsnake = head.ycor()
            xcormonster = monster.xcor()
            ycormonster = monster.ycor()
            dif_x = xcormonster - xcorsnake
            dif_y = ycormonster - ycorsnake
            
            if abs(dif_x) >= abs(dif_y):
                if dif_x > 0:
                    x = monster.xcor()
                    monster.setx(x - 20)
                if dif_x < 0:
                    x = monster.xcor()
                    monster.setx(x + 20)
            else:
                if dif_y > 0:
                    y = monster.ycor()
                    monster.sety(y - 20)
                if dif_y < 0:
                    y = monster.ycor()
                    monster.sety(y + 20)
            
        check = 0
        for n in body:              
            if n.distance(monster) < 20 and contact_check == False:
                contact += 1
                contact_check = True
            if n.distance(monster) > 20:
                check += 1

        if check == len(body):
            contact_check = False

        screen.ontimer(monster_move,random.randint(temp-50,temp+400))    

def consume():                      
    index = 0
    total = 0
    while index < len(food_list):               
        if food_list[index].distance(head) < 20:
            food_list[index].goto(10000,-10000) 
            food_list[index].clear()
            total = total + index + 1
        index += 1

    for i in range (0,total):                   
        new_segments = turtle.Turtle()
        new_segments.speed(0)
        new_segments.color("white","grey")
        new_segments.shape("square")
        new_segments.penup()
        new_segments.goto(10000,10000)
        body.append(new_segments)

def pause():                                
    global headDirection, preDirection, timepause, nopause, stop, check
    if headDirection != "stop":
        preDirection = headDirection
        stop()
    else:
        headDirection = preDirection
        timepause += int(time.time() - nopause)
        game_key(True)       

screen.listen()
screen.onscreenclick(start_screen)
screen.onkeypress(pause,"space")

time_start = time.time()
while True:                        
    screen.update()
    consume()

    for n in body:                     
        x = n.xcor()
        y = n.ycor()
        if x == 10000 and y == 10000:
            delay = E_delay
            break
        else:
            delay = temp
    if head.distance(monster) < 20:
        screen.update()
        head.write("GAME OVER!!!  ",align = "center", font = ("Verdana", 16, "bold"))
        stopgame = True
        break
    if len(body) == 50 and delay == temp:
        screen.update()
        head.write("WINNER!!!  ",align = "center", font = ("Verdana", 16, "bold"))
        stopgame = True
        break


screen.mainloop()