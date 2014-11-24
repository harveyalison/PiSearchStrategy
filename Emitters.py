from Globals import *
from PiSearchStrategy import *

class SimpleEmitter(object):

    def __init__(self, surface):
        self.surface = surface
        self.threatImg = pygame.image.load('Hostile_Air_Defence_50x50.png')
        self.angle = random.randint(0, 360)
        self.distanceFromCentre = DISPLAYRADIUS - 25
        self.lives = 3
        self.lifeFraction = 0
        self.UpdateRect()
        self.targetReached = False
        
    def Draw(self):
        # Draw threat img
        self.surface.blit(self.threatImg, (self.rect.left, self.rect.top))

        # Draw a leetle green rctangle for each life
        lifeNumber = 1
        while lifeNumber <= self.lives:
            lifeRectTop = self.rect.bottom - lifeNumber*6 + 1
            lifeRectLeft = self.rect.left + 1
            pygame.draw.rect(self.surface, GREEN, (lifeRectLeft, lifeRectTop, 5, 5))
            lifeNumber += 1

    def UpdateRect(self):
        top = DISPLAYCENTER_Y - (math.cos(math.radians(self.angle)) * self.distanceFromCentre) - 25
        left = DISPLAYCENTER_X + (math.sin(math.radians(self.angle)) * self.distanceFromCentre) - 25 
        self.rect = pygame.Rect((left, top), (50, 50))


    def UpdateState(self, receiver, level):  
              
        # Move a bit closer to the centre, a bit faster for higher levels
        if self.distanceFromCentre > 0:
                self.distanceFromCentre -= 0.1 * level

        if self.distanceFromCentre < 25:
            self.targetReached = True

        self.UpdateRect()

        # Lose a little bit of life if the emitter beam is
        # covering our centre, more if the beam is stronger
        if receiver.IsCovering(self.angle) == True:
            if receiver.power == receiver.WEAK:
                self.lifeFraction += 0.5
            elif receiver.power == receiver.MEDIUM:
                self.lifeFraction += 2
            elif receiver.power == receiver.STRONG:
                self.lifeFraction += 3

        if self.lifeFraction >= 10:
            self.lives -= 1
            self.lifeFraction = 0