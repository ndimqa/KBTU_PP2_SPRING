import pygame
import random
import time

pygame.init()

# Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
WIDTH = 400
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Background
BACKGROUND = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
BACKGROUND[0] = pygame.image.load("AnimatedStreet1.png")
BACKGROUND[1] = pygame.image.load("AnimatedStreet2.png")
BACKGROUND[2] = pygame.image.load("AnimatedStreet3.png")
BACKGROUND[3] = pygame.image.load("AnimatedStreet4.png")
BACKGROUND[4] = pygame.image.load("AnimatedStreet5.png")
BACKGROUND[5] = pygame.image.load("AnimatedStreet6.png")
BACKGROUND[6] = pygame.image.load("AnimatedStreet7.png")
BACKGROUND[7] = pygame.image.load("AnimatedStreet8.png")
i = 0
# FPS
FPS = 30
timer = pygame.time.Clock()

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface(self.image.get_size())

        center = (WIDTH // 2, HEIGHT - self.image.get_height() // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 100
 
    def move(self):
        pixels_per_frame = self.speed // FPS
        pressed_keys = pygame.key.get_pressed()

        # if self.rect.top > 0:
        #     if pressed_keys[pygame.K_UP]:
        #         self.rect.move_ip(0, -pixels_per_frame)
        # if self.rect.bottom < HEIGHT:
        #     if pressed_keys[pygame.K_DOWN]:
        #         self.rect.move_ip(0, pixels_per_frame)
         
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-pixels_per_frame, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(pixels_per_frame, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())

        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 1000

    def move(self):
        global INC_SPEED
        global score
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            INC_SPEED = random.randint(1,10)
            score += 1
            center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect)
INC_SPEED = 1
# Creating our own event
pygame.time.set_timer(INC_SPEED, 1000)

game_done = False
while not game_done:
    # Creating sprites
    enemy1 = Enemy()
    player1 = Player()

    #Creating Sprites Groups
    enemies = pygame.sprite.Group()
    enemies.add(enemy1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(enemy1)


    score = 0
    done = False
    while not done:
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_done = True
            # if event.type == INC_SPEED:
            #     for sprite in all_sprites:
            #         sprite.speed += 100
        

        if pygame.sprite.spritecollideany(player1, enemies):
            pygame.mixer.Sound('crash.wav').play()
            DISPLAYSURF.fill(RED)
            txt_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            DISPLAYSURF.blit(game_over, txt_rect)
            pygame.display.flip()
            for sprite in all_sprites:
                sprite.kill()
            choosen = False
            while not choosen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_done = True
                        choosen = True
                    if event.type == pygame.KEYDOWN:
                        choosen = True
                        if event.key == pygame.K_SPACE:
                            game_done = True
            done = True

        DISPLAYSURF.blit(BACKGROUND[i], (0, 0))

        scores = font_small.render(str(score), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))

        for sprite in all_sprites:
            sprite.move()
            sprite.draw(DISPLAYSURF)
            
        if i > 6:
            i = 0
        else:
            i += 1

        pygame.display.flip()

pygame.quit()