import pygame
import random
from math import *
from sys import exit


start = False
first = True
speedx = []
speedy = []
speed = 5
number = 7
location = []
size = 35
rect = []
circl = []
color = []



def move(rect, scre):
    global speed
    tolrance = 4 
    for i in range(len(rect)):
        for j in range(len(rect)):
            if rect[i].colliderect(rect[j]) and i != j:
                if speedx[i] + speedx[j] == 0:
                    speedx[i] *= -1
                    speedx[j] *= -1
                if speedy[i] + speedy[j] == 0:
                    speedy[i] *= -1
                    speedy[j] *= -1
                
                rect[i].x += speedx[i]
                rect[i].y += speedy[i]
                rect[j].x += speedx[j]
                rect[j].y += speedy[j]
                print (speedx, speed)
                


    for i in range(len(rect)):
        if start:
            rect[i].x += speedx[i]
            rect[i].y += speedy[i]
            if rect[i].left <= 0:
                speedx[i] *= -1
                rect[i].left = 0
            if rect[i].right >= scre.get_size()[0]:
                speedx[i] *= -1
                rect[i].right = scre.get_size()[0]
            if rect[i].top <= 0:
                speedy[i] *= -1
                rect[i].top = 0
            if rect[i].bottom >= scre.get_size()[1]:
                speedy[i] *= -1
                rect[i].bottom = scre.get_size()[1]



def ball(num):
    global screen
    global first
    again = False
    loop = True
    for i in range(num):
        if first:
            if i == 0:
                x = random.randint(0,screen.get_size()[0]-100)
                y = random.randint(0, screen.get_size()[1]-100)
                location.append((x,y))
    
            else:
                while(loop):
                    x = random.randint(0,screen.get_size()[0]-100)
                    y = random.randint(0, screen.get_size()[1]-100)
                    for r in location:
                        D = sqrt(pow(x - r[0], 2) + pow(y - r[1], 2))
                        if D <= size:
                            again = True
                            print(again, D, x, y, r,i)
                    if again == True: loop =True
                    elif again == False: loop= False
                location.append((x,y))
            loop=True
            color.append(((random.randint(0,250),random.randint(0,250),random.randint(0,250))))
            rect.append(pygame.Rect(location[i], (size, size)))
            pygame.draw.ellipse(screen, color[i], rect[i])
            speedx.append(random.choice([speed, -speed]))
            speedy.append(random.choice([speed, -speed]))
        else:
            pygame.draw.ellipse(screen, color[i], rect[i])
            
    first = False
    


pygame.init()


screen = pygame.display.set_mode((1360, 700))
pygame.display.set_caption('test')
clock = pygame.time.Clock()

while(True):
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start:start=False
                else: start=True
                
    ball(number)
    move(rect, screen)           
    

    pygame.display.update()
    clock.tick(60)