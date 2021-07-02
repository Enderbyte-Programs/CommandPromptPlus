import pygame
import random
from os import startfile
from tkinter import *
from tkinter import messagebox
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    )
def se(spawnrate):
    global spawn
    spawn = spawnrate
    window.destroy()
window = Tk()
window.title('Game')
lbl = Label(window,text='Please select your difficulty')
lbl.grid(column=2,row=0)
btn = Button(window,text='Super Easy',command=lambda: se(1000),bg='blue')
btn.grid(column=0,row=1)
btn1 = Button(window,text='Easy',command=lambda: se(500),bg='green')
btn1.grid(column=1,row=1)
btn2 = Button(window,text='Normal',command=lambda: se(250),bg='yellow')
btn2.grid(column=2,row=1)
btn3 = Button(window,text='Hard',command=lambda: se(125),bg='orange')
btn3.grid(column=3,row=1)
btn4 = Button(window,text='Super Hard',command=lambda: se(80),bg='red')
btn4.grid(column=4,row=1)
window.mainloop()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.image.load("sprite.png").convert()
        self.surf.set_colorkey((255,255,255),RLEACCEL)

        self.rect = self.surf.get_rect()

    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0,SCREEN_HEIGHT),
                )
            )
        self.speed = random.randint(5,20)
    def update(self):
        global startagain
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
        if startagain == True:
            self.kill()
            

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0,0,0),RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0,SCREEN_HEIGHT),
                )
            )
    def update(self):
        self.rect.move_ip(-5,0)
        if self.rect.right < 0:
            self.kill()
pygame.mixer.init()
ticks_played = 0
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Bullet Run Test Build 2171.3')

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY,spawn)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 2000)

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
pygame.mixer.music.load("gamemusicmain.mp3")
pygame.mixer.music.play(loops=-1)
collision_sound = pygame.mixer.Sound("death.ogg")
running = True
started = True
while started == True:
    player = Player()
    all_sprites.add(player)
    ticks_played = 0
    try:
        f = open('besttime.txt')
        bestscore = f.read()
        f.close()
        try:
            bestscore = int(bestscore)
        except:
            bestscore = 0
            f = open('besttime.txt','w')
            f.write('0')
            f.close()
    except:
        f = open('besttime.txt','x')
        f.write('0')
        bestscore = 0
        f.close()
    while running:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
                started = False

            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            elif event.type == ADDCLOUD:
                new_cloud = Cloud()
                clouds.add(new_cloud)
                all_sprites.add(new_cloud)
                
        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)
        enemies.update()
        clouds.update()
        screen.fill((135,206,250))

        for entity in all_sprites:
            screen.blit(entity.surf,entity.rect)

        if pygame.sprite.spritecollideany(player,enemies):
            player.kill()
            collision_sound.play()
            running = False

        pygame.display.flip()
            
        clock.tick(30)
        ticks_played += 1
        startagain = False
    messagebox.showerror('Oof','You died')
    running = True
    x = 'You scored' + str(ticks_played) + '!'
    messagebox.showinfo('Game',x)
    if ticks_played > bestscore:
        messagebox.showinfo('Game',"You have a new high score! "+' ' + str(ticks_played))
        try:
            f = open('besttime.txt','w')
            f.write(str(ticks_played))
            f.close()
        except:
            f = open('besttime.txt','x')
            f.write(str(ticks_played))
            f.close()
    started = False
    running = False
pygame.mixer.music.stop()
pygame.mixer.quit()
