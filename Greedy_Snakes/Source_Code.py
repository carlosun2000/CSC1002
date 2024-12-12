import turtle
import random
#create the turtlr objects for the head, tail, and moster
tail = turtle.Turtle('square')
head = turtle.Turtle('square')
Monster = turtle.Turtle('square')
#create turtle objects for five pens
pen=turtle.Turtle()                #draw the boundary and title
pen1=turtle.Turtle()               #write the description
pen2=turtle.Turtle()               #write the status of motion and contact
pen3=turtle.Turtle()               #write the status of time
pen4 = turtle.Turtle()             #write the food
pen5 = turtle.Turtle()             #write the terminal words
#set the initial value of some global variable to be used
g_dict_food={}                  #this dictionary is used for storage of food
g_list1=['N']                   #this list is for store the moving information
g_list2=[]                      #get the list of coordinates of tails
g_list4=[]                      # this list is for storage of tail stamps id
g_taillist=[]                   #storage of tail coordinates
g_i=0                           #g_i=0 means stop and g_i=1 means game start 
g_j=0                           #this variable controls the pause or continue
g_k=0
g_extend=5                      #the length to be extended
g_length = 6                    #current length of the body
g_Contact = 0                   
g_Time = 0
g_motion = 'Paused'

#the following part is intented to initialize the game.
#the uses of the following functions in this part are given by the function names
def initialize_head():
    head.up()
    head.screen.tracer(0)
    head.setpos(0,-40)
    head.color('red','red')

def initialize_tail():                 
    tail.up()
    tail.screen.tracer(0)
    tail.setpos(0,-40)
    tail.color('blue','black')
    
def initialize_pens():                  #pen pen1 pen2 pen3 pen4 pen5 
    pen.hideturtle()
    pen.screen.tracer(0)
    pen.up()

    pen1.hideturtle()
    pen1.screen.tracer(0)
    pen1.up()

    pen2.hideturtle()
    pen2.screen.tracer(0)
    pen2.up()

    pen3.hideturtle()
    pen3.screen.tracer(0)
    pen3.up()
    pen3.goto(-5,230)

    pen4.hideturtle()
    pen4.screen.tracer(0)
    pen4.up()

    pen5.hideturtle()
    pen5.screen.tracer(0)
    pen5.up()
    pen5.color('purple')

def draw_the_title():                          #draw the upper rectangle
    pen.goto(250,210)
    pen.down()
    pen.goto(250,290)
    pen.goto(-250,290)
    pen.goto(-250,210)
    pen.goto(250,210)
    pen.up()

def draw_the_boudary():                         #draw the boundary
    pen.goto(250,210)
    pen.down()
    pen.goto(250,-290)
    pen.goto(-250,-290)
    pen.goto(-250,210)
    pen.goto(250,210)

def write_the_title():                          # draw the title
    pen.up()
    pen.goto(-230,230)
    pen.write('Contact: ',font=('Arial',14,'normal'))
    pen.goto(-75,230)
    pen.write('Time: ',font=('Arial',14,'normal'))
    pen.goto(52,230)
    pen.write('Motion: ',font=('Arial',14,'normal'))
    pen.up()

def write_the_description():                    #write beginning words
    pen1.goto(-230,50)
    pen1.write(
        '''Welcome to Carlo's game!
        
        You are going to use 4 arrow keys to move the snake
        around the screen, trying to consume all the food items
        before the monster catches you

        Click anywhere to start the game!
        ''',font=('Arial',12,'normal')
    )

def draw_the_carve():                           #draw the carve
    pen.screen.setup(660,740)
    pen.pensize(4)
    draw_the_title()
    draw_the_boudary()
    write_the_title()
    write_the_description()

def write_the_content_1():                          #write contact, motion
    pen2.clear()
    pen2.goto(-140,230)
    pen2.write('{}'.format(g_Contact),font=('Arial',14,'normal'))
    pen2.goto(140,230)
    pen2.write('{}'.format(g_motion),font=('Arial',14,'normal'))

def write_the_content_2():                          # write time  
    if not terminate():
        global g_Time
        pen3.clear()
        pen3.write(f"{g_Time}",font=('Arial',14,'normal'))
        pen3.screen.update()
        head.screen.ontimer(write_the_content_2,1000)
        g_Time = g_Time+1

