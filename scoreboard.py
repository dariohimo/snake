from turtle import Turtle
from playsound import playsound

ALIGN = "center"

FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
   
   def __init__(self):     #creacion tablero de puntos.
       super().__init__()  #metodos acciones
       self.score = 0   #atributos c
       self.goto(0, 270)
       self.color("Red")
       self.update_score()
       self.update_score()
       self.hideturtle()
       
   def update_score(self):
      self.clear() 
      self.write(f"Score: {self.score}", font=FONT, align=ALIGN)
      self.penup()
      
   def increase_score(self):
       self.clear()
       self.score += 1
       self.update_score() 
       
   def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over !! {self.score}", font=FONT, align=ALIGN)
        playsound("./sounds/over.wav")
        
  
        
        
    
        
    
   