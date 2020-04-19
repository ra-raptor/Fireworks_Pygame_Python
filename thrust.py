from utility import *
import pygame,random
vec = pygame.math.Vector2
from particle import *

class ThrustNode(Particle):
    """ Thrust of rocket """
    def __init__(self,main,v,x,y,col):
        self.main = main
        #X-offset at place of origin
        self.xoffset = random.randint(-2,2) 
        self.position = vec(x,y)
        #adding x offset to spwan position
        self.position.x += self.xoffset
        #random magnitude of initial velocity and angle
        self.angle = random.randint(-5,5)
        self.magVel = random.randint(100,500)
        self.velocity = v
        self.velocity += vec(0,self.magVel).rotate(self.angle)
        self.acceleration = vec(0,0)
        #time of spwan
        self.birthTime = pygame.time.get_ticks()
        self.activeDuration = 10
        self.colorCollection = ORANGEFUN
        self.size = 2

    def draw(self):
        #selecting a random colour from colorCollection array and drawing a circle at the calculated position
        choice = random.choice(self.colorCollection)
        pygame.draw.circle(self.main.screen,choice,(int(self.position.x),int(self.position.y)),self.size)

    def update(self):
        #if survived more than lifespan then kill
        now = pygame.time.get_ticks()
        if now-self.birthTime > self.activeDuration:
            self.main.ThrustContainer.remove(self)
        self.update_position() #defined in Particle class