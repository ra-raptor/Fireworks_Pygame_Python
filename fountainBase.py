from utility import *
import pygame,random
from math import sqrt
vec = pygame.math.Vector2
from fountainParticles import *

class FountainBase():
    def __init__(self,main,x):
        self.main = main
        self.position = vec(x,self.main.canvasHeight)
        self.particle_count = 30
        self.colour = random.choice(GRADIENDTS)
        self.time = pygame.time.get_ticks()
        self.lifespan = 6000
        #play sound
        EXPLOSION_SOUNDS[0].play()

    def draw(self):
        pygame.draw.circle(self.main.screen,self.colour[0],(int(self.position.x),int(self.position.y)),4)
    
    def update(self):
        #die when lifespan is over
        now = pygame.time.get_ticks()
        if now - self.time > self.lifespan:
            self.main.FountainParticles.remove(self)
        #continious burst
        self.burst()
        
    def burst(self):
        for i in range(self.particle_count):
            t = FountainParticle(self.main,self.position.x,self.position.y,self.colour)
            self.main.FountainParticles.append(t)