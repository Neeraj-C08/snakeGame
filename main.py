import pygame
import time
import os
import random

pygame.init()

screenWidth = 800
screenHeight = 800
running = True

yVel = 0
xVel = 0
score = 0
randCoordx = (int)(random.random()*801)
randCoordy = (int)(random.random()*801)

gameOver = pygame.image.load("assets/images/image.png")
screen = pygame.display.set_mode((screenWidth,screenHeight))

mychar = pygame.Rect(400, 400, 50, 50)
myFood = pygame.Rect(600, 400, 25,25)
myList = []
myList.append(mychar)

pygame.draw.rect(screen,(0,255,0),mychar)
pygame.draw.rect(screen,(255,0,0),myFood)

clock = pygame.time.Clock()

#Game Loop


while running:

    clock.tick(30)

    

    prev_positions = [segment.copy() for segment in myList]

    


    if mychar.y < 800 and mychar.y > 0 and mychar.x < 800 and mychar.x > 0:
        myList[0].x += xVel
        myList[0].y += yVel
    else:
            screen.blit(gameOver,(0, 0))
            pygame.display.update()
            time.sleep(3)
            running = False

    for i in range(1, len(myList)):
        myList[i].x = prev_positions[i-1].x - 50
        myList[i].y = prev_positions[i-1].y 
        


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yVel = -5
                xVel = 0
            elif event.key == pygame.K_s:
                yVel = 5
                xVel = 0
            elif event.key == pygame.K_a:
                xVel = -5
                yVel = 0
            elif event.key == pygame.K_d:
                xVel = 5
                yVel = 0
            elif event.key == pygame.K_ESCAPE:
                running = False
            
    """

    keys = pygame.key.get_pressed()

    

    if keys[pygame.K_w]:
        mychar.y -= 1
    elif keys[pygame.K_s]:
        mychar.y += 1
    elif keys[pygame.K_a]:
        mychar.x -= 1
    elif keys[pygame.K_d]:
        mychar.x += 1
    if keys[pygame.K_ESCAPE]:
        running = False
    """

    if mychar.colliderect(myFood):
        score += 1
        myFood = pygame.Rect((int)(random.random()*801), (int)(random.random()*801), 25,25)
        if yVel == 0:
            myList.append(pygame.Rect(myList[-1].x-50, myList[-1].y, 50, 50))
        else:
            myList.append(pygame.Rect(myList[-1].x, myList[-1].y-50, 50, 50))

        

    

    screen.fill((0, 0, 0))  # Clear screen each frame

    for i in myList:
        pygame.draw.rect(screen, (0, 255, 0), i)  # Draw rectangle at updated position

    pygame.draw.rect(screen,(255,0,0),myFood)

    pygame.display.update()

print(score)

    




    