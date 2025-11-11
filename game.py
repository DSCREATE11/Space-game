"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
---------------------------------------------------IMPORTING LIBRARIES--------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""


import pygame.camera
import pygame.font
import pygame
import sys
import keyboard
import os
import tkinter as tk



"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
---------------------------------------------------INITIALIZATION-------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""


pygame.camera.init()
pygame.font.init()
pygame.init()

BROWN=(165,42,42)

pygame.font.init()

font1 = pygame.font.Font("Dashhorizon-eZ5wg.otf",58)
font2 = pygame.font.Font("Super Space.otf",80)
font3 = pygame.font.Font("Holla Weekend.otf",100)
font4 = pygame.font.Font("WolfalconRegular-RpjW3.ttf",70)
font5 = pygame.font.Font("FastHand-lgBMV.ttf",120)

pygame.mixer.init()
bg_sound = pygame.mixer.Sound("bg.mp3")


text=font2.render("V/S", True, (255,255,255), (0,0,0))
Play=font1.render("Press C to continue.........", True, (255,255,255),(0,0,255))

covertext=font5.render("SPACE WARS", True, (255,0,0))

mush=pygame.image.load("mush.png")
mush=pygame.transform.scale(mush,(200,250))

img2=pygame.image.load("mship1.png")

img1=pygame.image.load("sps1.png")


Switch=False

flag=1

cameras = pygame.camera.list_cameras()

if not cameras:
    print("No camera detected! Skipping webcam capture.")
    webcam = None
else:
    print("Using camera:", cameras[0])
    webcam = pygame.camera.Camera(cameras[0])


"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
-----------------------------------------------------FUNCTIONS----------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""
   
def oncam():
    webcam.start()
    img = webcam.get_image()
    a=pygame.transform.scale(img,(900,500))
    WIDTH = 900
    HEIGHT = 500
    screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
    return(a,screen)
    

def playerone(flag,ll):
    a,screen=oncam()
    while True :
        pygame.display.set_caption(ll[0])
        if flag==0:
          break
        for e in pygame.event.get() :
          if e.type == pygame.QUIT :
            flag=0
          if keyboard.is_pressed('c'):
            pygame.image.save(a,str(ll[0])+'.jpg')
            flag=0
        # draw frame
        screen.blit(a, (0,0))
        pygame.display.flip()
        # grab next frame    
        img = webcam.get_image()
        a=pygame.transform.scale(img,(900,500))
    pygame.quit()


def playertwo(flag,ll):
    a,screen=oncam()
    pygame.display.set_caption(ll[1])
    while True :
        if flag==0:
          break
        for e in pygame.event.get() :
          if e.type == pygame.QUIT :
            flag=0
          if keyboard.is_pressed('c'):
            pygame.image.save(a,str(ll[1])+'.jpg')
            flag=0
        screen.blit(a, (0,0))
        pygame.display.flip() 
        img = webcam.get_image()
        a=pygame.transform.scale(img,(900,500))
    pygame.quit()


def loadplayers(ll):
    player1=pygame.image.load(str(ll[0])+'.jpg')
    player1=pygame.transform.scale(player1,(400,200))
    player2=pygame.image.load(str(ll[1])+'.jpg')
    player2=pygame.transform.scale(player2,(400,200))
    return(player1,player2)

"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
---------------------------------------------------HOME WINDOW PROGRAM--------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""


screen = pygame.display.set_mode((1200,500))
screen.fill((0,0,0))


sur=pygame.Surface((1200,500))
sur=sur.convert_alpha()
sur.fill((0,0,0,0))
ground=pygame.draw.ellipse(sur,(0,0,255),(0,0,1200,500),1000)

CLD1_X=50
CLD2_X=1000

img1=pygame.transform.scale(img1,(180,150))
cld1=pygame.surface.Surface((150,400))


img2=pygame.transform.rotate((pygame.transform.scale(img2,(150,200))),270)
cld2=pygame.surface.Surface((150,400))


