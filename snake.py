#variables besoin pour score board:
#playerName
#playTime1
#score1

import pygame
import time

TITLE = "Snake"

WIDTH  = 800
HEIGHT = 600


import random
#background
background = pygame.image.load('.\\images\\anebula.jpg')


#player
ship = Actor('rocket_64.png')
ship.x=400
ship.y=300

#apple
apple=Actor('mercurius.png')
apple.width = 64
apple.height = 64

apple.x=random.randint(30,WIDTH-30)
apple.y=random.randint(30,HEIGHT-30)

#other
playerName = str(input("Le nom du joueur: "))

direction = "U"

score = 0

shipSpeed = 5

pause = False

appleTot = 0

shipSpeedP = 5

rminSpeedP = 0

playTime = 0

winStatus = False

minSpeed = -1

gameOver = False

restart = False

scoreWin = False

timer = 0

playTimeStop = 0

gameTime = 0

tauxDeJeux = 4

playTime1 = 0

score1 = 0
#Rest of code -----------------
    
def draw():
    #global variables ------------
    global gameOver
    global score
    global restart
    global shipSpeed
    global minSpeed
    global pause
    global direction
    global playTime
    global playTimeStop
    global tauxDeJeux
    #global variables ------------
    global pause
    global gameOver
    global gameTime
    global score1
    global playTime1
    
    if tauxDeJeux <= 0:
        #code du prof pour envoyer les données ------------------------------------------------------------------------------------------
        gameEndFunt()
    
    if pause == False or gameOver == False:
    
        screen.clear()
        screen.blit(background, (0, 0))
            
        screen.draw.text('Time: ' + str(playTime),(360,30),width=180,lineheight=20, color="Green")
        
        minSpeedChange()
        
        if (gameOver != True):
            scorefunt()
            ship.draw()
            apple.draw()
            speedDraw()
            tauxDeJeuxfont()
            
            
            
            if ship.x >= 800:
                gameOver = True

            elif ship.x <= 0:
                ship.y = 800
                gameOver = True
                    
            elif ship.y >= 590:
                gameOver = True
                    
            elif ship.y <= 0:
                gameOver = True
                
            if score >= 1000000000:
                score = 999999999
                
            if scoreWin == True:
                screen.clear()
                screen.draw.text('You Won!')
            
        
        else:
            screen.clear()
            drawGame()
            playTimeStop = playTime
            
                
            
            if restart == True:
                
                screen.clear()
                createApple()
                ion = "R"
                pause = False
                gameOver = False
                restart = False
                ship.x = 400
                ship.y = 300
                if tauxDeJeux == 3:
                    score1 = score
                if tauxDeJeux == 2 and score > score1:
                    score1 = score
                if tauxDeJeux == 1 and score > score1:
                    score1 = score
                    
                if tauxDeJeux == 3:
                    playTime1 = playTime
                if tauxDeJeux == 2 and playTime > playTime1:
                    playTime1 = playTime
                if tauxDeJeux == 1 and playTime > playTime1:
                    playTime1 = playTime
                    
                score = 0
                shipSpeed = 5
                minSpeed = -1
                playTime = 0
                tauxDeJeux -= 1
                if score >= 1000000000:
                    score = 999999999
                
        if pause == True and gameOver == False:
            screen.draw.text('Paused' ,(275,275),width=180,fontsize=100,lineheight=20, color="Red")

def update(dt):
    global scores
    global circles
    global ship
    global shipSpeed
    global score
    global minSpeed
    global timer
    global pause
    global gameOver
    global playTimeStop
    global tauxDeJeux
        
    if gameOver == False:
        
        timer += dt
        if timer > 1:
            timer = 0
            playTimeFunt()
        
        if direction == "U":
            ship.y -= shipSpeed
        elif direction == "D":
            ship.y += shipSpeed
        elif direction == "L":
            ship.x -= shipSpeed
        elif direction == "R":
            ship.x += shipSpeed
            
        if ship.colliderect(apple):
            apple.x=random.randint(30,WIDTH-30)
            apple.y=random.randint(30,HEIGHT-30)
            
            if shipSpeed == -1:
                score += 2
            elif shipSpeed >= 5:
                score += 1
            elif shipSpeed >= 10:
                score += 2
            elif shipSpeed = 15:
                score += 4
            else:
                score += 1
        
        if shipSpeed < minSpeed:
            shipSpeed = minSpeed
                
        if shipSpeed <= -2:
            shipSpeed = -1
        elif shipSpeed >= 16:
            shipSpeed = 15
    
    if gameOver != True or pause != True:
        gameTime = timer

