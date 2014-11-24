import pygame, sys, time
from PiSearchStrategy import *

class LifeLostScreen(object):

    def __init__(self, surface):
        self.surface = surface

    def Show(self):
        self.Draw()

    def Draw(self):

        # Draw a little triangle joining the pi to the speech bubble
        polygon = ((DISPLAYCENTER_X + 20, DISPLAYCENTER_Y - 15), 
                   (DISPLAYCENTER_X + 40, DISPLAYCENTER_Y - 30), 
                   (DISPLAYCENTER_X + 60, DISPLAYCENTER_Y - 30),)
        pygame.draw.polygon(self.surface, WHITE, polygon, 0)
        pygame.draw.polygon(self.surface, RED, polygon, 2)

        # Draw the speech bubble
        speechBubbleRect = pygame.Rect((DISPLAYCENTER_X + 40, DISPLAYCENTER_Y - 80), (110, 50))
        pygame.draw.rect(self.surface, WHITE, speechBubbleRect, 0)
        pygame.draw.rect(self.surface, RED, speechBubbleRect, 2)

        # Draw a little white bit over the join
        pygame.draw.line(self.surface, WHITE, 
                         (DISPLAYCENTER_X + 42, DISPLAYCENTER_Y - 31),
                         (DISPLAYCENTER_X + 58, DISPLAYCENTER_Y - 31))
        pygame.draw.line(self.surface, WHITE, 
                         (DISPLAYCENTER_X + 42, DISPLAYCENTER_Y - 30),
                         (DISPLAYCENTER_X + 56, DISPLAYCENTER_Y - 30))
        pygame.draw.line(self.surface, WHITE, 
                         (DISPLAYCENTER_X + 42, DISPLAYCENTER_Y - 29),
                         (DISPLAYCENTER_X + 54, DISPLAYCENTER_Y - 29))

        # Draw message
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Ouch!', True, RED, WHITE)
        speechBubbleRect.topleft = (DISPLAYCENTER_X + 49, DISPLAYCENTER_Y - 69)
        self.surface.blit(textSurfaceObj, speechBubbleRect)

        pygame.display.update()

        # Play sound
        soundObj = pygame.mixer.Sound('OhDear.wav')
        soundObj.play()
        time.sleep(2)
