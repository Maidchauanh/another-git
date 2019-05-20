import pygame
import random
class fallingOb:
	def __init__(self,screen,color,y,width,height):	
		self.screen=screen
		self.color=color
		self.x=random.randint(10,900-50)
		self.y=y
		self.width=width
		self.height=height
	def fall(self):
		self.y+=10
		if self.y >=600:
			self.y=0
			self.x=random.randint(10,850)
		pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
white=(255,255,255)
black=(0,0,0)
width,height=40,50
pygame.init()
screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Falling")
run=True
Object=[]
clock=pygame.time.Clock()
#making the rain drops
for i in range(1):
	x=random.randint(10,890)
	Bia=fallingOb(screen,black,0,width,height)
	Object.append(Bia)
#mainloops
while run :
	clock.tick(30)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
   	screen.fill(white)
	for o in Object:
		o.fall()
    	pygame.display.update()
pygame.quit()