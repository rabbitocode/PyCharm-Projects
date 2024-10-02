from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
steps_moved = 0  # Counter to delay collision detection

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    scoreboard.scores()
    steps_moved += 1  # Increment steps

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail (start checking after some initial moves).
    if steps_moved > 3:  # Start checking for collisions after initial moves
        for segment in snake.all_snakes[1:]:  # Skip the head
            if snake.head.distance(segment) < 8:
                scoreboard.reset()
                snake.reset()

screen.exitonclick()
