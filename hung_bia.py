# Pygame template - skeleton for a new pygame project
import pygame
from random import *
from os import path

# initialize the path
	
PNG_dir=path.join(path.dirname(__file__),"PNG")
Meoteors_dir=path.join(PNG_dir,"Meteors")




X = 900
Y = 600
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
#loading the image

background=pygame.image.load (path.join(PNG_dir,"SpacegameBackground.png")).convert()
player_img=pygame.image.load (path.join(PNG_dir,"ketbia.png")).convert()
ChaiBia=pygame.image.load (path.join(PNG_dir,"ChaiBia.png")).convert()
player_img.set_colorkey(WHITE)
ChaiBia.set_colorkey(WHITE)
player_rect=player_img.get_rect()
background_rect=background.get_rect()


def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False


class Player(pygame.sprite.Sprite):
	def __init__(self,X,Y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.X=X
		self.Y=Y
		self.width=width
		self.height=height
		self.image=pygame.transform.scale(player_img,(self.width,self.height))
		self.image.set_colorkey(BLACK)
		self.radius=112/2
		#self.image.fill(self.color)
		self.rect=self.image.get_rect()	
		self.rect.centerx = X/2
		self.rect.bottom=Y
		self.speed=15
		self.time=0
		self.g=100
	def update(self):
		if keyPressed(pygame.K_LEFT)==True and self.rect.left>=0 :
			self.rect.x-=self.speed
		elif keyPressed(pygame.K_RIGHT)==True and self.rect.right<=self.X-300:
			self.rect.x+=self.speed
class Enemy(pygame.sprite.Sprite):
	def __init__(self,X,Y,width,height):
		pygame.sprite.Sprite.__init__(self)
		self.X=X
		self.Y=Y
		self.width=width
		self.height=height


		#self.image=pygame.transform.scale(ChaiBia,(20,60))
		self.image=pygame.transform.scale(ChaiBia,(self.width,self.height))
		#self.image.fill(self.color)
		self.rect=self.image.get_rect()	
		self.radius=20
		self.time=0
		self.g=100
		self.rect.y=-self.height
		self.rect.x=randint(1,self.X/10-(30+40/10))*10
		self.diem = 0
	def update(self):
		self.rect.y+=self.g*0.5*self.time**2
		self.time+=0.05
		if self.rect.y >= Y :
			self.rect.y=-self.height
			self.time=0
			self.rect.x=randint(1,self.X/10-(30+40/10))*10

class HinhGai(pygame.sprite.Sprite):
	def __init__(self,X,Y):
		pygame.sprite.Sprite.__init__(self)
		self.X=X
		self.Y=Y
		#self.image=pygame.transform.scale(ChaiBia,(20,60))
		self.image=pygame.Surface((300,self.Y))
		self.image.fill(RED)
		self.rect=self.image.get_rect()	
		self.rect.x= self.X-300
running = True
ThungBia=Player(X,Y,int(112*1.2),int(50*1.2))
gaixinh=HinhGai(X,Y,)

# Nhap enemy
for i in range(1):
	Bia=Enemy(X,Y,25,35)
	Kethu.add(Bia)
Nhan_vat.add(ThungBia,gaixinh)
diem =0 


#Game loop


while running:
	# keep loop running at the right speed

	clock.tick(FPS)

	# Process input (events)

	for event in pygame.event.get():
	    # check for closing window
	    if event.type == pygame.QUIT:
	        running = False

	# Update
	#screen.fill(BLACK)
	screen.blit(background,background_rect)

	Nhan_vat.update()
	Kethu.update()

	#Checking colision

	if Bia.rect.y>=ThungBia.rect.top and Bia.rect.x >= ThungBia.rect.left and Bia.rect.x <= ThungBia.rect.right :
   		diem+=1
		print diem

    # Draw / render
	Kethu.draw(screen)
	Nhan_vat.draw(screen)
    # *after* drawing everything, flip the display
	pygame.display.update()
pygame.quit()
