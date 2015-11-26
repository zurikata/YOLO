import pygame


from pygame.locals import * # allows to write easily and quick

# pygame init()
pygame.init()

clock = pygame.time.Clock()

# the size of the screen
SIZE=WIDTH,HEIGHT=800,600

# the clock
DELAY =60
CELLSIZE =15

# Define movements
UP = 'up'
DOWN= 'down'
LEFT = 'left'
RIGHT= 'right'


def whatNext():
    for event in pygame.event.get([KEYDOWN,KEYUP,QUIT]):
        if event.type==QUIT:
            pygame.quit()
            

        elif event.type==KEYDOWN:
            continue
        return event.key

    return None

def makeTextObjs(text, font, tcolour):
    textSurface = font.render(text, True, tcolour)
    return textSurface, textSurface.get_rect()
    




def msgSurface(text, textColour):

    smallText= pygame.font.Font('freesansbold.ttf',20)
    largeText= pygame.font.Font('freesansbold.ttf',150)

    titleTextSurf, titleTextRect = makeTextObjs(text,largeText,textColour)
    titleTextRect.center= (int(WIDTH/2),int(HEIGHT/2))
    surface.blit(titleTextSurf,titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText,pygame.color.THECOLORS["white"]) 
    typTextRect.center= (int(WIDTH/2),int(HEIGHT/2)+120)
    surface.blit(typTextSurf,typTextRect)
    pygame.display.update()
    clock.tick(0)


    while whatNext() == None:
        for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                
        clock.tick()
        pygame.display.update()
        

    runGame()


    

def runGame():
    
    startx = 3 # start point in x
    starty = 3 # start point in y

    coordenates = [{'x':startx,'y':starty}]

    direction= RIGHT
    

    isAlive= 'Yes'


    while True: # main game loop

        while isAlive == 'Yes':
            
  
            for event in pygame.event.get():  # event handling loop
                if event.type==QUIT:
                    pygame.quit()
                    

                elif event.type==KEYDOWN: # when the key is pressed
                    if event.key==K_LEFT:
                        direction = LEFT

                    elif event.key==K_RIGHT:
                        direction = RIGHT

                    elif event.key==K_DOWN:
                        direction = DOWN

                    elif event.key==K_UP:
                        direction = UP

            if direction == UP:
                newCell = {'x':coordenates[0]['x'],'y':coordenates[0]['y']-1}

            elif direction == DOWN:
                newCell = {'x':coordenates[0]['x'],'y':coordenates[0]['y']+1}

            elif direction == LEFT:
                newCell = {'x':coordenates[0]['x']-1,'y':coordenates[0]['y']}

            elif direction == RIGHT:
                newCell = {'x':coordenates[0]['x']+1,'y':coordenates[0]['y']}

            del coordenates[-1] # it deletes de negative first of the coordenates


            coordenates.insert(0, newCell)
            surface.fill(pygame.color.THECOLORS["black"])

            drawCell(coordenates)
            pygame.display.update()    
            clock.tick(DELAY)


            if (newCell['x']<0 or newCell['y']<0 or newCell['x']>WIDTH/CELLSIZE or newCell['y']>HEIGHT/CELLSIZE):
                    isAlive = 'No'

        msgSurface('You Died!',pygame.color.THECOLORS["red"] )
        




def drawCell(coordenates):
    for coord in coordenates:
        x= coord['x']*CELLSIZE
        y= coord['y']*CELLSIZE

        makeCell= pygame.Rect(x,y,CELLSIZE,CELLSIZE)
        pygame.draw.rect(surface,pygame.color.THECOLORS["blue"],makeCell)

while True:
    
    global surface
    surface = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Dancing Block")
    runGame()
    