def initilize_the_monster():
    Monster.fillcolor('purple')
    Monster.screen.tracer(0)
    Monster.up()
    while True:
        x = random.randint(-240,240)
        y = random.randint(-280,200)
        if (x<-140 or x>140) and (y<-180 or y>100):
            Monster.setpos(x,y)
            break
    
def initializer():
    head.screen.title(r"Carlo's snake game")
    initialize_pens()
    initilize_the_monster()
    draw_the_carve()
    initialize_head()
    initialize_tail()
    pen3.write('0',font=('Arial',14,'normal'))
    write_the_content_1()
    pen.screen.update()

#in this part, the functions are intended to control the move of the snake
#the following four functions are to control the moving direction
def right():
    global g_motion
    g_list1.append('a')
    g_motion = 'Right'
    write_the_content_1()
    restart()
       
def left():
    global g_motion
    g_list1.append('b')
    g_motion = 'Left'
    write_the_content_1()
    restart()
      
def up():
    global g_motion
    g_list1.append('c')
    g_motion = 'Up'
    write_the_content_1()
    restart()
    
def down():
    global g_motion
    g_list1.append('d')
    g_motion = 'Down'
    write_the_content_1()
    restart()

#this function is to make a connection to the tap on the keyboard with a name  
def head_dir():
    if g_i ==1:
        head.screen.onkey(right,'Right')
        head.screen.onkey(left,'Left')
        head.screen.onkey(up,'Up')
        head.screen.onkey(down,'Down')

#this function is used to check whether the snake is in the boundary
def is_boundary():
    x,y = head.pos()
    if x<230 and y<190 and x>-230 and y>-270:
        return True
    return False

def collide():
    x,y = head.pos()
    x=round(x)
    y=round(y)
    if x>=240 and g_motion == 'Right':
        return False
    elif y>=190 and g_motion == 'Up' :
        return False
    elif y<=-270 and g_motion == 'Down' :
        return False
    elif x<=-240 and g_motion == 'Left' :
        return False
    return True

#this function is to control the snake's tail's move 
def tail_move():
    if collide():
        x,y=head.pos()
        x=round(x)
        y=round(y)
        tail.goto(x,y)
        stamp_id=tail.stamp()
        g_taillist.append((x,y))
        g_list2.append(stamp_id)
        if len(g_list2)>=g_length:
            tail.clearstamp(g_list2.pop(0))
            del g_taillist[0]

#this function is to make the snake move (mainly head's move)
def snake_move():
    global g_extend
    if not terminate():
        if g_j==0:
            x,y = head.pos()
            x=round(x)
            y=round(y)
            head_dir()
            tail_move()
            dire = g_list1[-1]
            if dire == 'a':
                head.seth(0)
            elif dire == 'b':
                head.seth(180)
            elif dire == 'c':
                head.seth(90)
            elif dire=='d':
                head.seth(270)
            if dire != 'N' : 
                if is_boundary():
                    head.forward(20)
                else:
                    if (x<230 and x>-230) or(y<190 and y>-270):
                        if y>=190 and dire != 'c':
                            head.forward(20)
                        if y<=-270 and dire != 'd':
                            head.forward(20)
                        if x>= 230 and dire != 'a':
                            head.forward(20)
                        if x<=-230 and dire != 'b':
                            head.forward(20)
                    else:
                        if x >230 and y>190 and dire not in 'ac':
                            head.forward(20)
                        if x <-230 and y>190 and dire not in 'bc':
                            head.forward(20)
                        if x >230 and y<-270 and dire not in 'ad':
                            head.forward(20)
                        if x <-230 and y<-270 and dire not in 'bd':
                            head.forward(20)
            g_extend += is_food_eat()
            if g_extend != 0:
                g_extend -= 1
                if len(g_dict_food)==0 and g_extend==0:
                    g_extend+=1
                    g_dict_food[10]='finish'
                velocity=450
            else:    
                velocity=random.randint(220,260)
        else:
            velocity=20
        head.screen.ontimer(snake_move,velocity)
        head.screen.update()

# the following two functions are intended to control the monster's move
#obtain coordinates of monster and head
def obtain_the_coordinates():
    x1,y1 = head.pos()
    x1=round(x1)
    y1=round(y1)
    x2,y2 = Monster.pos()
    x2=round(x2)
    y2=round(y2)
    return x1,y1,x2,y2

