from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    #collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #collision with wall
    x_cor = snake.segments[0].xcor()
    y_cor = snake.segments[0].ycor()
    if x_cor > 280 or x_cor < -280 or y_cor > 280 or y_cor < -280:
        scoreboard.game_over()
        snake.reset()
    
    #collision with self
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            snake.reset()
            scoreboard.game_over()

screen.exitonclick()