def on_key_down(key):
    global score
    global direction
    global gameOver
    global shipSpeed
    global restart
    global pause
    global minSpeedP
    global shipSpeedP
    global minSpeed
    global ship
    global gameOver
    global playTimeStop
    global tauxDeJeux
    
    if pause == False or gameOver == False:
        
        if (key == keys.UP):
            direction = "U"
            ship.angle = 0
        elif (key == keys.DOWN):
            direction = "D"
            ship.angle = 180
        elif (key == keys.LEFT):
            direction = "L"
            ship.angle = 90
        elif (key == keys.RIGHT):
            direction = "R"
            ship.angle = 270
            
        elif (key == keys.S):
            gameOver = True
            
        elif (key == keys.KP0):
            shipSpeed = - 1
            
        elif (key == keys.KP1):
            shipSpeed = 0
            
        elif (key == keys.KP2):
            shipSpeed = 5
            
        elif (key == keys.KP3):
            shipSpeed = 10
                
        elif (key == keys.KP4):
            shipSpeed = 15
            
        elif (key == keys.KP5):
            shipSpeed -= 1
        
        elif (key == keys.KP8):
            shipSpeed += 1
            
        elif (key == keys.R):
            if gameOver == True:
                restart = True
            
        elif (key == keys.F9):
            score = 999999999
        
        elif (key == keys.F10):
            tauxDeJeux = 3
            
        elif (key == keys.F11):
            tauxDeJeux = 999999999
            
        elif (key == keys.P):
            pause = not pause
            if pause == True and gameOver == False:
                minSpeedP = minSpeed
                shipSpeedP = shipSpeed
                minSpeed = 0
                shipSpeed = 0
            else:
                minSpeed = minSpeedP
                shipSpeed = shipSpeedP
    
    
def gameEndFunt():
    global score
    global score1
    global playTime1
    global playTime
    screen.draw.text("Score Final: " + str(score1), (275, 275), color="green")
    print("Score Final: " + str(score1))
    print("Meilleur Temp: " + str(playTime1))
    time.sleep(5)
    pygame.quit()

def tauxDeJeuxfont():
    global tauxDeJeux
    if tauxDeJeux == 3:
        screen.draw.text('Jeux restants: ' + str(tauxDeJeux),(30, 580), color="green")
    if tauxDeJeux == 2:
        screen.draw.text('Jeux restants: ' + str(tauxDeJeux),(30, 580), color="orange")
    if tauxDeJeux == 1:
        screen.draw.text('Jeux restants: ' + str(tauxDeJeux),(30, 580), color="orange")
    if tauxDeJeux == 0:
        screen.draw.text('Jeux restants: ' + str(tauxDeJeux),(30, 580), color="red")
def drawGame():
    global minSpeed
    global score
    global playTimeStop
    global tauxDeJeux
    screen.draw.text('GAME OVER',(350,100),width=180,lineheight=5, color="red")
    screen.draw.text('Your score: ' + str(score),(350,200),width=360,lineheight=5)
    screen.draw.text('Your speed: ' + str(shipSpeed),(350,300),width=180,lineheight=5)
    screen.draw.text('Play Time: ' + str(playTime),(350,400),width=180,lineheight=5)
def speedDraw():
    global shipSpeed
    screen.draw.text('Speed: ' + str(shipSpeed),(700,30))
    
def createApple():
    global apple
    apple.x=random.randint(30,WIDTH-30)
    apple.y=random.randint(30,HEIGHT-30)
    
def scorefunt():
    global score
    screen.draw.text('Score: ' + str(score), (35,30))

def minSpeedDraw():
    global minSpeed
    screen.draw.text('Min Speed: ' + str(minSpeed), (35, 570))
      
def playTimeFunt():
    global playTime
    
    playTime += 1
    
def minSpeedChange():
    global minSpeed
    global playTime
    
    if playTime == 20:
        minSpeed = 6
    elif playTime == 30:
        minSpeed = 7
    elif playTime == 40:
        minSpeed = 8
    elif playTime == 50:
        minSpeed = 9
    elif playTime == 60:
        minSpeed = 10
    elif playTime == 70:
        minSpeed = 11
    elif playTime == 80:
        minSpeed = 12
    elif playTime == 90:
        minSpeed = 13
    elif playTime == 100:
        minSpeed = 14
    elif playTime == 110:
        minSpeed = 15
        
    elif playTime == 150:
        minSpeed = 16
    
#Owner: Jan Van de Casteele