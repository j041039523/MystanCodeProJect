"""
File: PotholeFilling.py
Name: Jerry h
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

def main():
    # Written by Jerry
    """
    pre-condition Karel is at the (2,2)
    post-condition Karel is at the (2,7)
    """
    for i in range(3):
        go_in()
        put_99_beeper()
        go_out()



def go_in():
    """
    pre-condition: Karel is at the upper left, facing East
    post-condition: karel is at the pothole,facing South
    """
    move()
    turn_right()
    move()

def put_99():
    """
    Karel will put 99 beepers in the pothole
    """
    put_99_beeper()
def go_out():
    """
    pre-condition: Karel is in the pothole, facing South
    post-condition: karel is at the upper left, facing East
    """
    turn_around()
    move()
    turn_right()
    move()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def put_99_beeper():
    for i in range(99):
        put_beeper()

def turn_around():
    turn_left()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
