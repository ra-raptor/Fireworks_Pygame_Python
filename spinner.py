from utility import *
import pygame,random
from math import sqrt,cos,sin,pi
vec = pygame.math.Vector2
from spinnerParticle import *

class Spinner():
    def __init__(self,main,x,y):
        self.main = main
        self.position = vec(x,y)
        self.velocity = vec(0,0).rotate(0)
        self.acceleration = vec(0,0)
        #number of particles emmited
        self.particle_count = 50
        #random color sequence 
        self.colour = random.choice(GRADIENDTS)
        #time of birth as a reference
        self.birthTime = pygame.time.get_ticks()
        #time in millisecond to die
        self.lifespan = 7000
        #initail rotation = 0 degrees
        self.rotation = 0
        #dR is by how much degrees will the spinner be rotated each time
        self.dR = 16
        #self.size is Radius of SpinnerBody
        self.size=10
        #play sound
        EXPLOSION_SOUNDS[0].play()

    def draw(self):
        #draw a circle with the specified colour and radius in the given position 
        pygame.draw.circle(self.main.screen,self.colour[0],(int(self.position.x),int(self.position.y)),self.size)
    
    def update(self):
        #if survived more than lifespan then kill
        now = pygame.time.get_ticks()
        if now-self.birthTime > self.lifespan:
            self.main.SpinnerParticles.remove(self)
        #rotate
        self.rotate()
        #calcuating X and Y spwan position of 4 particles each 90 degrees apart
        Xoffset1 = self.position.x + self.size*sin(self.rotation*pi/180)
        Yoffset1 = self.position.y - self.size*cos(self.rotation*pi/180)
        Xoffset2 = self.position.x + self.size*sin((self.rotation+180)*pi/180)
        Yoffset2 = self.position.y - self.size*cos((self.rotation+180)*pi/180)
        Xoffset3 = self.position.x + self.size*sin((self.rotation+90)*pi/180)
        Yoffset3 = self.position.y - self.size*cos((self.rotation+90)*pi/180)
        Xoffset4 = self.position.x + self.size*sin((self.rotation-90)*pi/180)
        Yoffset4 = self.position.y - self.size*cos((self.rotation-90)*pi/180)
        for i in range(self.particle_count):
            t1 = SpinnerParticle(self.main,Xoffset1,Yoffset1,self.colour,self.rotation)
            t2 = SpinnerParticle(self.main,Xoffset2,Yoffset2,self.colour,self.rotation+180)
            t3 = SpinnerParticle(self.main,Xoffset3,Yoffset3,self.colour,self.rotation+90)
            t4 = SpinnerParticle(self.main,Xoffset4,Yoffset4,self.colour,self.rotation-90)
            self.main.SpinnerParticles.append(t1)
            self.main.SpinnerParticles.append(t2)
            self.main.SpinnerParticles.append(t3)
            self.main.SpinnerParticles.append(t4)

    def rotate(self):
        #increases rotation value each frame
        self.rotation += self.dR

