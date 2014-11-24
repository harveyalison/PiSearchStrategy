from Globals import *
import pygame
from pygame.locals import *
import math
import pygame.gfxdraw

class SimpleReceiver(object):

    CLOCKWISE = 'Clockwise'
    ANTICLOCKWISE = 'Anticlockwise'
    STRONG = 'Strong'
    MEDIUM = 'Medium'
    WEAK = 'WEAK'

    def __init__(self, surface):
        self.surface = surface
        self.speedIncreasing = False
        self.speedDecreasing = False
        self.widthIncreasing = False
        self.widthDecreasing = False
        self.direction = self.CLOCKWISE    
        self.angle = 0
        self.width = 45
        self.power = self.MEDIUM
        self.speed = 1
        self.lives = 3
        self.rect = pygame.Rect((DISPLAYCENTER_X-25, DISPLAYCENTER_Y-25), (50, 50))

    def UpdateState(self, emitters):
        # Adjust speed, in the range 1-10
        if(self.speedIncreasing and self.speed < 10):
            self.speed += 1
        elif(self.speedDecreasing and self.speed > 1):
            self.speed -= 1
           
        # Adjust width, in the range 5-180 degrees
        if(self.widthIncreasing and self.width < 180):
            self.width += 5
        elif(self.widthDecreasing and self.width > 5):
            self.width -= 5

        # Update angle, depending on direction
        if(self.direction == self.CLOCKWISE):
            self.angle += self.speed
            if self.angle > 360:
                self.angle -= 360                
        elif(self.direction == self.ANTICLOCKWISE):
            self.angle -= self.speed
            if self.angle < 0:
                self.angle += 360

        # Update power
        if self.width < 45:
            self.power = self.STRONG
        elif self.width < 90:
            self.power = self.MEDIUM
        else:
            self.power = self.WEAK
    
    def Handle(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.direction = self.CLOCKWISE
            if event.key == K_LEFT:
                self.direction = self.ANTICLOCKWISE
            if event.key == ord('a'):
                self.speedIncreasing = True
            if event.key == ord('b'):
                self.speedDecreasing = True
            if event.key == K_UP:
                self.widthIncreasing = True
            if event.key == K_DOWN:
                self.widthDecreasing = True
        elif event.type == KEYUP:
            if event.key == ord('a'):
                self.speedIncreasing = False
            if event.key == ord('b'):
                self.speedDecreasing = False
            if event.key == K_UP:
                self.widthIncreasing = False
            if event.key == K_DOWN:
                self.widthDecreasing = False


    def Draw(self):
        #pgyame.gfxdraw.pie(surface, x, y, r, start, end, color)
        # note pie uses degrees, but starts at 90
        colour = GREEN
        if self.power == self.WEAK:
            colour = YELLOW
        elif self.power == self.STRONG:
            colour = RED             

        pygame.gfxdraw.pie (self.surface, DISPLAYCENTER_X, DISPLAYCENTER_Y, DISPLAYRADIUS, 
                        self.angle-90-self.width/2, self.angle-90+self.width/2, colour)

        # Draw the Pi (magic offset numbers used to line up the centre of the receiver 
        # with the middle of the raspberry in the png)
        piImg = pygame.image.load('Pi.png')
        self.surface.blit(piImg, (DISPLAYCENTER_X - 23, DISPLAYCENTER_Y - 35))

    def IsCovering(self, angle):

        selfRads = math.radians(self.angle)
        halfWidthRads = math.radians(self.width/2)
        angleRads = math.radians(angle)

        if selfRads + halfWidthRads > angleRads and selfRads - halfWidthRads < angleRads:
            return True     

        return False