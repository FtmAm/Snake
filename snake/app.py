
import pygame
from random import randint
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self, p = 0):
        super().__init__()
        if (p == 1):
            self.image = pygame.image.load('graphics/ax2.png').convert()
            self.rect = self.image.get_rect()
        elif p == 2:    
            self.image = pygame.image.load('graphics/ax3.png').convert()
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load('graphics/ax.jpg').convert()
            self.rect = self.image.get_rect()
def wall(player):
    if (player.rect.x >= 400):
        player.rect.x = 0
    if (player.rect.y >= 400):
        player.rect.y = 60
    if (player.rect.x <= -20):
        player.rect.x = 380
    if (player.rect.y <= 40):
        player.rect.y = 380
    return player
def score(score_, max_score):
    font = pygame.font.Font(None, 20)
    text = font.render(f'Your score : {score_}', False, 'black')
    text_rec = text.get_rect(center = (300, 40))
    max_score = max(max_score, score_)
    text2 = font.render(f'Max score : {max_score}', False, 'black')
    text2_rec = text2.get_rect(center = (300, 20))
    screen.blit(text, text_rec)
    screen.blit(text2, text2_rec)
    return max_score
def move(players):
    for i in range(len(players) - 1,0, -1):
        players[i].rect.x = players[i - 1].rect.x
        players[i].rect.y = players[i - 1].rect.y
    if (direct == 'up'):
        players[0].rect.y -= 20
        players[0].image = pygame.image.load('graphics/ax4.png').convert()
    if (direct == 'down'):
        players[0].rect.y += 20
        players[0].image = pygame.image.load('graphics/ax2.png').convert()
    if (direct == 'left'):
        players[0].rect.x -= 20
        players[0].image = pygame.image.load('graphics/ax6.png').convert()
    if (direct == 'right'):
        players[0].rect.x += 20
        players[0].image = pygame.image.load('graphics/ax5.png').convert()
    return players
pygame.init()
screen = pygame.display.set_mode([400, 400])
player_test = Player(1)
clock = pygame.time.Clock()
x = 100
y = 40
direct = 'up'
timer = pygame.USEREVENT
pygame.time.set_timer(timer, 200)
active = False
score_ = 0
max_score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if direct != 'down':
                        direct = 'up'
                if event.key == pygame.K_DOWN:
                    if direct != 'up':
                        direct = 'down'
                if event.key == pygame.K_LEFT:
                    if direct != 'right':
                        direct = 'left'
                if event.key == pygame.K_RIGHT:
                    if direct != 'left':
                        direct = 'right'
            if event.type == timer:
                x = players[len(players) - 1].rect.x
                y = players[len(players) - 1].rect.y
                players = move(players)
                
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    active = True
    if active:          
        screen.fill('White')
        surf = pygame.Surface([400, 60])
        surf.fill('Yellow')
        surf_rec = surf.get_rect(center = (200, 30))
        screen.blit(surf, surf_rec)
        player_test = players[0]
        player_test = wall(player_test)
        players[0] = player_test
        if (players[0].rect.colliderect(obj.rect)):
            score_ += 1
            obj.rect.x = randint(0, 19) * 20
            obj.rect.y = randint(3, 19) * 20
            while (pygame.sprite.spritecollide(obj, players_sprite, False)):
                obj.rect.x = randint(0, 19) * 20
                obj.rect.y = randint(3, 19) * 20
            player_testi = Player(2)
            player_testi.rect.x = x
            player_testi.rect.y = y
            players.append(player_testi)
            players_sprite.add(player_testi)
        players_sprite.draw(screen)
        max_score = score(score_, max_score)
        screen.blit(player_test.image, player_test.rect)
        this = pygame.sprite.spritecollide(player_test, players_sprite, True)
        screen.blit(obj.image, obj.rect)
        if len(this):
            active = False
    else:
        direct = 'up'
        score_ = 0
        screen.fill('pink')
        players = []
        player_test.rect.x = 100
        player_test.rect.y = 100
        players_sprite = pygame.sprite.Group()
        players.append(player_test)
        obj = Player()
        obj.rect.x = 100
        obj.rect.y = 60
        font = pygame.font.Font(None, 30)
        text = font.render('Press space to run', False, 'Black')
        text_rec = text.get_rect(center = (200, 50))
        text_score = font.render(f'Max score: {max_score}', False, 'Black')
        text_score_rec = text_score.get_rect(center = (200, 80))
        screen.blit(text, text_rec)
        screen.blit(text_score, text_score_rec)
    clock.tick(60) 
    pygame.display.update()

