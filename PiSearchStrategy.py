import pygame.gfxdraw
from Receivers import *
from Emitters import *
from Globals import *
from IntroScreen import *
from LifeLostScreen import *
from GameOverScreen import *

# The one and only receiver
RECEIVER = None

# The collection of emitters
EMITTERS = []

LEVEL = None
SCORE = None

def main():
    global FPSCLOCK, WINDOWSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    WINDOWSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pi Search Strategy')
    
    # Keep going until the user says quit
    while True:
        introScreen = IntroScreen(WINDOWSURF)
        introScreenResult = introScreen.Show()
        if introScreenResult == Result.QUIT:
            break
        if introScreenResult == Result.NEWGAME:
            GameLoop()   

    # Shut down in an orderly fashion
    pygame.quit()
    sys.exit()

def GameLoop():
    global LEVEL, SCORE, RECEIVER
    SCORE = 0
    LEVEL = 1
    RECEIVER = SimpleReceiver(WINDOWSURF)

    while True: # Main game loop
        SetupLevel()
        levelResult = LevelLoop()
        if levelResult == Result.LEVELUP:
            LEVEL += 1
        elif levelResult == Result.QUIT:
            return Result.QUIT
        elif levelResult == Result.GAMEOVER:
            return Result.GAMEOVER

def SetupLevel():
    global EMITTERS, LEVEL
        
    if LEVEL != 1:
        # Pause a bit to let any sounds finish
        # from previous level
        time.sleep(2)
        # Play level up sound
        soundObj = pygame.mixer.Sound('LevelUp.wav')
        soundObj.play()
        time.sleep(2)
    
    # Each level has a number of emitters equal to the level
    emitterCount = LEVEL   
    EMITTERS = []       
    while emitterCount > 0:
        EMITTERS.append(SimpleEmitter(WINDOWSURF))
        emitterCount -= 1        
            
def LevelLoop(): 
    
    while True: # Main level loop
        eventResult = HandleEvents()

        if eventResult == Result.QUIT:
            return Result.QUIT
        
        gameStateChanged = Result.NOWT;
        if eventResult == Result.SUMMAT:
            gameStateChanged = UpdateState()
        
        if gameStateChanged == Result.LEVELUP:
            return Result.LEVELUP
        elif gameStateChanged == Result.GAMEOVER:
            # Show game over screen
            gameOverScreen = GameOverScreen(WINDOWSURF)
            gameOverScreen.Show()
            return Result.GAMEOVER
        elif gameStateChanged == Result.LIFELOST:
            # Show life lost screen
            lifeLostScreen = LifeLostScreen(WINDOWSURF)
            lifeLostScreen.Show()
            # Resume
            gameStateChanged = Result.SUMMAT
        elif gameStateChanged == Result.SUMMAT:
            UpdateWindow()

        # Wait a clock tick
        FPSCLOCK.tick(FPS)

def HandleEvents():
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            return Result.QUIT

        RECEIVER.Handle(event)

    # For now, always say summat happened
    return Result.SUMMAT

def UpdateState():
    global EMITTERS, RECEIVER, SCORE, LEVEL

    # Default result to always update for now
    result = Result.SUMMAT

    # Update the receiver
    RECEIVER.UpdateState(EMITTERS)

    # Update all the emitters
    for emitter in EMITTERS:
        emitter.UpdateState(RECEIVER, LEVEL)

    liveEmitters = []
    noEmitterReachedTarget = True
    for emitter in EMITTERS:
        if emitter.lives == 0:
            soundObj = pygame.mixer.Sound('KaBoom.wav')
            soundObj.play()
            SCORE += 1
        elif emitter.targetReached == True:
            noEmitterReachedTarget = False
            RECEIVER.lives -= 1
            if RECEIVER.lives == 0:
                result = Result.GAMEOVER
                break
            else:
                result = Result.LIFELOST
                break   
        else:
            liveEmitters.append(emitter)

    EMITTERS = liveEmitters 
    
    if len(EMITTERS) == 0 and noEmitterReachedTarget == True:
        result = Result.LEVELUP

    return result

def UpdateWindow():
    # First, fill the whole screen with black
    WINDOWSURF.fill(BLACK)

    # Then update the status and display
    DrawStatus()
    DrawDisplay()
    
    # Redraw the screen
    pygame.display.update()

def DrawDisplay():
    # Draw a border for the display
    displayBorderRect = pygame.Rect(0, STATUSHEIGHT, DISPLAYWIDTH, DISPLAYHEIGHT)
    pygame.gfxdraw.rectangle(WINDOWSURF, displayBorderRect, WHITE)
    
    # Draw the emitters
    DrawEmitters()

    # Draw the Receiver
    RECEIVER.Draw()
        
def DrawStatus():       
    # Draw a border for the status
    statusBorderRect = pygame.Rect(0, 0, DISPLAYWIDTH, STATUSHEIGHT)
    pygame.gfxdraw.rectangle(WINDOWSURF, statusBorderRect, WHITE)
        
    fontObj = pygame.font.Font('freesansbold.ttf', 8)
    
    # Draw lives left
    textSurfaceObj = fontObj.render('Lives:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (DISPLAYBORDER, 7)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

    lifeNumber = 0
    while lifeNumber < RECEIVER.lives:
        smallPiImg = pygame.image.load('PiSmall.png')
        WINDOWSURF.blit(smallPiImg, (DISPLAYBORDER + 20*lifeNumber, 20))
        lifeNumber += 1

    # Draw receiver speed 
    textSurfaceObj = fontObj.render('Speed:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (400, 7)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)
    textSurfaceObj = fontObj.render(str(RECEIVER.speed), True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (445, 7)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

    # Draw receiver beam width
    textSurfaceObj = fontObj.render('Width:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (400, 20)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)
    textSurfaceObj = fontObj.render(str(RECEIVER.width), True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (445, 20)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

    # Draw receiver direction
    textSurfaceObj = fontObj.render('Direction:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (400, 33)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)
    textSurfaceObj = fontObj.render(str(RECEIVER.direction), True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (445, 33)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

    # Draw receiver strength
    textSurfaceObj = fontObj.render('Power:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (300, 33)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)
    textSurfaceObj = fontObj.render(str(RECEIVER.power), True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (330, 33)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('Score:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (300, 20)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)
    textSurfaceObj = fontObj.render(str(SCORE), True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (330, 20)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj.render('Level:', True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (300, 7)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)
    textSurfaceObj = fontObj.render(str(LEVEL), True, GREEN, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (330, 7)    
    WINDOWSURF.blit(textSurfaceObj, textRectObj)

def DrawEmitters():
    for emitter in EMITTERS:
        emitter.Draw()  

if __name__ == '__main__':
    main()