from utility import *
import pygame,random
from math import sqrt
vec = pygame.math.Vector2
from particle import *
from particlenode import *
from thrust import *
from subnode import *

class Root(Particle):
    def __init__(self,main,x,y,destination,category="N"):
        self.main = main
        self.position =  vec(x,self.main.canvasHeight)
        #calculate required initial velocity to reach mouse pointer
        self.velocity_value = sqrt(60*destination*10)
        self.velocity = vec(0,-self.velocity_value).rotate(0)
        self.acceleration = vec(0,0)
        self.particle_count = 1000
        self.category = category # N : Normal , S : Sprinkler , B : Big Bang
        self.colour = random.choice(GRADIENDTS)
        if self.category == "S":
            self.subNodeCount = 20
        if self.category == "B":
            self.ringCol = random.choice(GRADIENDTS)

    def draw(self):
        pygame.draw.circle(self.main.screen,self.colour[0],(int(self.position.x),int(self.position.y)),6)
    
    def update(self):
        self.thrust()
        self.update_position() #from Particle class 
        #burst at topmost point
        if self.velocity.y > 0:
            self.burst()

    def burst(self):
        #choose random sound and play
        temp = random.choice([2,3])
        EXPLOSION_SOUNDS[temp].play()
        #generate particles
        for i in range(self.particle_count):
            t = ParticleNode(self.main,self.position.x,self.position.y,self.colour)
            self.main.ParticleContainer.append(t)
        #if S then also genetate subnode
        if self.category == "S":
            for i in range(self.subNodeCount):
                s = Subnode(self.main,self.position.x,self.position.y,self.colour)
                self.main.SubNodeContainer.append(s)
        #if b then also generate Ring
        if self.category == "B":
            for i in range(1000):
                t = ParticleNode(self.main,self.position.x,self.position.y,self.colour,nerfCount=3)
                self.main.ParticleContainer.append(t)
            for i in range(1000):
                t = ParticleNode(self.main,self.position.x,self.position.y,self.ringCol,nerfCount="RING")
                self.main.ParticleContainer.append(t)
        #remove self after bang
        self.main.TempContainer.remove(self)

    #generate thrust
    def thrust(self):
        l = sqrt(self.velocity.x**2 + self.velocity.y**2)
        num = l/10
        n = int(num)
        for i in range(n):
            v = (self.velocity.x,self.velocity.y)
            t = ThrustNode(self.main,v,self.position.x,self.position.y,self.colour)
            self.main.ThrustContainer.append(t)
