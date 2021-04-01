import pygame
import math 

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)

def draw_dashed_line(surf, color, start_pos, end_pos, width, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.aaline(surf, color, start.get(), end.get(), width)

def draw_dashed_lines(surf, color, points, width, dash_len):
    for i in range(len(points) - 1):
        draw_dashed_line(surf, color, points[i], points[i + 1], width, dash_len)

#variables for screen 
WIDTH = 800
HEIGTH = 600

#variables for text
x_val  = ['-3п', '-5п/2', '-2п', '-3п/2', '-п','-п/2', '0', 'п/2', 'п', '3п/2', '2п', '5п/2', '3п']
y_val  = [' 1.00', ' 0.75', ' 0.50', ' 0.25',' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
x1_val = ['-3', '-2', '-1']

#colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# variables for graphics
PI = math.pi

# made legend
legend = pygame.Surface((110,50))
legend.fill(WHITE)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
font_1 = pygame.font.SysFont("comicsansms", 20)
font_leg = pygame.font.SysFont("comicsansms", 15)
font_l = pygame.font.SysFont("comicsansms", 12)

#texts
text = font_leg.render("X", True, (0, 0, 0))
text_1 = font_1.render("cos x", True, (BLACK))
text_2 = font_1.render('sin x',True, BLACK)

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = False
    
    #filling screen white color 
    screen.fill((250,250,250))
    
    # X and Y axis
    pygame.draw.line(screen, (0, 0, 0), (70, HEIGTH // 2), (730, HEIGTH // 2), 2) #X axis
    pygame.draw.line(screen, (0, 0, 0), (WIDTH // 2, 30), (WIDTH // 2, 570), 2) #Y axis
    
    # Borders
    pygame.draw.rect(screen, BLACK, (70, 30, 660, 540), 2) 
    
    # Draw backgound
    for i in range(1,10):
        pygame.draw.line(screen, BLACK, (70, i*(60)), (730, i*(60))) # X
    
    for i in range(1,8):
        pygame.draw.line(screen, BLACK,(i*(700//7),30),(i*(700//7),570)) # Y
        
    # Draw lines (left and right)
    for i in range(1, 32):
       pygame.draw.line(screen,BLACK,(70, 60 + int(i) * 15), (76, 60 + int(i) * 15)) # small lines left side
    for i in range(1, 30, 2):        
        pygame.draw.line(screen,BLACK,(70,60 + i * 30),(80, 60 + i *30)) # big lines left side
    for i in range(1,32):
       pygame.draw.line(screen,BLACK,(730, 60 + int(i) * 15), (724, 60 + int(i) * 15)) # small lines right side
    for i in range(1, 30, 2):        
        pygame.draw.line(screen,BLACK,(730, 60 + i * 30),(720, 60 + i * 30)) # big lines right side
    
    #Draw lines up
    for i in range(1,24):
        pygame.draw.line(screen,BLACK,(100+ i*(100//4),30),(100+ i* (100//4),38)) # medium lines up 
    for i in range(1,12):
        pygame.draw.line(screen,BLACK,(100+ i*(100//2),30),(100+ i* (100//2),40)) # big lines up
        
    # small lines up 
    f = 100
    for i in range(1,7):
        for j in range(1,9,2):
            pygame.draw.line(screen,BLACK,(f+ j*12,30),(f+ j* 12,36))
        f = f + 100 
    
    #Draw lines down
    m = 560
    for i in range(1,24):
        pygame.draw.line(screen,BLACK,(100+ i*(100//4), m),(100+ i* (100//4),m + 8)) # medium lines down
    for i in range(1,12):
        pygame.draw.line(screen,BLACK,(100+ i*(100//2),558),(100+ i* (100//2),570)) # big lines down
        
    # small lines down
    f = 100
    for i in range(1,7):
        for j in range(1,9,2):
          pygame.draw.line(screen,BLACK,(f+ j*12,563),(f+ j* 12,569))
        f = f + 100 
    
    #Draw 'X'
    screen.blit(text, (395, 580))
    
    #Draw X axis values
    n = ' '
    for i in range(len(x_val)):
        n = x_val[i]
        x = font_l.render(n, True, (0, 0, 0))
        screen.blit(x, ((100 + 50 * i) - x.get_width() // 2, 570))
        
    #Draw high X axis values
    for i in range(len(x1_val)):
        n = x1_val[i]
        x = font_l.render(n, True, (0, 0, 0))
        screen.blit(x, ((110 + 80 * i) - x.get_width() // 2,  (HEIGTH // 2) + 45 ))
    
    #Draw Y axis values
    for i in range(len(y_val)):
        n = y_val[i]
        x = font_l.render(n, True, (0, 0, 0))
        screen.blit(x, (30 , 59 * (i + 1)  ))
    
    # Draw sin graph
    for x in range(100, 700):
        sin_y1 = 240 * math.sin((x - 100) / 100 * PI)
        sin_y2 = 240 * math.sin((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, RED, False, [(x, 300 + sin_y1), ((x + 1), 300 + sin_y2)])

    #Draw cos graph
    for x in range(100, 700, 3):
        cos_y1 = 240 * math.cos((x - 100) / 100 * PI)
        cos_y2 = 240 * math.cos((x - 99) / 100 * PI)
        pygame.draw.aalines(screen, BLUE, False, [(x, 300 + cos_y1), ((x + 1), 300 + cos_y2)])
    
    # Inserting and fill legend 
    screen.blit(legend,(470,53))
    legend.blit(text_1,(5 ,45 - text_1.get_width()//2)) #cos
    p = [(60, 40 ),(90, 40)]
    draw_dashed_lines(legend, BLUE,p, 3,3)
    
    legend.blit(text_2,(10 ,25 - text_2.get_width()//2)) #sin
    pygame.draw.line(legend,RED,(60, 20 ),(90, 20),2)
    
    pygame.display.flip()