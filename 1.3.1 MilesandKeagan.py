import turtle as trtl
import random



# the body list for new bodies









#create turtle for maze
maze_drawer = trtl.Turtle()
maze_drawer.speed(0)    
wall_width = 10
door_width = 10
distance = 5
maze_drawer.ht()

#create turtles for snake
snake_head = trtl.Turtle()
snake_head.shape("triangle")
snake_head.shapesize(.5)
snake_head.penup()

snake_body = trtl.Turtle()
snake_body.shape("circle")
snake_body.shapesize(.5)
snake_body.penup()


#create turtle for collectible
collectible = trtl.Turtle()
collectible.shape("circle")
collectible.color("red")
collectible.shapesize(.5)

body_list = [snake_head, snake_body, new_body]

#functions for the maze
def drawDoor():
    maze_drawer.penup()
    maze_drawer.forward(door_width)
    maze_drawer.pendown()

def drawBarrier():
    maze_drawer.right(90)
    maze_drawer.forward(wall_width*2)
    maze_drawer.backward(wall_width*2)
    maze_drawer.left(90)


for i in range(50):
    if i > 4:
        door = random.randint(door_width, distance - 2 * door_width)
        barrier = random.randint(wall_width, distance - 2 * door_width)

        if (door < barrier):
            maze_drawer.forward(door)
            drawDoor()
            maze_drawer.forward(barrier - door - door_width)
            drawBarrier()
            maze_drawer.forward(distance - barrier)
        else:
            maze_drawer.forward(barrier)
            drawBarrier()
            maze_drawer.forward(door - barrier)
            drawDoor()
            maze_drawer.forward(distance - door - door_width)

        maze_drawer.left(90)
    distance += wall_width

#functions for the snake
def up():
    snake_head.setheading(90)
    snake_head.forward(20)
    move_snake_up()
    # snake_body.goto(snake_head.xcor(), snake_head.ycor() - 20)
    # if statement for head touching collectible
    if (snake_head.distance(collectible.position()) < 10):
        new_body()
        move_collectible()

def down():
    snake_head.setheading(270)
    snake_head.forward(20)
    move_snake_down()
    #snake_body.goto(snake_head.xcor(), snake_head.ycor() + 20)
    if (snake_head.distance(collectible.position()) < 10):
        new_body()
        move_collectible()


def left():
    snake_head.setheading(180)
    snake_head.forward(20)
    move_snake_left()
    #snake_body.goto(snake_head.xcor() + 20, snake_head.ycor())
    if (snake_head.distance(collectible.position()) < 10):
        new_body()
        move_collectible()

def right():
    snake_head.setheading(0)
    snake_head.forward(20)
    move_snake_right()
    #snake_body.goto(snake_head.xcor() - 20, snake_head.ycor())
    if (snake_head.distance(collectible.position()) < 10):
        new_body()
        move_collectible()


# function for random collectible
def move_collectible():
    collectible.ht()
    collectible.penup()
    collectible.goto(random.choice(range(-200, 200, 20)), random.choice(range(-200, 200, 20)))
    collectible.st()



# function creating a new body
def new_body():
    body_new = trtl.Turtle()
    body_new.ht()
    body_new.shape("circle")
    body_new.color("black")
    body_new.shapesize(.5)
    body_new.penup()
    body_list.append(body_new)

    
def move_snake_up():
    # utilizing body list
    for i in range(len(body_list)):
        if (i == 0):
            pass
        else:
            body_list[i].goto(body_list[i - 1].xcor(), body_list[i - 1].ycor() - 20)

def move_snake_down():
    # utilizing body list
    for i in range(len(body_list)):
        if (i == 0):
            pass
        else:
            body_list[i].goto(body_list[i - 1].xcor(), body_list[i - 1].ycor() + 20)            



def move_snake_left():
    # utilizing body list
    for i in range(len(body_list)):
        if (i == 0):
            pass
        else:
            body_list[i].goto(body_list[i - 1].xcor() + 20, body_list[i - 1].ycor())    



def move_snake_right():
    # utilizing body list
    for i in range(len(body_list)):
        if (i == 0):
            pass
        else:
            body_list[i].goto(body_list[i - 1].xcor() - 20, body_list[i - 1].ycor())      






     

#create screen
wn = trtl.Screen()

#keypress bindings
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

#listen
wn.listen()


#mainloop
wn.mainloop()