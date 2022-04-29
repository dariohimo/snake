from turtle import Turtle
import random
from playsound import playsound

#creacion del cuerpo de la serpiente

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
#segments[0]
#SEGMENTS  = [0]
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0

class Snake:
    def __init__ (self):
        self.segments = []  #atributo
        
        self.create_snake() #metodo
        self.head = self.segments[0]
        
     
#movimeinto serpiente
    def create_snake(self):
        
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        snake_segment = Turtle("circle")
        snake_segment.color(random.random(), random.random(), random.random()) 
        snake_segment.penup()
        snake_segment.goto(position)    
        self.segments.append(snake_segment)
        
    def extend(self):
       self.add_segment(self.segments[-1].position())
       
       
       
       
    #movimeinto de la serpiente
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1) :
           new_x = self.segments[seg_num -1 ].xcor()
           new_y = self.segments[seg_num -1 ].ycor()
           self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(20)
    #segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            playsound("./sounds/eat.wav")

    def down(self): 
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            playsound("./sounds/eat.wav")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            playsound("./sounds/eat.wav")
        
    def right(self):  
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            playsound("./sounds/eat.wav")


