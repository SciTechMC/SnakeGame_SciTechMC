import pgzrun
import os
import pygame

TITLE = "Snake"

WIDTH  = 802
HEIGHT = 602


import random
import time

#player
snake=Actor('snake.png')
snake.width = 24
snake.height = 24

snake.x=400
snake.y=300

#apple
apple=Actor('apple.png')
apple.width = 25
apple.height = 25

apple.x=random.randint(30,WIDTH-30)
apple.y=random.randint(30,HEIGHT-30)

#other
direction = "R"

score = 0

snakeSpeed = 5

pause = False

appleTot = 0

snakeSpeedP = 5

minSpeedP = 0

playTime = 0

winStatus = False

minSpeed = -1

gameOver = False

restart = False

scoreWin = False

#Rest of code -----------------

def draw():
    #global variables ------------
    global gameOver
    global score
    global restart
    global snakeSpeed
    global minSpeed
    global pause
    global minSpeedP
    global snakeSpeedP
    global direction
    global playTime
    global scoreWin
    #global variables ------------
    
    screen.clear()
    
    # Draw horizontal lines
    for y in range(1, HEIGHT, 25):
        pygame.draw.line(screen.surface, (255, 255, 255), (0, y), (WIDTH, y))
    
    # Draw vertical lines
    for x in range(1, WIDTH, 25):
        pygame.draw.line(screen.surface, (255, 255, 255), (x, 0), (x, HEIGHT))
        

    
    if (gameOver != True):
        scorefunt()
        snake.draw()
        apple.draw()
        speedDraw()
        minSpeedDraw()
        
        if snake.x >= 800:
            gameOver = True

        elif snake.x <= 0:
            snake.y = 800
            gameOver = True
                
        elif snake.y >= 590:
            gameOver = True
                
        elif snake.y <= 0:
            gameOver = True
            
        if score >= 1000000000:
            score = 999999999
            
        if scoreWin == True:
            screen.clear()
            screen.draw.text('You Won!')
#        if score >= 10:
#            minSpeed = 5
#        elif score >= 20:
#            minSpeed = 10
#        elif score >= 60:
#            minSpeed = 15
#        elif score >= 200:
#            scoreWinFunt()

    else:
        screen.clear()
        drawGame()
        
        if restart == True:
            
            screen.clear()
            createApple()
            direction = "R"
            pause = False
            gameOver = False
            restart = False
            snake.x = 400
            snake.y = 300
            score = 0
            snakeSpeed = 5
            minSpeed = -1
            playTime = 0
            
    if pause == True and gameOver == False:
        screen.draw.text('Paused' ,(275,275),width=180,fontsize=100,lineheight=20, color="Red")

def update():
    global scores
    global circles
    global snake
    global snakeSpeed
    global score
    global minSpeed
    
    if direction == "U":
        snake.y -= snakeSpeed
    elif direction == "D":
        snake.y += snakeSpeed
    elif direction == "L":
        snake.x -= snakeSpeed
    elif direction == "R":
        snake.x += snakeSpeed
        
    if snake.colliderect(apple):
        apple.x=random.randint(30,WIDTH-30)
        apple.y=random.randint(30,HEIGHT-30)
        
        if snakeSpeed == -1:
            score += 2
        elif snakeSpeed <= 5:
            score += 1
        elif snakeSpeed <= 10:
            score += 4
        elif snakeSpeed <= 15:
            score += 8
        else:
            score += 1
    
    if snakeSpeed <= minSpeed:
        snakeSpeed = minSpeed
            
    if snakeSpeed <= -2:
        print("reverting to previous value")
        snakeSpeed = -1
    elif snakeSpeed >= 16:
        snakeSpeed = 15
        
#    if score >= 10:
#        minSpeed = 5
#    elif score >= 20:
#        minSpeed = 10
#    elif score >= 60:
#        minSpeed = 15
#    elif score >= 200:
#        scoreWinFunt()

def on_key_down(key):
    global score
    global direction
    global gameOver
    global snakeSpeed
    global restart
    global pause
    global minSpeedP
    global snakeSpeedP
    global minSpeed
    
    
    if (key == keys.UP) and direction != "D":
        direction = "U"
    elif (key == keys.DOWN) and direction != "U":
        direction = "D"
    elif (key == keys.LEFT) and direction != "R":
        direction = "L"
    elif (key == keys.RIGHT) and direction != "L":
        direction = "R"
        
    elif (key == keys.S):
        gameOver = True
        
    elif (key == keys.KP0):
        snakeSpeed = - 1
        
    elif (key == keys.KP1):
        snakeSpeed = 0
        
    elif (key == keys.KP2):
        snakeSpeed = 5
        
    elif (key == keys.KP3):
        snakeSpeed = 10
            
    elif (key == keys.KP4):
        snakeSpeed = 15
        
    elif (key == keys.KP5):
        snakeSpeed -= 1
    
    elif (key == keys.KP8):
        snakeSpeed += 1
        
    elif (key == keys.BACKSPACE):
        if gameOver == True:
            restart = True
        
    elif (key == keys.F9):
        score += 999999999
        
    elif (key == keys.P):
        pause = not pause
        if pause == True and gameOver == False:
            minSpeedP = minSpeed
            snakeSpeedP = snakeSpeed
            minSpeed = 0
            snakeSpeed = 0
        else:
            minSpeed = minSpeedP
            snakeSpeed = snakeSpeedP


def drawGame():
    global minSpeed
    global score
    screen.draw.text('GAME OVER',(350,200),width=180,lineheight=5)
    screen.draw.text('Your score: ' + str(score),(350,300),width=360,lineheight=5)
    screen.draw.text('Your speed: ' + str(snakeSpeed),(350,400),width=180,lineheight=5)
def speedDraw():
    global snakeSpeed
    screen.draw.text(str(snakeSpeed),(760,30))
    
def createApple():
    global apple
    apple.x=random.randint(30,WIDTH-30)
    apple.y=random.randint(30,HEIGHT-30)
    
def scorefunt():
    global score
    screen.draw.text(str(score), (35,30))

def scoreWinFunt():
    scoreWin = True

def minSpeedDraw():
    global minSpeed
    screen.draw.text(str(minSpeed), (35, 580))
        
#    if pause == False:
#        clock.schedule_interval(playTimefunt, 1.0)
#    
#        clock.schedule_interval(minSpeedfunt, 15.0)
#        if minSpeed <= 5:
#            screen.draw.text('Minimum Speed: ' + str(minSpeed),(35,570),width=180,lineheight=20, color="Green")
#        elif minSpeed <= 10:
#            screen.draw.text('Minimum Speed: ' + str(minSpeed),(35,570),width=180,lineheight=20, color="Orange")
#        elif minSpeed <= 15:
#            screen.draw.text('Minimum Speed: ' + str(minSpeed),(35,570),width=180,lineheight=20, color="Red")
    

#def playTimefunt():
#    global winStatus
#    global playTime
#    
#    clock.schedule_interval(playTimefunt, 1.0)
#    screen.draw.text('Time: ' + str(playTime),(350,30),width=180,lineheight=20, color="Green")
#    print(playTime)
#    
#    if playTime >= 3600:
#        winStatus = True
#    elif playTime < 3600:
#        playTime += 1
    
#    clock.unschedule(playTimefunt)
#def minSpeedfunt():
#    global minSpeed
#    if minSpeed >= 15:
#        minSpeed = 15
#    else:
#        minSpeed += 1
    
#   clock.unschedule(minSpeedfunt)