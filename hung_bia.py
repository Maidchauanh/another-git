# Pygame template - skeleton for a new pygame project
import pygame
from random import *

X = 360
Y = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init() # mixer de choi nhac
screen = pygame.display.set_mode((X,Y ))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

Nhan_vat= pygame.sprite.Group()
Kethu=pygame.sprite.Group()


def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False


class Player(pygame.sprite.Sprite):
	def __init__(self,color,X,Y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.color=color
		self.X=X
		self.Y=Y
		self.width=width
		self.height=height


		self.image=pygame.Surface((width,height))
		self.image.fill(self.color)
		self.rect=self.image.get_rect()
		self.rect.centerx = X/2
		self.rect.bottom=Y
		self.speed=15
		self.time=0
		self.a=100
	def update(self):
		'''if keyPressed(pygame.K_LEFT)==True and self.rect.left>=0 :
			self.speed,self.a=self.speed*-1,self.a*-1
			self.rect.x+=-self.speed*self.time + 0.5*-self.a*self.time**2
			self.time+=0.05
			print self.time
		if keyPressed(pygame.K_LEFT)==False:
			self.time=0
		if keyPressed(pygame.K_RIGHT)==True and self.rect.right<=self.X-5:
			self.rect.x+=self.speed*self.time + 0.5*self.a*self.time**2
			self.time+=0.05
		if keyPressed(pygame.K_RIGHT)==False:
			self.time=0'''
		if keyPressed(pygame.K_LEFT)==True and self.rect.left>=0 :
			self.rect.x-=self.speed
		elif keyPressed(pygame.K_RIGHT)==True and self.rect.right<=self.X-5:
			self.rect.x+=self.speed
		
class Enemy(pygame.sprite.Sprite):
	def __init__(self,color,X,Y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.color=color
		self.X=X
		self.Y=Y
		self.width=width
		self.height=height


		self.image=pygame.Surface((self.width,self.height))
		self.image.fill(self.color)
		self.rect=self.image.get_rect()	
		self.time=0
		self.g=100
		self.rect.y=self.height
		self.rect.x=randint(1,self.X/10)*10
	def update(self):
		self.rect.y+=self.g*0.5*self.time**2
		self.time+=0.05
		if self.rect.y  >= Y :
			self.rect.y=-self.height
			self.time=0
			self.rect.x=randint(1,self.X/10)*10

#Game loop
running = True
ThungBia=Player(GREEN,X,Y,50,30)
for i in range(1):
	Bia=Enemy(RED,X,Y,20,30)
	Kethu.add(Bia)
Nhan_vat.add(ThungBia)



while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    screen.fill(BLACK)
    Nhan_vat.update()
    Kethu.update()
    # Draw / render
    Kethu.draw(screen)
    Nhan_vat.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.update()

pygame.quit()
