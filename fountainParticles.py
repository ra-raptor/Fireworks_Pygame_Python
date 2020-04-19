from utility import *
import pygame,random
vec = pygame.math.Vector2
from particle import *

class FountainParticle(Particle):
    def __init__(self,main,x,y,col):
        self.main = main
        self.position = vec(x,y)
        #random initial angle and velocity
        self.angle = random.randint(-1,1)
        self.mag = random.randint(-500,-400)
        self.velocity = vec(0,self.mag).rotate(0)
        self.acceleration = vec(0,0)
        self.birthTime = pygame.time.get_ticks()
        self.size_counter_time = pygame.time.get_ticks()
        #random lifespan
        self.activeDuration = random.choice([3000,4000,5000,6000])
        self.colorCollection = col
        self.size = 3
        #posDir is a check for postive direction, half the particles will have positive x velocity half will have negetive
        self.posDir = False
        randInt = random.choice([0,1])
        if randInt == 1:
            self.posDir = True
        self.XVelOffset = random.randint(0,70)

    def draw(self):
        #select random color and draw
        choice = random.choice(self.colorCollection)
        pygame.draw.circle(self.main.screen,choice,(int(self.position.x),int(self.position.y)),self.size)

    def update(self):
        #die when lifespan over
        now = pygame.time.get_ticks()
        if now-self.birthTime > self.activeDuration:
            self.main.FountainParticles.remove(self)   
        #decrease size after set interval (JUST AS A TEST)
        if now - self.size_counter_time > 200:
            self.size_counter_time = now
            self.size-= 1
            if self.size < 2 :
                self.size = 2  
        if self.posDir:
            self.position.x += self.XVelOffset*self.main.dt
        if not self.posDir:
            self.position.x -= self.XVelOffset*self.main.dt
        self.update_position() #From Particle class