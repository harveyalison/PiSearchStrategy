from PiSearchStrategy import *
import pygame
from pygame.locals import *

class IntroScreen(object):

    def __init__(self, surface):
        self.surface = surface

    def Show(self):
        self.Draw()
        return self.HandleEvents()

    def Draw(self):
        # First, fill the whole screen with black
        self.surface.fill(BLACK)

        # Draw Game Title
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Pi Search Strategy!', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (100, 50)
        self.surface.blit(textSurfaceObj, textRectObj)

        # Draw game description
        fontObj = pygame.font.Font('freesansbold.ttf', 16)
        
        textSurfaceObj = fontObj.render('Adjust the Raspberry Pi receiver parameters', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 150)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('to detect all threats!', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 175)
        self.surface.blit(textSurfaceObj, textRectObj)

        # Draw Controls       
        textSurfaceObj = fontObj.render('Controls:', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 225)
        self.surface.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = fontObj.render('UP = Increase angle (reduces detection power)', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 250)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('DOWN = Decrease angle (increases detection power)', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 275)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('LEFT = Search left', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 300)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('RIGHT = Search right', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 325)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('A = Increase speed (reduces detection power)', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 350)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('B = Decrease speed (increases detection power)', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 375)
        self.surface.blit(textSurfaceObj, textRectObj)

        # Draw Options
        textSurfaceObj = fontObj.render('Options:', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 425)
        self.surface.blit(textSurfaceObj, textRectObj)
        
        textSurfaceObj = fontObj.render('N = new game', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 450)
        self.surface.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj.render('Q = quit', True, GREEN, BLACK)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = (50, 475)

        self.surface.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        
    def HandleEvents(self):
        # Wait forever until the user enters something we can use
        while True:
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT or \
                    (event.type == KEYUP and event.key == K_ESCAPE) or \
                    (event.type == KEYUP and event.key == ord('q')):
                    return Result.QUIT                
                elif event.type == KEYUP:
                    if event.key == ord('n') or event.key == pygame.K_c:
                        return Result.NEWGAME

