import pygame
vec = pygame.math.Vector2
from utility import *

class Button:
    def __init__(self,main,surface,x,y,w,h,colour,text):
        self.surface = surface
        self.position = vec(x,y)
        self.width = w
        self.height = h
        self.main = main
        self.colour = BUTTONS #from utility
        self.currentColour = self.colour[0]
        self.fontColor = self.colour[1]
        self.text = text
        self.ishover = False
        self.clicked = False

    def draw(self):
        #draw diffrent style based on current state
        if self.ishover:
            self.currentColour = self.colour[1]
            self.fontColor = self.colour[0]
        if self.clicked:
            self.currentColour = self.colour[2]
            self.fontColor = self.colour[1]
        pygame.draw.rect(self.surface,self.currentColour,(self.position.x,self.position.y,self.width,self.height),0)
        #draw text on btn
        if self.text != "":
            font = pygame.font.SysFont('Calibri',28)
            text = font.render(self.text,1,self.fontColor)
            self.surface.blit(text,(self.position.x+self.width/2-46,self.position.y+self.height/2-7))

    def update(self):
        # check for hover when mouse pointer is nearby
        x,y = pygame.mouse.get_pos()
        if y > self.position.y and y < self.position.y + self.height:
            if x > self.position.x and x < self.position.x + self.width:
                self.ishover = True


