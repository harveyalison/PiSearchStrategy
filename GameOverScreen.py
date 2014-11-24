import random, pygame, sys, time
from Globals import *
from PiSearchStrategy import *

class GameOverScreen(object):

    def __init__(self, surface):
        self.surface = surface

    def Show(self):
        self.Draw()

    def Draw(self):

        # First, fill the whole screen with black
        self.surface.fill(BLACK)

        # Draw message
        fontObj = pygame.font.Font('freesansbold.ttf', 64)
        textSurfaceObj = fontObj.render('Game Over!', True, RED, BLACK)
        textRectObj = self.surface.get_rect()
        textRectObj.topleft = (75, 150)
        self.surface.blit(textSurfaceObj, textRectObj)

        pygame.display.update()

        # Play sound
        soundObj = pygame.mixer.Sound('GameOver.wav')
        soundObj.play()
        time.sleep(2)

