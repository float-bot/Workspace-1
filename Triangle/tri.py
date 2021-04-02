#Made by jglue, out of boredom...
import pygame as pg
import random
import time
pg.init()

(width,height) = (500,350)
screen = pg.display.set_mode((width,height))
running = True
white = (255,255,255)
screen.fill(white)
blue = (100,100,255)
green = (25,255,25)
red = (255,0,0)
dice = 1
x = random.randint(150,350)
y = random.randint(150,350)
# Need to add a background color change here. make it like white or something...

def draw_point(x,y,color):
    s=pg.Surface((1,1))
    s.fill(color)
    r = s.get_rect()
    r.x = x
    r.y = y
    screen.blit(s,r)

def start_point(x,y,color):
    s=pg.Surface((3,3))
    s.fill(color)
    r = s.get_rect()
    r.x = x
    r.y = y
    screen.blit(s,r)

def next_jump(x,y,point):
    if point == 1: # This roll relates to the bottom left point(50,310).
        x = (50 + x) / 2
        y = (310 + y) / 2
        draw_point(x, y, green)
        return x, y
    if point == 2: # This roll relates to the bottom right point(450,310).
        x = (450 + x) / 2
        y = (310 + y) / 2
        draw_point(x, y, red)
        return(x, y)
    if point == 3: # This roll relates to the top middle point(250,10).
        x = (250 + x) / 2
        y = (10 + y) / 2
        draw_point(x, y, blue)
        return(x, y)
    
        
draw_point(x, y, blue)
while running < 5000:
    if running > 4997:
        time.sleep(5)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #if event.type == pg.KEYDOWN:
    point=random.randint(1,3) 
    x,y = next_jump(x,y,point)
    print(x,y)
    print("Rolled a:",point)
    
#If you adjust these points  \/\/\/\/   make sure to adjust the new_x and new_y positions up at points 1,2, and 3 under next_jump.
    start_point(250,10,'white') # Top point.
    start_point(50, 310, 'white') # Bottom left point.
    start_point(450, 310, 'white') # Bottom right point.

    pg.display.update()
    pg.display.flip()

    running += 1
    print("count:",running)

    if running == 5000:
        print("Preparing for a long pause.")
        time.sleep(5)