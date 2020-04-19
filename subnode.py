from utility import *
import pygame,random
from math import sqrt
vec = pygame.math.Vector2
from particle import *
from particlenode import *

class Subnode(Particle):
    def __init__(self,main,x,y,c):
        self.main = main
        self.position = vec(x,y)
        #random magnitude of initial velocity and angle
        self.angle = random.randint(-180,180)
        self.velMag = random.choice([300,600])
        self.velocity = vec(self.velMag,0).rotate(self.angle)
        self.acceleration = vec(0,0)
        #particle count of how many particle this will emmit
        self.particle_count = 100
        self.colour = c
        self.timeCounter = pygame.time.get_ticks()
        self.lifespan = 400
        self.size = 4

    def draw(self):
        pygame.draw.circle(self.main.screen,self.colour[0],(int(self.position.x),int(self.position.y)),self.size)
    
    def update(self):
        self.update_position() #defined in Particle Class
        #burst when lifespan is over
        now = pygame.time.get_ticks()
        if now - self.timeCounter > self.lifespan:
            self.burst()

    def burst(self):
        #choose a random sound and play
        temp = random.choice([1,2,3,4])
        EXPLOSION_SOUNDS[temp].play()
        #emmit particles at Burst phase
        for i in range(self.particle_count):
            t = ParticleNode(self.main,self.position.x,self.position.y,self.colour,nerfed=True)
            self.main.ParticleContainer.append(t)
        self.main.SubNodeContainer.remove(self)