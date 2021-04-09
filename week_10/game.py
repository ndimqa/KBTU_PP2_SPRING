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

# Background
BACKGROUND = pygame.image.load("AnimatedStreet.png")

# Screen
WIDTH, HEIGHT = BACKGROUND.get_size()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# FPS
FPS = 60
timer = pygame.time.Clock()

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())

        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)
        self.speed = 300
    
    def collide(self):
        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
        self.rect.center = center

    def move(self):
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface(self.image.get_size())

        center = (WIDTH // 2, HEIGHT - self.image.get_height() // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 300
 
    def move(self):
        pixels_per_frame = self.speed // FPS
        pressed_keys = pygame.key.get_pressed()
         
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

        self.speed = 600

    def move(self):
        global INC_SPEED
        global score
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            INC_SPEED = random.randint(1,5)
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
    coin1 = Coin()

    #Creating Sprites Groups
    enemies = pygame.sprite.Group()
    enemies.add(enemy1)
    coin_ = pygame.sprite.Group()
    coin_.add(coin1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    all_sprites.add(enemy1)
    all_sprites.add(coin1)


    score = 0
    done = False
    coin = 0
    pygame.mixer.Sound('soundtack.mp3').play()
    while not done:
        
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_done = True
        
        if pygame.sprite.spritecollideany(player1, enemies):
            pygame.mixer.pause()
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
        
        if pygame.sprite.spritecollideany(player1,coin_):
            coin1.collide()
            pygame.mixer.Sound('get_coin.mp3').play()
            coin = coin + 1

        DISPLAYSURF.blit(BACKGROUND, (0, 0))
        
        coins = font_small.render(str(coin), True, BLACK)
        scores = font_small.render(str(score), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))
        DISPLAYSURF.blit(coins, (WIDTH - 30, 10))

        for sprite in all_sprites:
            sprite.move()
            sprite.draw(DISPLAYSURF)

        pygame.display.flip()

pygame.quit()