#move monster  
def Monster_move():
    global g_Contact
    
    if not terminate():
        x1,y1,x2,y2 = obtain_the_coordinates()
        ran=random.randint(0,1)
        if (ran ==0 and abs(x1-x2)>20)or abs(y1-y2)<20:
            if x1-x2<=-20:
                Monster.seth(180)
                Monster.forward(20)
                Monster.screen.update()
            if x1-x2>=20:
                Monster.seth(0)
                Monster.forward(20)
                Monster.screen.update()
        else:
            if y1-y2<=-20:
                Monster.seth(270)
                Monster.forward(20)
                Monster.screen.update()
            if y1-y2>=20:
                Monster.seth(90)
                Monster.forward(20)
                Monster.screen.update()
        g_list4.clear()

        for x3,y3 in g_taillist:
            if abs(x3-x2)<=20 and abs (y3-y2)<=20:
                g_list4.append(1)
        if 1 in g_list4:
            g_Contact +=1
            write_the_content_1()
            head.screen.update()
    velocity = random.randint(240,450)
    Monster.screen.ontimer(Monster_move,velocity)
 
#the following functions are used for randomly placing the food.
#this function was to obtain 10 coodinates of the food
def randomize_food():
    i=1
    while len(g_dict_food)<9:
        x = 20*random.randint(-11,11)
        y = 20*random.randint(-13,9)
        cor = (x,y)
        if cor != (0,0) and cor not in g_dict_food:
            g_dict_food[cor]=i
            i+=1

#this function is used to place the food in the position and record their number
def place_food():
    pen4.clear()
    for i in g_dict_food.keys():
        x,y = i
        pen4.setpos(x-5,y-5)
        pen4.write(f'{g_dict_food[i]}',font=('Arial',12,'normal'))
    pen4.screen.update()

#this food is to judge whether the food has been consumed. if so, it will help with the speed of snake
def is_food_eat():
    global g_length
    x,y=head.pos()
    x=round(x)
    y=round(y)
    if (x,y) in g_dict_food:
        x=g_dict_food.pop((x,y))
        g_length += x
        place_food()
        return x
    return 0

#this function is to start the game
def start(x,y):
    global g_i,g_k
    if g_i==0:
        global g_motion
        g_i=1
        pen1.clear()
        pause()
        g_motion = 'Paused'
        randomize_food()
        place_food()
        write_the_content_1()
        write_the_content_2()
        snake_move()
        Monster_move()
        
# to check whether the game is at the end
def terminate():
    if g_i==1 and 10 in g_dict_food and g_extend==0 and len(g_list2)==50:
        x,y=head.pos()
        pen5.color('red')
        pen5.goto(x-80,y)
        pen5.screen.update()
        pen5.write('WINNER!!',font=('Arial',12,'normal'))
        return True
    elif g_i==1 and is_catch():
        x,y=head.pos()
        pen5.goto(x-100,y)
        pen5.screen.update()
        pen5.write('Game over!!',font=('Arial',12,'normal'))
        return True
    return False
    
#this function is to check whether the monster catches the head
def is_catch():
    x1,y1=Monster.pos()
    x2,y2=head.pos()
    x1=round(x1)
    x2=round(x2)
    y1=round(y1)
    y2=round(y2)
    if abs(x1-x2)<=20 and abs(y1-y2)<=20:
        return True
    return False

#this function is to pause the move of snake.
def pause():
    global g_j
    global g_motion
    head_dir()
    if g_j ==0:
        g_motion='Paused'
        write_the_content_1()
        g_j=1
    else:
        restart()

#this function is to restart the game from pause
def restart():
    global g_j
    global g_motion
    global g_k
    if g_j==1:
        g_j=0
        g_k=1
        x = g_list1[-1]
        if x == 'a':
            g_motion = 'Right'
        elif x== 'b':
            g_motion = 'Left'
        elif x == 'c':
            g_motion = 'Up'
        elif x=='d':
            g_motion= 'Down'
        write_the_content_1()

if __name__ == '__main__':
    initializer()
    head.screen.onclick(start)
    head.screen.onkey(pause,'space')
    head.screen.listen()
    head.screen.mainloop()
