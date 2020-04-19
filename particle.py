from utility import *
import pygame,random
vec = pygame.math.Vector2

class Particle:
    "base class for all particles"
    def __init__(self,main,x,y):
        pass

    def update_position(self):
        self.acc("y",10)
        self.velocity += self.acceleration
        self.position += self.velocity*self.main.dt

    def draw(self):
        pygame.draw.circle(self.main.screen,RED,(int(self.position.x),int(self.position.y)),1)

    def acc(self,dir,val):
        if dir == "x":
            self.velocity.x += val
        if dir == "y":
            self.velocity.y += val