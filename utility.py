import pygame
from os import path,getcwd
pygame.mixer.init()

''' COLOURS '''

WHITE = (255,255,255)
BACKGROUND = (30,30,30)
RED = [(255,0,0),(255,30,30), (255,60,60),(225,90,90),(255,120,120),(255,150,150)]
GREEN = [(0,255,0),(30,255,30), (60,255,60),(90,255,90),(120,255,120),(150,255,150)]
BLUE = [(0,0,255),(30,30,255), (60,60,255),(90,90,255),(120,120,255),(150,150,255)]
YELLOW = [(255,255,0),(255,255,30), (255,255,60),(225,255,90),(255,255,120),(255,255,150)]
GREENBLUE = [(0,255,255),(30,255,255), (60,255,255),(90,255,255),(120,255,255),(150,255,255)]
PINK = [(255,0,255),(255,30,255), (255,60,255),(225,90,255),(255,120,255),(255,150,255)]
ORANGEFUN = [(252, 74, 26),(253, 101, 19),(252, 125, 16),(251, 145, 22), (249, 165, 35),(247, 183, 51)]
ORANGECORAL = [(255, 153, 102),(255, 142, 99),(255, 131, 97),(255, 119, 96),(255, 107, 96),(255, 107, 96) ]
PURPINK = [(127, 0, 255),(151, 0, 255),(171, 0, 255),(191, 0, 255),(208, 0, 255),(225, 0, 255) ]
TELEGRAM = [(28, 146, 210),(81, 168, 217),(122, 190, 224),(162, 211, 232),(201, 232, 241),(242, 252, 254)]
ALIVE = [(203, 53, 107),(202, 53, 95),(201, 54, 83),(198, 56, 72),(194, 59, 61),(189, 63, 50)]
COMPARENOW = [(239, 59, 54),(247, 92, 85),(253, 121, 115),(255, 148, 144),(255, 174, 173),(255, 200, 200)]
GRANDEUR = [(0, 0, 70),(0, 38, 106),(0, 72, 140),(0, 107, 171),(0, 144, 199),(28, 181, 224)]
PURPINE = [(32, 0, 44),(62, 34, 74),(95, 68, 106),(130, 103, 140),(166, 141, 175),(203, 180, 212)]
GREENLAKE = [(9, 48, 40),(9, 48, 40),(14, 76, 60),(19, 91, 69),(26, 106, 78),(35, 122, 87) ]

BUTTONS = [(70,70,70),(225,255,225),(30,160,30)]
GRADIENDTS = [RED,GREEN,BLUE,YELLOW,GREENBLUE,PINK,ORANGEFUN,ORANGECORAL,PURPINK,TELEGRAM,ALIVE,COMPARENOW,GRANDEUR,PURPINE,GREENLAKE]

''' SOUND '''
wavFolder = path.join(getcwd(),'sounds/wav')
mp3Folder = path.join(getcwd(),'sounds/mp3')
EXPLOSION_SOUNDS = [
    pygame.mixer.Sound(path.join(wavFolder,'fire2.wav')),
    pygame.mixer.Sound(path.join(wavFolder,'Explosion+4.wav')),
    pygame.mixer.Sound(path.join(wavFolder,'Explosion+6.wav')),
    pygame.mixer.Sound(path.join(wavFolder,'Explosion+8.wav')),
    pygame.mixer.Sound(path.join(wavFolder,'Fireball+1.wav')),
    pygame.mixer.Sound(path.join(wavFolder,'Fireball+3.wav')),
    pygame.mixer.Sound(path.join(wavFolder,'Missile+2.wav')),
]