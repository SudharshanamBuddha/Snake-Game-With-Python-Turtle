from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Old Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
food = Food()
snake = Snake()
screen.listen()
screen.onkey(snake.Up, 'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Left, 'Left')
screen.onkey(snake.Right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()
        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            game_is_on = False
            snake.reset()
            scoreboard.game_over()
screen.exitonclick()
