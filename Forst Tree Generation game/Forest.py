from turtle import *
import turtle
import random
import math
#importing the file
import utilities as ut

############### Setup Screen
turtle.bgcolor('pink')
turtle.title("Welcome to Forest Drawing!")
turtle.setup (800,700, startx=0, starty=0)  # fudge factors due to window borders & title bar

#GLOBAL VARIABLES
HEIGHT = 110 # Tree Height
WIDTH = 55 # Tree Width
HEIGHT_STEM = 80 #STEM (RECTANGLE) HEIGHT
WIDTH_STEM = 15 #STEM WIDTH
movement = 8 #movement through arrow
new_tilt_value = 0 # Tilt angle changes by 10 at each key press

############ Coordinates of mouse click
def handle_click(x, y):
    global option_selected
    print(x,y)
    # select tree option 
    if ut.distance(145,310,x,y) <= 15:
        select_options(145.0,310.0)
        ut.option_selected = 1
        ut.draw_circle(230,310.0,10,'black','pink')
    #select bird option
    if ut.distance(230,310,x,y) <= 15:
        select_options(230,310)
        ut.option_selected = 2
        ut.draw_circle(145.0,310.0,10,'black','pink') # Unselect Tree option
        create_bird()
    # If option 1 is select then draw tree
    if y < 300 and y > -320 and x < 340 and x > -350:
        if ut.option_selected == 1:
            factor = ut.random_scale_factor() #Get a new scale factor at each click drawing
            ut.draw_rectangle(x,y,WIDTH_STEM*factor,HEIGHT_STEM*factor,'brown','brown') #Draw STEM
            ut.draw_triangle(ut.posx,ut.posy,WIDTH*factor,HEIGHT*factor,'green','green')
        # If option 2 is selected draw Bird     
        elif ut.option_selected == 2:
            ut.stamp_turtle(x,y,'purple')



#### Create Circle options   
def create_options():
    turtle.hideturtle()
    turtle.penup()
    #Tree option
    turtle.speed(1000)
    turtle.goto(145.0,310.0)
    turtle.pendown()
    turtle.circle(10,)
    turtle.penup()
    turtle.forward(15)
    turtle.write('Tree',font=('Arial',12,'bold'))
    
    # Bird Option
    turtle.goto(230.0,310.0)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.forward(15)
    turtle.write('Bird',font=('Arial',12,'bold'))


######## Handle bird
def right_keypress():
    global new_tilt_value 
    new_tilt_value = new_tilt_value - movement
    turtle.tiltangle(new_tilt_value)# change angle anti-clockwise  
def left_keypress():
    global new_tilt_value 
    new_tilt_value = new_tilt_value + movement
    turtle.tiltangle(new_tilt_value) # change angle clockwise    

####### Create Bird  
def create_bird():
    turtle.goto(-330, 310) #Go to top left
    turtle.register_shape('bird',((-22,-39),(-20,-7),(-7,3),(-11,7),(-12,9),(-11,10),(-9,10),(-3,7),(10,24),(30,16),(13,18),(4,0),(14,-6),(6,-13),(0,-4),(-14,-13),(-22,-39)))
    turtle.shape('bird') #register shape
    turtle.color('purple')
    turtle.showturtle() # show turtle
    turtle.listen()
    turtle.onkeypress(left_keypress, 'Left')
    turtle.onkeypress(right_keypress,'Right')

######## Choose option
def select_options(x,y):
    ut.draw_circle(x,y,10,'black','green')

####### Due to my screensize i haven't selected 700X700
def rectangle_boundary(): 
    turtle.goto(-350,300)
    turtle.pendown()
    turtle.forward(690)
    turtle.right(90)
    turtle.forward(620)
    turtle.right(90)
    turtle.forward(690)
    turtle.right(90)
    turtle.forward(620)
    turtle.right(90)
    turtle.penup()
    # turtle.goto(-330, 310)
    
    
def main():   
    turtle.speed(1000)
    create_options() # create 2 options
    select_options(145.0,310.0)# Select tree option by default
    option_selected = 0 #Change selected option to tree
    rectangle_boundary() # Draw the boundary for clicks
    turtle.onscreenclick(handle_click) # Listen for further events



main()
turtle.done()