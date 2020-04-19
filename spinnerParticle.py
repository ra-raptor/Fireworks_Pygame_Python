from utility import *
import pygame,random
vec = pygame.math.Vector2
from random import gauss

class SpinnerParticle():
    def __init__(self,main,x,y,col,dir):
        self.main = main
        self.position = vec(x,y)
        #random magnitude of initial velocity
        self.magVel = self.RANDOM()
        self.velocity = vec(-self.magVel,0).rotate(dir)
        self.acceleration = vec(0,0)
        self.birthTime = pygame.time.get_ticks()
        self.activeDuration = 700
        self.colorCollection = col
        self.size = 2
  
    def draw(self):
        #selecting a random colour from colorCollection array and drawing a circle at the calculated position
        choice = random.choice(self.colorCollection)
        pygame.draw.circle(self.main.screen,choice,(int(self.position.x),int(self.position.y)),self.size)

    def update(self):
        #if survived more than lifespan then kill
        now = pygame.time.get_ticks()
        if now-self.birthTime > self.activeDuration:
            self.main.SpinnerParticles.remove(self) 
        #motion
        self.velocity += self.acceleration
        self.position += self.velocity*self.main.dt  
    
    def RANDOM(self):
        #return a gaussain random value
        ran = gauss(50,1000)
        if ran > 10 and ran <1000:
            return ran
        else:
            return self.RANDOM()