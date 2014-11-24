# Constants

FPS = 60 # frames per second, the general speed of the program
STATUSHEIGHT = 50
DISPLAYWIDTH = 512
DISPLAYHEIGHT = 512
WINDOWWIDTH = DISPLAYWIDTH # size of window's width in pixels
WINDOWHEIGHT = DISPLAYHEIGHT + STATUSHEIGHT # size of windows' height in pixels
DISPLAYCENTER_X = WINDOWWIDTH/2
DISPLAYCENTER_Y = WINDOWHEIGHT/2 + STATUSHEIGHT/2
DISPLAYBORDER = 10

DISPLAYRADIUS = DISPLAYWIDTH/2 - DISPLAYBORDER
if DISPLAYWIDTH > DISPLAYHEIGHT:
    DISPLAYRADIUS = DISPLAYHEIGHT/2 - DISPLAYBORDER

def enum(**enums):
    return type('Enum', (), enums)

Result = enum(NOWT=0, QUIT=1, SUMMAT=2, LEVELUP=3, GAMEOVER=4, NEWGAME=5, LIFELOST=6)

#            R    G    B
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
BLACK    = (  0,   0,   0)
GREEN    = (  0, 255,   0)
PINK     = (252, 128, 165)
YELLOW   = (255, 255,   0)