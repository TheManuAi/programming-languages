def turn_right():
    turn_left()
    turn_left()
    turn_left()   

# TODO: Improve maze-solving logic when I reach an intermediate level.

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()