sun1=pygame.Surface((100,100))
sun1=sun1.convert_alpha()
sun1.fill((0,0,0,0))
sun=pygame.draw.ellipse(sun1,(255,140,0),(0,0,100,100))


button_x=390
button_y=430
play=pygame.Surface((Play.get_width(),Play.get_height()))
play.fill((0,255,0))


vel=3


while True:

    if keyboard.is_pressed('c'):
       break


    bg_sound.play()

    screen.blit(covertext,(55,32))

    screen.blit(sun1,(1000,30))
    screen.blit(cld1,(CLD1_X,160))
    screen.blit(cld2,(CLD2_X,200))


    screen.blit(sur,(0,360))
    
    screen.blit(play,(button_x,button_y))
    screen.blit(Play,(button_x,button_y))

    cld1.blit(img1,(0,0))
    cld2.blit(img2,(0,0))

    
    CLD1_X+=vel
    CLD2_X+=vel

    if CLD1_X>1200:
         CLD1_X=-200
    if CLD2_X>1200:
         CLD2_X=-200

    
    pygame.display.flip()
    
    pygame.display.update()


pygame.quit()

"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
---------------------------------------------PLAYER DATA INPUT PROGRAM--------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""

def getdata():
     global ll
     ll=[]
     pl1=name1.get()
     pl2=name2.get()
     tk.Tk.destroy(window)
     ll.append(pl1)
     ll.append(pl2)

ll=[]    
        
window=tk.Tk()
window.title("Player Data Input")
   
frame=tk.Frame(window)
frame.pack()

player1=tk.LabelFrame(frame,text="Player 1")
player1.grid(row=0,column=0)

lname1=tk.Label(player1,text="Please enter your name : ")
lname1.grid(row=0,column=1,padx=20,pady=10,sticky='news')

name1=tk.Entry(player1)
name1.grid(row=1,column=1,padx=20,pady=10,sticky='news')

player2=tk.LabelFrame(frame,text="Player 2")
player2.grid(row=2,column=0)

lname2=tk.Label(player2,text="Please enter your name : ")
lname2.grid(row=0,column=1,padx=20,pady=10,sticky='news')

name2=tk.Entry(player2)
name2.grid(row=3,column=1,padx=20,pady=10,sticky='news')


button=tk.Button(frame,text="Continue",command=getdata)
button.grid(row=3,column=0,padx=20,pady=10,sticky='news')

window.mainloop()

"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------SUB MAIN PROGRAM--------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""


playerone(1,ll)

playertwo(1,ll)

player1,player2=loadplayers(ll)

screen = pygame.display.set_mode((1200,600))
screen.fill((0,0,0))

pygame.font.init()


font1 = pygame.font.Font("Dashhorizon-eZ5wg.otf",80)
font2 = pygame.font.Font("Super Space.otf",80)
font3 = pygame.font.Font("Holla Weekend.otf",100)
font4 = pygame.font.Font("WolfalconRegular-RpjW3.ttf",70)
font5 = pygame.font.Font("FastHand-lgBMV.ttf",80)
sfont1=pygame.font.Font("Dashhorizon-eZ5wg.otf",25)

pn1=font1.render(str(ll[0]),True,(0,0,0),(255,255,255))
pn2=font1.render(str(ll[1]),True,(0,0,0),(255,255,255))
pn1s=sfont1.render(str(ll[0]),True,(0,0,0),(255,255,255))
pn2s=sfont1.render(str(ll[1]),True,(0,0,0),(255,255,255))

sur2=pygame.Surface((300,300))
sur2=sur2.convert_alpha()
sur2.fill((0,0,0,0))
ground2=pygame.draw.ellipse(sur2,(0,0,255),(0,0,300,300),1000)

sur1=pygame.Surface((1200,180))
sur1=sur1.convert_alpha()
sur1.fill((0,0,0,0))
ground1=pygame.draw.ellipse(sur1,(0,0,255),(0,0,1200,180),1000)

countdown_duration = 5
remaining_time = countdown_duration

COUNTDOWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COUNTDOWN_EVENT, 1000)

pygame.mixer.init()
countdown_sound = pygame.mixer.Sound("sound.mp3")


while True:

    for event in pygame.event.get():
        if event.type == COUNTDOWN_EVENT:
            remaining_time = max(-1, remaining_time - 1)        
    if keyboard.is_pressed('q'):
        break

    if remaining_time == 3:
        countdown_sound.play()
    
    screen.blit(sur2,(450,-150))
    screen.blit(sur1,(0,520))

    if remaining_time >0:
        countdown_text = font5.render(f"{remaining_time}", True, (0, 0, 0))
        screen.blit(countdown_text, (565,20))
    if remaining_time == 0:
        countdown_text = font1.render("FIGHT!", True, (0, 0, 0))
        screen.blit(countdown_text, (525,30))

    screen.blit(text,(515,220))
    screen.blit(player1,(40,190))
    screen.blit(pn1,(40,390))
    screen.blit(player2,(750,190))
    screen.blit(pn2,(750,390))
        
    if remaining_time == -1:
        break

    pygame.display.flip()

pygame.quit()



"""---------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------MAIN PROGRAM--------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
------------------------------------------------------------------------------------------------------------------------|
----------------------------------------------------------------------------------------------------------------------"""

import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_FIRE_SOUND = pygame.mixer.Sound('blaster-2-81267.mp3')
BULLET_HIT_SOUND = pygame.mixer.Sound('mixkit-arcade-mechanical-bling-210.wav')
BG_SOUND = pygame.mixer.Sound("cyberpunk-171563.mp3")

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
PLAYER_FONT = pygame.font.SysFont('Arial', 30)

FPS = 60
VEL = 10
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 100, 80

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

img2=pygame.image.load("mship1.png")

img1=pygame.image.load("sps1.png")

bgi=pygame.image.load("bground.png")

img1=pygame.transform.scale(img1,(180,150))

img2=pygame.transform.rotate((pygame.transform.scale(img2,(150,200))),270)


YELLOW_SPACESHIP_IMAGE =pygame.transform.scale(img1,(120,90))
YELLOW_SPACESHIP=pygame.Surface((120,90),pygame.SRCALPHA)
YELLOW_SPACESHIP.fill((0,0,0,0))
YELLOW_SPACESHIP.blit(YELLOW_SPACESHIP_IMAGE,(0,0))

RED_SPACESHIP_IMAGE=pygame.transform.scale(pygame.transform.rotate(img2,180),(120,90))
RED_SPACESHIP=pygame.Surface((120,90),pygame.SRCALPHA)
RED_SPACESHIP.fill((0,0,0,0))
RED_SPACESHIP.blit(RED_SPACESHIP_IMAGE,(0,0))



def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    # Scale background to match window size dynamically
    scaled_bg = pygame.transform.scale(bgi, (WIDTH, HEIGHT))
    WIN.blit(scaled_bg, (0, 0))

    pygame.draw.rect(WIN, WHITE, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    player1_text=PLAYER_FONT.render(str(ll[0]),1,WHITE)
    player2_text=PLAYER_FONT.render(str(ll[1]),1,WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(player1_text,(10, 450))
    WIN.blit(player2_text,(WIDTH - red_health_text.get_width() + 50, 450))
    

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        a="redbullet"+str(red_bullets.index(bullet))
        a=pygame.Surface((10,5))
        pygame.draw.rect(a,RED,(0,0,10,5))        
        WIN.blit(a,(bullet.x,bullet.y))

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()



def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width+30 < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
    pygame.quit()

def main():

    WIN.fill(BLACK)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    BG_SOUND.play(loops=-1)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_COMMA and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text =str(ll[0])+" Wins!"

        if yellow_health <= 0:
            winner_text = str(ll[1])+" Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

main()

os.remove(str(ll[0])+'.jpg')
os.remove(str(ll[1])+'.jpg')
webcam.stop()
pygame.quit()