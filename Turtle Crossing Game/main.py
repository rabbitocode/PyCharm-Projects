import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
car_manager = CarManager()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)





screen.onkey(player.MoveUP, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    scoreboard.Scores()

    car_manager.create_car()
    car_manager.move_cars()


    # Detects if player has reac-ed the end line
    if player.ycor() > player.FINISH_LINE_Y:
        player.LevelUp()
        scoreboard.UpdateScore()


    # Detects if player has collided with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.GameOver()
            game_is_on = False


screen.exitonclick()