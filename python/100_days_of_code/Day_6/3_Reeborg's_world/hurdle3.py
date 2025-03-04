def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():    
    # Version 1
    if wall_in_front() == True:
        jump()
    else:
        move()
    # Version 2
    # if front_is_clear() == True:
    #     move()
    # if wall_in_front() == True:
    #     turn_left()
    #     move()
    #     turn_right()
    #     move()
    #     turn_right()
    #     move()
    #     turn_left()
    # continue