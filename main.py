import pygame,os,time,random
from particle import *
from utility import *
from root import *
from fountainBase import *
from spinner import *
from button import *
pygame.init()

class Main:
    ''' main class that controls the entire programm '''
    def __init__(self):
        self.WIDTH = 600
        self.HEIGHT = 750
        self.TITLE = "Fireworks!!"
        #height of canvas for fireworks
        self.canvasHeight = 600
        self.FPS = 30
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.clock = pygame.time.Clock()
        self.isRunning = True
        self.otp = False
        self.play = False
        #clickstate is index of current firework
        self.clickState = 1
        self.run()
    
    def run(self):
        self.isPlaying = True
        # these groups will hold add objects
        self.TempContainer = []
        self.ParticleContainer = []
        self.ThrustContainer = []
        self.SubNodeContainer = []
        self.FountainParticles = []
        self.SpinnerParticles = []
        self.Btns = []

        while self.isPlaying:
            self.clock.tick(self.FPS)
            self.dt = self.clock.tick(self.FPS)/1000
            self.ready()
            self.createButtons()
            self.Btn1.clicked = True
            self.events()
            self.update()
            self.draw()

    def ready(self):
        if self.play and not self.otp:
            count = 1
            self.spwan(count)
            self.play = False
            
    def spwan(self,count):
        # spwan count number of rocket root nodes (TEST)
        for i in range(count):
            self.randt = random.randint(-250,250)
            self.randt2 = random.randint(-50,20)
            self.randv = random.randint(-50,50)
            self.randvy = random.randint(-50,60)
            temp = random.choice([4,6])
            EXPLOSION_SOUNDS[temp].play()
            t = Root(self,self.WIDTH/2 + self.randt,self.canvasHeight+self.randt2,random.randint(100,500),"N")
            self.TempContainer.append(t)

    def spwanXY(self,count,x,y,d,t):
        #spawn method 
        for i in range(count):
            temp = random.choice([4,6])
            EXPLOSION_SOUNDS[temp].play()
            t = Root(self,x,y,d,t)
            self.TempContainer.append(t)
    
    def checkBtnState(self):
        # checks btn state
        if self.clickState==1:
            self.Btn1.clicked = True
        if self.clickState==2:
            self.Btn2.clicked = True
        if self.clickState==3:
            self.Btn3.clicked = True
        if self.clickState==4:
            self.Btn4.clicked = True
        if self.clickState==5:
            self.Btn5.clicked = True

    def resetClick(self):
        #resets click 
        self.Btn1.clicked = False
        self.Btn2.clicked = False
        self.Btn3.clicked = False
        self.Btn4.clicked = False
        self.Btn5.clicked = False
        
    def createButtons(self):
        self.Btn1 = Button(self,self.screen,5,600,114,100,RED,"Rocket 1")
        self.Btn2 = Button(self,self.screen,124,600,114,100,ORANGECORAL,"Rocket 2")
        self.Btn3 = Button(self,self.screen,243,600,114,100,YELLOW,"Rocket 3")
        self.Btn4 = Button(self,self.screen,362,600,114,100,GREEN,"Fountain")
        self.Btn5 = Button(self,self.screen,481,600,114,100,BLUE," Spinner")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.isPlaying:
                    self.isPlaying = False
                self.isRunning = False
            if event.type == pygame.KEYDOWN:
                self.play = True
            #mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN and event.button== 1:
                mouse_x, mouse_y = event.pos
                #handling click for btns
                if mouse_y>600 and mouse_y<700:
                    if mouse_x>5 and mouse_x<119:
                        self.clickState =1
                    if mouse_x>124 and mouse_x<238:
                        self.clickState =2
                    if mouse_x>243 and mouse_x<357:
                        self.clickState =3
                    if mouse_x>362 and mouse_x<476:
                        self.clickState =4
                    if mouse_x>481 and mouse_x<595:
                        self.clickState =5
                #handling click for crackers
                if mouse_y < 600:
                    if self.clickState == 1:
                        self.spwanXY(1,mouse_x,self.WIDTH+100,self.canvasHeight-mouse_y,"N")
                    if self.clickState == 2:
                        self.spwanXY(1,mouse_x,self.WIDTH+100,self.canvasHeight-mouse_y,"S")
                    if self.clickState ==3:
                        self.spwanXY(1,mouse_x,self.WIDTH+100,self.canvasHeight-mouse_y,"B")
                    if self.clickState == 4:
                        t = FountainBase(self,mouse_x)
                        self.FountainParticles.append(t)
                    if self.clickState == 5:
                        t = Spinner(self,mouse_x,mouse_y)
                        self.SpinnerParticles.append(t)
                             
    def update(self):
        #resetclick
        self.resetClick()
        #check for btn state
        self.checkBtnState()
        #update each group
        for i in self.TempContainer:
            i.update()
        for i in self.ParticleContainer:
            i.update()
        for i in self.ThrustContainer:
            i.update()
        for i in self.SubNodeContainer:
            i.update()
        for i in self.FountainParticles:
            i.update()
        for i in self.SpinnerParticles:
            i.update()
        # update each btn
        self.Btn1.update()
        self.Btn2.update()
        self.Btn3.update()
        self.Btn4.update()
        self.Btn5.update()

    def draw(self):
        self.screen.fill(BACKGROUND)
        #draw each groups
        for i in self.TempContainer:
            i.draw()
        for i in self.ParticleContainer:
            i.draw()
        for i in self.ThrustContainer:
            i.draw()
        for i in self.SubNodeContainer:
            i.draw()
        for i in self.FountainParticles:
            i.draw()
        for i in self.SpinnerParticles:
            i.draw()
        #draw background for bts
        pygame.draw.rect(self.screen,(25,25,25),(0,600,600,100))
        # draw each btns
        self.Btn1.draw()
        self.Btn2.draw()
        self.Btn3.draw()
        self.Btn4.draw()
        self.Btn5.draw()
        pygame.display.update()

if __name__ == "__main__":
    temp = Main()
    pygame.quit()
    pygame.display.quit()