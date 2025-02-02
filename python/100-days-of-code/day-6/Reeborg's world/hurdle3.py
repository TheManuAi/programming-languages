def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():  
    if front_is_clear() == True:
        move()
    if wall_in_front() == True:
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
    continue    