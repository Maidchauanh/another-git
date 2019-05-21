import pygame
import random
class fallingOb:
	def __init__(self,screen,color,x,y,width,height):	
		self.screen=screen
		self.color=color
		self.x=x
		#self.x=random.randint(10,900-50)
		self.y=y
		self.width=width
		self.height=height
	def fall(self):
		self.y+=10
		if self.y >=600:
			self.y=0
			self.x=round(random.randint(10,850)/10.0)*10.0
			print self.x
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
class Character:
	def __init__(self,screen,color,x,y,width,height):
		self.screen=screen 
		self.color=color
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.keys=pygame.key.get_pressed()
	def Draw(self):
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
	def Dichuyen(self):
		global xnhanvat,ynhanvat
		self.keys=pygame.key.get_pressed()
		if self.keys[pygame.K_LEFT]:
			xnhanvat-=10
		if self.keys[pygame.K_RIGHT]:
			xnhanvat+=10
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
width,height=20,30
pygame.init()
screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Falling")
run=True
Object=[]
clock=pygame.time.Clock()
width_nhanvat,Height_nhanvat=50,30
xnhanvat=900/2-width_nhanvat/2
ynhanvat=600-Height_nhanvat
for i in range(1):
	x=round(random.randint(10,600)/10.0)*10.0
	y=-1*random.randint(300,1000)
	Bia=fallingOb(screen,black,x,y,width,height)
	Object.append(Bia)
#mainloops
while run :
	clock.tick(30)
   	screen.fill(white)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False		
	for o in Object:
		o.fall()
	nhanvat=Character(screen,red,xnhanvat,ynhanvat,width_nhanvat,Height_nhanvat)
	nhanvat.Draw()
	nhanvat.Dichuyen()
	pygame.display.update()
pygame.quit()