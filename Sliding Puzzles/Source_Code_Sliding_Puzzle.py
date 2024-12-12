import random
#parameter is the dimension of the program. this function is aimmed at generate two well-organized lists
def generate_dimensional_list(p_dimension):
    global g_list1
    global g_list2
    g_list1 = []
    g_list2 = []
    for i in range(1,p_dimension**2):
       g_list1.append(i)
       g_list2.append(i)
    g_list1.append('')     #/*list1: generate a immutable list for operations during the following process
    g_list2.append('')     #list2: generate a list of original number for final test

#This function is aimmed to move the blank space upwards
def up_move(p_dimension):
    space = g_list1.index('')
    if space >= p_dimension:                    #only space not at the bottom can move
        g_list1[space]= g_list1[space-p_dimension]
        g_list1[space-p_dimension] = ''
    else:
        print('you cannot go down')

#This function is aimmed to move the blank space downwards
def right_move(p_dimension):
    space = g_list1.index('')
    if (space+1) % p_dimension !=0:               #only space not at the right can move
        g_list1[space] = g_list1[space+1]
        g_list1[space+1] = ''
    else:
        print('you cannot go to the left')

##This function is aimmed to move the blank space leftwards
def left_move(p_dimension):
    space = g_list1.index('')
    if space % p_dimension !=0:                    #only space not at the left can move
        g_list1[space] = g_list1[space-1]
        g_list1[space-1] = ''
    else:
        print('you cannot go to the right')

##This function is aimmed to move the blank space downwards
def down_move(p_dimension):
    space = g_list1.index('')
    if (p_dimension**2-p_dimension) > space:         #only space not at the bottom can move
        g_list1[space] = g_list1[space+p_dimension]
        g_list1[space+p_dimension] = ''
    else:
        print('you cannot go up')

#This function is to obtain a randomized function
def generate_a_random_list(p_dimension):
    step = 20000
    for _ in range(step):
        space = g_list1.index('')
        ran = random.randint(1,4)              # generate a random number to randomly move the blank
        if ran ==1 and space >= p_dimension:     # up points cannot move up
            up_move(p_dimension)
        elif ran ==2 and (p_dimension**2-p_dimension) > space:   #bottom points cannot move down
            down_move(p_dimension)
        elif ran == 3 and (space+1) % p_dimension !=0:     # right points cannot move right
            right_move(p_dimension)
        elif ran == 4 and space % p_dimension !=0:       #left points cannot move left
            left_move(p_dimension)
    return g_list1

#This function is to print the puzzle out
def generate_a_puzzle(p_dimension):
    for i in range(1,len(g_list1)+1):
        if i % p_dimension !=0:
            print(g_list1[i-1],end='\t')     #each line the number of elements is dimension
        else:
            print(g_list1[i-1])

#This function is to generate a statement for the space to move
def input_statement(p_left,p_right,p_up,p_down,p_dimension):
    space = g_list1.index('')
    s='Enter your move '
    if (space+1)% p_dimension != 0:                 #space not at right
        s += 'left-{},'.format(p_left)
    if space % p_dimension != 0:                    #space not at left
        s += 'right-{},'.format(p_right)
    if  (p_dimension**2-p_dimension) > space:        #space not at bottom 
        s += 'up-{},'.format(p_up)    
    if  space >= p_dimension:                        #space not at top
        s += 'down-{},'.format(p_down)       
    s += '>'
    return s                                         # s can tell where the space is 

#This function is to interact with the users, making them input the key
def input_the_choice(p_left,p_right,p_up,p_down,p_dimension):
    while True:
        state = input_statement(p_left,p_right,p_up,p_down,p_dimension)   
        choice = input(state)                       #make the user to input a direction
        if choice in [p_left,p_right,p_up,p_down]:
            return choice                            #check whether the user is correctly input
        else:
            print('invalid choice! choose again')
            generate_a_puzzle(p_dimension)

#This function is to conduct a move, based on the key the user inputs.
def one_move(p_left,p_right,p_up,p_down,p_dimension):
    move = input_the_choice(p_left,p_right,p_up,p_down,p_dimension)
    if move == p_left:
        right_move(p_dimension)
    elif move == p_right:
        left_move(p_dimension)
    elif move == p_up:
        down_move(p_dimension)
    elif move == p_down:
        up_move(p_dimension)                 #create a move function for the number near the space to move

#this function is to repeat the moves, until the user succeed in the game!
def play(p_left,p_right,p_up,p_down,p_dimension):
    i=0                                   #count the moving times
    while True:
        one_move(p_left,p_right,p_up,p_down,p_dimension)
        if g_list1 == g_list2:                   #check whether return to the initial condition
            generate_a_puzzle(p_dimension)
            print('congratulation!','your total moves are: ',i+1)
            break
        generate_a_puzzle(p_dimension)
        i+=1

#This function is to obtain the dimension from the user
def obtain_the_dimension():
    while True:
        try:
            dimension = float(input('Please enter an integer from 3 to 10 >'))
            l = [3,4,5,6,7,8,9,10]
            if dimension%1 == 0 and dimension in l:
                dimension = int(dimension)
                return dimension
            else:
                print('your dimension is not an integer from 3 to 10!')
        except:
            print('Your input for dimension is invalid! try again!')

#This function is to generate four different characters for keys
def obtain_the_keys():
    while True:
        try:
            left,right,up,down = input(r'please enter 4 characters stand for left\right\up\down >').replace(' ','')
            l1 = [left,right,up,down]
            l2 = list(set(l1))      #to eliminate the same element
            if len(l2)==4:
                return left,right,up,down
            else:
                print('You cannot input same characters')
        except:
            print('you can only input 4 characters')


s = '''Welcome to Carlo's game!
In this game, you are required to input the dimension of the Sliding Puzzle (3~10)
and input four different characters for four moving directions (space is not allowed.)
The system will provide you with a table containing a space and different numbers. 
You can input letters for your moving direction (the adjacent tile moves)
Until all number appear sequentially,ordered from left to right, top to bottom
'''
print(s)
p_dimension = obtain_the_dimension()
p_left,p_right,p_up,p_down=obtain_the_keys()
while True:                    # make the program can be repeatedly conducted
    generate_dimensional_list(p_dimension)   
    list1 = generate_a_random_list(p_dimension)
    generate_a_puzzle(p_dimension)
    play(p_left,p_right,p_up,p_down,p_dimension)       
    ans = input('enter \'n\' to start a new game or other buttons to quit: ')   #choose whether to repeat
    if ans == 'n':
        continue               #start a new game
    else:                      #input other bottons to end the game
        break
