from turtle import *
import turtle
import random
import math

#GLOBAL VARIABLES
option_selected = 1 # 1 for Tree and 2 for bird 
pen_color = 'black'  #default
fill_color = 'pink'  #same as backgroud
posx = 0  #Default x-coordinate
posy = 0 #Default y-coordinate


#############Random tree size
def random_scale_factor():
    return round(random.uniform(0.7,1.3), 2)

######### Restore state
def restore_state():
    posx,posy = -330,310 #Restore global variables
    turtle.goto(posx,posy) # goto birds location
    
    pen_color = 'black' #Restore global variable
    turtle.color(pen_color) # Default
    
    if option_selected == 2:
        fill_color = 'purple' #Keep the colors to purple for option 2
        turtle.fillcolor(fill_color)  
    else:
        fill_color = 'pink'
        turtle.fillcolor(fill_color) # default filing color is none

######## Save current state
def save_state(x,y,pen_color,fill_color):
    posx, posy = x,y #set current position of x 
    turtle.color(pen_color) #current turtle color
    turtle.fillcolor(fill_color) #Current
      
#############Draw Rectangle 
def draw_rectangle(centre_x,centre_y,width,height,pen_color,fill_color):
    
    turtle.hideturtle()
    turtle.goto(centre_x,centre_y)
    turtle.left(90)
    turtle.pencolor(pen_color)
    #inside color
    turtle.fillcolor(fill_color)
    #start color filling
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(height) # Height
    turtle.left(90) #position to height
    turtle.forward(width) # width
    turtle.left(90)
    turtle.forward(height)# Height
    turtle.left(90)
    turtle.forward(width/2) # width
    turtle.left(180) # reset postion for next stem
    turtle.end_fill() # Fill the color
    turtle.penup()
    
    # save current values and pos x,y so that triangle can start drawing from this x and y
    save_state(turtle.xcor(),turtle.ycor(),pen_color,fill_color) 

    #cannot use restore because it is using draw_triangle immediately 
    
    
################Draw triangle
def draw_triangle(center_x,center_y,width,height,pen_color,fill_color):
    
    turtle.pendown() # start drawing
    turtle.pencolor(pen_color) #pen color
    turtle.fillcolor(fill_color) #inside color
    turtle.begin_fill() #start color filling
    turtle.forward(width) #width
    #get first coordinate for centroid of triangle
    x1 = turtle.xcor()
    y1 = turtle.ycor()
    turtle.left(120)
    turtle.forward(height) #height sides
    #get second coordinate for centroid of triangle
    x2 = turtle.xcor()
    y2 = turtle.ycor()
    turtle.left(120)
    turtle.forward(height)
    #get 3rd coordinate for centroid of triangle   
    x3 = turtle.xcor()
    y3 = turtle.ycor() 
    turtle.left(120)
    turtle.forward(width)
    turtle.end_fill() #fill color
    turtle.penup() #pen up and calcualte center of current triangle    
    #get center of the triangle
    x = round((x1 + x2 + x3) / 3, 2)
    y = round((y1 + y2 + y3) / 3, 2)
    
    #2nd triangle    
    turtle.goto(x,y)  
    turtle.pendown() 
    turtle.begin_fill()
    turtle.forward(width) #width
    #get first coordinate for centroid of triangle
    x1 = turtle.xcor()
    y1 = turtle.ycor()
    turtle.left(120)
    turtle.forward(height) #height sides
    #get second coordinate for centroid of triangle
    x2 = turtle.xcor()
    y2 = turtle.ycor()
    turtle.left(120)
    turtle.forward(height)
    #get 3rd coordinate for centroid of triangle   
    x3 = turtle.xcor()
    y3 = turtle.ycor() 
    turtle.left(120)
    turtle.forward(width)
    turtle.forward(width)
    turtle.end_fill()
    turtle.penup() #pen up and calcualte center of current triangle
    x = round((x1 + x2 + x3) / 3, 2)
    y = round((y1 + y2 + y3) / 3, 2)
    
    #3rd triangle
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width) #width
    #get first coordinate for centroid of triangle
    x1 = turtle.xcor()
    y1 = turtle.ycor()
    turtle.left(120)
    turtle.forward(height) #height sides
    #get second coordinate for centroid of triangle
    x2 = turtle.xcor()
    y2 = turtle.ycor()
    turtle.left(120)
    turtle.forward(height)
    #get 3rd coordinate for centroid of triangle   
    x3 = turtle.xcor()
    y3 = turtle.ycor() 
    turtle.left(120)
    turtle.forward(width)
    turtle.end_fill()
    turtle.penup()
    
    restore_state() #restore after each draw
    
#### Draw Circle 
def draw_circle(centre_x, centre_y, radius, pen_color, fill_color):
    save_state(centre_x,centre_y,pen_color,fill_color) #Save current state
    
    turtle.hideturtle()
    turtle.goto(centre_x,centre_y) # Go to this location
    turtle.pendown() #Ready to draw
    turtle.pencolor(pen_color) #Drawing lines color
    turtle.begin_fill() #Start filling color 
    turtle.fillcolor(fill_color) # Shape fill color
    turtle.circle(radius) #Draw a circle
    turtle.end_fill()# End filling color
    turtle.penup()  
    
    restore_state() #restore after each draw
    
#### Cartesian distance    
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dist

#### Stamp turtle
def stamp_turtle(centre_x, centre_y, color):
    save_state(centre_x,centre_y,'black',color)
    
    turtle.showturtle()
    turtle.goto(centre_x,centre_y) #Go to clicked location
    turtle.color(color) #change the color of turtle
    turtle.stamp() #Stamp the turtle on given position    
    
    restore_state() #restore after each draw
    
    
