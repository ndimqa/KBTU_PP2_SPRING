import pygame
import time
import random
import pickle
 
pygame.init()
# lelevls list
levels = []
levels.append("lvl1.txt")
levels.append("lvl2.txt")
levels.append("lvl3.txt")
wall = pygame.image.load("wall_image.jpg")
walls_points = []

#file nake for data
FILE_NAME = 'snakes_saved.data'

#colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# width and heigh
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)

#score
def Your_score(score, x, y, color):
    value = score_font.render(color +" Score: " + str(score), True, yellow)
    dis.blit(value, [x, y])
 
#draw snake
def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])
 
# measseges on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width / 2) - (mesg.get_width()/2), (dis_height  / 2) - mesg.get_height()])   
def message_1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [(dis_width / 2) - (mesg.get_width()/2), (dis_height / 4) - mesg.get_height()])

def pauseLoop():
    pause = True
    # for pause
    while pause:
        dis.fill(blue)
        message("Press space to continue game", yellow)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
 
def gameLoop():
    # variables for snakes
    game_over = False
    game_close = False
    chosen = False
    level_chosen = False
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List_1 = []
    Length_of_snake_1 = 1
    
    x2 = (dis_width / 2) - 20
    y2 = dis_height / 2
 
    x2_change = 0
    y2_change = 0
 
    snake_List_2 = []
    Length_of_snake_2 = 1
    
    #variables for food
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close == True:
            # loop when player lost
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake_1 - 1, 0, 0, " black")
            Your_score(Length_of_snake_2 - 1, dis_width - 165, 0, " white")
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        #quit 
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        #play again
                        gameLoop()
        while not chosen:
            # main screen
            dis.fill(blue)
            message("Press space to load saved game", yellow)
            message_1("press form 1 to 3 to chose level",yellow)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        #choose level 1
                        level_num = 0
                        chosen = True
                    if event.key == pygame.K_2:
                        #choose level 2
                        level_num = 1
                        chosen = True
                    if event.key == pygame.K_3:
                        #choose level 3
                        level_num = 2
                        chosen = True
                    if event.key == pygame.K_SPACE:
                        # downolad game from file
                        try:
                            with open(FILE_NAME, 'br') as f:
                                snakes = pickle.load(f)
                                snake_List_1 = snakes[0]
                                x1 = snakes[1]
                                y1 = snakes[2]
                                Length_of_snake_1 = snakes[3]
                                x1_change = snakes[4]
                                y1_change = snakes[5]
                                Length_of_snake_2 = snakes[6]
                                x2 = snakes[7]
                                y2 = snakes[8]
                                Length_of_snake_2 = snakes[9]
                                x2_change = snakes[10]
                                y2_change = snakes[11]
                                foodx = snakes[12]
                                foody = snakes[13]
                                level_num = snakes[14]
                                chosen = True
                        except Exception as e:
                            print(e)
                            chosen = True
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #when you quit all data saved in file
                with open(FILE_NAME, 'bw') as f:
                    snakes = [snake_List_1, x1, y1, Length_of_snake_1 , x1_change, y1_change,
                             snake_List_2, x2, y2, Length_of_snake_2 , x2_change, y2_change,
                             foodx, foody, level_num]
                    pickle.dump(snakes, f)
                    game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # move left black snake
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    # move right black snake
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    # move up black snake
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    # move down black snake
                    y1_change = snake_block
                    x1_change = 0
                if event.key == pygame.K_a:
                    # move left white snake
                    x2_change = -snake_block
                    y2_change = 0
                elif event.key == pygame.K_d:
                    # move right white snake
                    x2_change = snake_block
                    y2_change = 0
                elif event.key == pygame.K_w:
                    # move up white snake
                    y2_change = -snake_block
                    x2_change = 0
                elif event.key == pygame.K_s:
                    # move down white snake
                    y2_change = snake_block
                    x2_change = 0
                elif event.key == pygame.K_ESCAPE:
                    #pause
                    pauseLoop()
                    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            # if black snake go through screen palyer lost
            game_close = True
        x1 += x1_change
        y1 += y1_change
        
        if x2 >= dis_width or x2 < 0 or y2 >= dis_height or y2 < 0:
            # if white snake go through screen palyer lost
            game_close = True
        x2 += x2_change
        y2 += y2_change
        
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head_1 = []
        snake_Head_1.append(x1)
        snake_Head_1.append(y1)
        snake_List_1.append(snake_Head_1)
        if len(snake_List_1) > Length_of_snake_1:
            del snake_List_1[0]
        for x in snake_List_1[:-1]:
            # if snake go towards its self
            if x == snake_Head_1:
                game_close = True
        our_snake(snake_block, snake_List_1, black)
        
        snake_Head_2 = []
        snake_Head_2.append(x2)
        snake_Head_2.append(y2)
        snake_List_2.append(snake_Head_2)
        if len(snake_List_2) > Length_of_snake_2:
            del snake_List_2[0]
        for x in snake_List_2[:-1]:
            # if snake go towards its self
            if x == snake_Head_2:
                game_close = True
        our_snake(snake_block, snake_List_2, white)
        
        file = open(levels[level_num],'r').readlines()
        # makking level
        for i in range(len(file)):
            for j in range(len(file[i])):
                if file[i][j] == "#":
                    dis.blit(wall,(j * snake_block, i * snake_block))
                    walls_points.append((j * snake_block, i * snake_block))
        
        food = [foodx, foody]
        for points in walls_points:
            if list(points) == snake_Head_1 or list(points) == snake_Head_2:
                game_close = True
            if list(points) == food:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            
        Your_score(Length_of_snake_2 - 1, dis_width - 165, 0, " white")
        Your_score(Length_of_snake_1 - 1, 0, 0, " black")
        
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_1 += 1
            
        if x2 == foodx and y2 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake_2 += 1
        
        if x1 == x2 and y1 == y2:
            game_close = True
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
