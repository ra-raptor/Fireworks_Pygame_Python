from utility import *
import pygame,random
vec = pygame.math.Vector2
from particle import *

class ParticleNode(Particle):
    def __init__(self,main,x,y,col,nerfed=False,nerfCount=False):
        self.main = main
        self.position = vec(x,y)
        #random magnitude of initial velocity and angle
        self.angle = random.randint(-180,180)
        self.magVel = random.randint(-1000,0)
        self.velocity = vec(self.magVel,0).rotate(self.angle)
        self.acceleration = vec(0,0)
        self.birthTime = pygame.time.get_ticks()
        self.size_counter_time = pygame.time.get_ticks()
        self.activeDuration = 400
        self.colorCollection = col
        self.size = 3
        #will behave diffrently for Semi Bang and Ring
        self.nerfedforbang = False
        self.isRing = False
        if (nerfed):
            #when nerfed 
            self.velocity/=5
        if (nerfCount):
            self.nerfedforbang = True
            self.nerfDivisor = nerfCount
            if nerfCount != "RING":
                self.velocity /= self.nerfDivisor
            self.waitFor = 100
            self.activeDuration = 450
            if nerfCount=="RING":
                self.randomNum = random.randint(500,600)
                self.velocity = vec(self.randomNum,0).rotate(self.angle)
                self.isRing = True
  
    def draw(self):
        #select random color and draw
        choice = random.choice(self.colorCollection)
        if (self.nerfedforbang):
            choice = WHITE
            now = pygame.time.get_ticks()
            if now - self.birthTime < self.waitFor:
                choice = random.choice(self.colorCollection)
        if (self.isRing) == True:
            choice = random.choice(self.colorCollection)
        pygame.draw.circle(self.main.screen,choice,(int(self.position.x),int(self.position.y)),self.size)

    def update(self):
        #die when lifespan is over
        now = pygame.time.get_ticks()
        if now-self.birthTime > self.activeDuration:
            self.main.ParticleContainer.remove(self)  
        #decrease size with time (JUST AS A TEST) 
        if now - self.size_counter_time > 200:
            self.size_counter_time = now
            self.size-= 1
            if self.size < 2 :
                self.size = 2
        self.update_position() #Particle Class