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
    
move()

while not at_goal():
    if front_is_clear() == False:
        jump()
    else:
        move()
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################