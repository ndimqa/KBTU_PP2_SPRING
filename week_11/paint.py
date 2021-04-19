import pygame 

pygame.init()

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
COLORS = [RED, GREEN, BLUE, WHITE]
i  = 0
width = 500
height = 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint")

isPressed = False
prevPoint = (0,0)

#0 - pencil, 1 - rectangle, 2 - circle 3 - erase
currentTool = 0
toolCount = 4

def drawRectangle(surface, x,y, w, h):
    pygame.draw.rect(surface, COLORS[i], [x, y, w, h]) #deleted 5 

def drawCircle(surface, x,y):
    pygame.draw.circle(surface, COLORS[i], (x, y), 5)

def drawLine(surface, startPos, endPos):
    pygame.draw.line(surface, COLORS[i], startPos, endPos, 2)

def erase(surface, x, y):
    pygame.draw.circle(surface, BLACK, (x, y), 40)

done = False
while not done:
    curPoint = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                currentTool = (currentTool + 1) % toolCount
            if event.key == pygame.K_c:
                screen.fill(BLACK)
            if event.key == pygame.K_z:
                if i == 3:
                    i = 0
                else:
                    i += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        elif event.type == pygame.MOUSEMOTION and isPressed == True:
            if currentTool == 0: # line
                 drawLine(screen, prevPoint, curPoint)
            elif currentTool == 1: # rectangle
                drawRectangle(screen, curPoint[0],curPoint[1],10,10)
            elif currentTool == 2: # circle
                drawCircle(screen, curPoint[0], curPoint[1])
            elif currentTool == 3: #erase
                erase(screen, curPoint[0],curPoint[1])
        
            prevPoint = curPoint
            curPoint = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
            pygame.image.save(screen, 'screenshot.jpg')

    pygame.display.flip()