# turn_left and move() functions are already defined in the Reeborg's world website 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
time = 6
while time > 0:
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    time -= 1