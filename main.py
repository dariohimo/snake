from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen() # instanciar el objeto
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("Programate snake")

#quitamos animacion de movimeinto.
screen.tracer(0)


#crear instanciar objeto serpiente

snake = Snake()  #objeto serpiente

#Crear instancia del objeto comida.
food = Food()

#crear objeto tablero de puntos
scoreboard = Scoreboard()

#Movimientos serpiente

screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#screen.onkey(snake.up, "UP")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.2)
    snake.move()
    
    #detectar colision con comida
    
    if snake.head.distance(food) < 15:
       food.refresh()
       scoreboard.increase_score()
       snake.extend()
       
       
    #Detectar colision paredes
    if snake.head.xcor()  > 280 or snake.head.xcor() < -280 or  snake.head.ycor()  > 280 or snake.head.ycor() < -280:
       game_is_on = False
       scoreboard.game_over()
      
    #detectar colision de cola
    for segment in snake.segments:
       if segment == snake.head:      
          pass
       elif snake.head.distance(segment) < 10:
           game_is_on = False
           scoreboard.game_over()
          
    
    


screen.exitonclick()