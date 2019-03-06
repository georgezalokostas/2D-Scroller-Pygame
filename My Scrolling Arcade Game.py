import pygame
import random

pygame.init()

clock = pygame.time.Clock()
# Settings
FPS = 30
screen_Width = 700
screen_Height = 700
background_moving_speed = 4
bulletDelay = 150
enemyBulletDelay = 400
finalbossBulletDelay = 200
player_width = 80
player_height = 80
enemy_width = 80
enemy_height = 80
player_speed = 5.5
bullet_speed = 10
bullet_size = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (128, 255, 128)
YELLOW = (248, 203, 24)
playerWalkCount = 0
enemy_randomY_movement = 0

screen = pygame.display.set_mode((screen_Width, screen_Height))
screen_rect = screen.get_rect()
pygame.display.set_caption("My Scrolling Arcade Game")

now = pygame.time.get_ticks()
oldtime = now
now_enemy_movement = pygame.time.get_ticks()
oldtime_enemy_movement = now_enemy_movement
now_enemy_shoot = pygame.time.get_ticks()
oldtime_enemy_shoot = now_enemy_shoot

PAUSE, DEAD, WON, STARTING_SCREEN, DIFFICULTY, RUNNING_EASY, RUNNING_NORMAL, RUNNING_HARD, HELP = 0, 1, 2, 3, 4, 5, 6, 7, 8
state = STARTING_SCREEN
current_state = state

pause_font = pygame.font.SysFont("Serif", 35, True, False)
score_font = pygame.font.SysFont("Serif", 30, True, False)

background_x = 0
background_y = -4622 + screen_Height

starting_screen = pygame.image.load('sprites/start.png').convert()
difficulty_screen = pygame.image.load('sprites/menu.png').convert()
help_screen = pygame.image.load('sprites/help.png').convert()
background = pygame.image.load('sprites/level1.png').convert()
heart = pygame.image.load('sprites/heart.png').convert()
heart.set_colorkey(WHITE)
death = pygame.image.load('sprites/death.jpg').convert()
won = pygame.image.load('sprites/results.jpg').convert()
medkitimage = pygame.image.load('sprites/medkit.png').convert()
medkitimage.set_colorkey(WHITE)
player_standing_up = pygame.image.load('sprites/hero-up-1.png').convert()
player_standing_up.set_colorkey(GREEN)
player_standing_left = pygame.image.load('sprites/hero-left-1.png').convert()
player_standing_left.set_colorkey(GREEN)
player_standing_down = pygame.image.load('sprites/hero-down-1.png').convert()
player_standing_down.set_colorkey(GREEN)
player_standing_left = pygame.image.load('sprites/hero-left-1.png').convert()
player_standing_left.set_colorkey(GREEN)
player_standing_right = pygame.image.load('sprites/hero-right-1.png').convert()
player_standing_right.set_colorkey(GREEN)
player_standing_topright = pygame.image.load('sprites/hero-upperright-1.png').convert()
player_standing_topright.set_colorkey(GREEN)
player_standing_topleft = pygame.image.load('sprites/hero-upperleft-1.png').convert()
player_standing_topleft.set_colorkey(GREEN)
player_standing_bottomright = pygame.image.load('sprites/hero-bottomright-1.png').convert()
player_standing_bottomright.set_colorkey(GREEN)
player_standing_bottomleft = pygame.image.load('sprites/hero-bottomleft-1.png').convert()
player_standing_bottomleft.set_colorkey(GREEN)
enemy_walk = [pygame.image.load('sprites/enemy-walk1.png').convert(),
              pygame.image.load('sprites/enemy-walk2.png').convert(),
              pygame.image.load('sprites/enemy-walk3.png').convert(),
              pygame.image.load('sprites/enemy-walk4.png').convert(),
              pygame.image.load('sprites/enemy-walk5.png').convert()]
enemy_walk[0].set_colorkey(GREEN)
enemy_walk[1].set_colorkey(GREEN)
enemy_walk[2].set_colorkey(GREEN)
enemy_walk[3].set_colorkey(GREEN)
enemy_walk[4].set_colorkey(GREEN)
player_up = [pygame.image.load('sprites/hero-up-1.png').convert(),
             pygame.image.load('sprites/hero-up-2.png').convert(),
             pygame.image.load('sprites/hero-up-3.png').convert(),
             pygame.image.load('sprites/hero-up-4.png').convert(),
             pygame.image.load('sprites/hero-up-5.png').convert()]
player_up[0].set_colorkey(GREEN)
player_up[1].set_colorkey(GREEN)
player_up[2].set_colorkey(GREEN)
player_up[3].set_colorkey(GREEN)
player_up[4].set_colorkey(GREEN)
player_down = [pygame.image.load('sprites/hero-down-1.png').convert(),
               pygame.image.load('sprites/hero-down-2.png').convert(),
               pygame.image.load('sprites/hero-down-3.png').convert(),
               pygame.image.load('sprites/hero-down-4.png').convert(),
               pygame.image.load('sprites/hero-down-5.png').convert()]
player_down[0].set_colorkey(GREEN)
player_down[1].set_colorkey(GREEN)
player_down[2].set_colorkey(GREEN)
player_down[3].set_colorkey(GREEN)
player_down[4].set_colorkey(GREEN)
player_right = [pygame.image.load('sprites/hero-right-1.png').convert(),
                pygame.image.load('sprites/hero-right-2.png').convert(),
                pygame.image.load('sprites/hero-right-3.png').convert(),
                pygame.image.load('sprites/hero-right-4.png').convert(),
                pygame.image.load('sprites/hero-right-5.png').convert()]
player_right[0].set_colorkey(GREEN)
player_right[1].set_colorkey(GREEN)
player_right[2].set_colorkey(GREEN)
player_right[3].set_colorkey(GREEN)
player_right[4].set_colorkey(GREEN)
player_left = [pygame.image.load('sprites/hero-left-1.png').convert(),
               pygame.image.load('sprites/hero-left-2.png').convert(),
               pygame.image.load('sprites/hero-left-3.png').convert(),
               pygame.image.load('sprites/hero-left-4.png').convert(),
               pygame.image.load('sprites/hero-left-5.png').convert()]
player_left[0].set_colorkey(GREEN)
player_left[1].set_colorkey(GREEN)
player_left[2].set_colorkey(GREEN)
player_left[3].set_colorkey(GREEN)
player_left[4].set_colorkey(GREEN)
player_bottom_left = [pygame.image.load('sprites/hero-bottomleft-1.png').convert(),
                      pygame.image.load('sprites/hero-bottomleft-2.png').convert(),
                      pygame.image.load('sprites/hero-bottomleft-3.png').convert(),
                      pygame.image.load('sprites/hero-bottomleft-4.png').convert(),
                      pygame.image.load('sprites/hero-bottomleft-5.png').convert()]
player_bottom_left[0].set_colorkey(GREEN)
player_bottom_left[1].set_colorkey(GREEN)
player_bottom_left[2].set_colorkey(GREEN)
player_bottom_left[3].set_colorkey(GREEN)
player_bottom_left[4].set_colorkey(GREEN)
player_bottom_right = [pygame.image.load('sprites/hero-bottomright-1.png').convert(),
                       pygame.image.load('sprites/hero-bottomright-2.png').convert(),
                       pygame.image.load('sprites/hero-bottomright-3.png').convert(),
                       pygame.image.load('sprites/hero-bottomright-4.png').convert(),
                       pygame.image.load('sprites/hero-bottomright-5.png').convert()]
player_bottom_right[0].set_colorkey(GREEN)
player_bottom_right[1].set_colorkey(GREEN)
player_bottom_right[2].set_colorkey(GREEN)
player_bottom_right[3].set_colorkey(GREEN)
player_bottom_right[4].set_colorkey(GREEN)
player_upper_left = [pygame.image.load('sprites/hero-upperleft-1.png').convert(),
                     pygame.image.load('sprites/hero-upperleft-2.png').convert(),
                     pygame.image.load('sprites/hero-upperleft-3.png').convert(),
                     pygame.image.load('sprites/hero-upperleft-4.png').convert(),
                     pygame.image.load('sprites/hero-upperleft-5.png').convert()]
player_upper_left[0].set_colorkey(GREEN)
player_upper_left[1].set_colorkey(GREEN)
player_upper_left[2].set_colorkey(GREEN)
player_upper_left[3].set_colorkey(GREEN)
player_upper_left[4].set_colorkey(GREEN)
player_upper_right = [pygame.image.load('sprites/hero-upperright-1.png').convert(),
                      pygame.image.load('sprites/hero-upperright-2.png').convert(),
                      pygame.image.load('sprites/hero-upperright-3.png').convert(),
                      pygame.image.load('sprites/hero-upperright-4.png').convert(),
                      pygame.image.load('sprites/hero-upperright-5.png').convert()]
player_upper_right[0].set_colorkey(GREEN)
player_upper_right[1].set_colorkey(GREEN)
player_upper_right[2].set_colorkey(GREEN)
player_upper_right[3].set_colorkey(GREEN)
player_upper_right[4].set_colorkey(GREEN)


class Player(object):
    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.facing_left = False
        self.facing_right = False
        self.facing_up = False
        self.facing_down = False
        self.facing_up_left = False
        self.facing_up_right = False
        self.facing_down_left = False
        self.facing_down_right = False
        self.standing = True
        self.health = 1
        self.score = 0
        self.easyhighscore = 0
        self.normalhighscore = 0
        self.experthighscore = 0

    def hit(self):
        self.health -= 1
        self.score -= 50

    def draw(self, screen):
        global playerWalkCount

        if playerWalkCount + 1 >= 15:
            playerWalkCount = 0

        if facing_left:
            screen.blit(player_left[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_right:
            screen.blit(player_right[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_up:
            screen.blit(player_up[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_down:
            screen.blit(player_down[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_up_left:
            screen.blit(player_upper_left[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_up_right:
            screen.blit(player_upper_right[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_down_left:
            screen.blit(player_bottom_left[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        elif facing_down_right:
            screen.blit(player_bottom_right[playerWalkCount // 3], (player.x, player.y))
            playerWalkCount += 1
        else:
            screen.blit(player_standing_up, (player.x, player.y))


class Enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveLeft = False
        self.moveRight = True
        self.standing = True
        self.speed = 5
        self.health = 3
        self.enemyWalkCount = 0

    def draw(self, screen):

        if self.enemyWalkCount + 1 >= 15:
            self.enemyWalkCount = 0
        screen.blit(enemy_walk[self.enemyWalkCount // 4], (self.x, self.y))
        self.enemyWalkCount += 1

    def hit(self):
        self.health -= 1

    def updateboss(self):
        global enemy_randomY_movement
        enemy_randomY_movement = 0
        global now_enemy_movement, oldtime_enemy_movement
        if self.moveRight:
            if (self.x + enemy_width <= 690):
                self.moveRight = True
                self.moveLeft = False
                self.x += self.speed
            else:
                self.moveLeft = True
                self.moveRight = False
                self.x -= self.speed

        elif self.moveLeft:
            if (self.x > 20):
                self.moveRight = False
                self.moveLeft = True
                self.x -= self.speed

            else:
                self.moveRight = True
                self.moveLeft = False
                self.x += self.speed

        now_enemy_movement = pygame.time.get_ticks()

    def update(self):
        global enemy_randomY_movement
        enemy_randomY_movement = 0
        global now_enemy_movement, oldtime_enemy_movement
        if self.moveRight:
            if (self.x + enemy_width <= 690):
                self.moveRight = True
                self.moveLeft = False
                self.x += self.speed
            else:
                self.moveLeft = True
                self.moveRight = False
                self.x -= self.speed

        elif self.moveLeft:
            if (self.x > 20):
                self.moveRight = False
                self.moveLeft = True
                self.x -= self.speed

            else:
                self.moveRight = True
                self.moveLeft = False
                self.x += self.speed

        now_enemy_movement = pygame.time.get_ticks()

        if now_enemy_movement - oldtime_enemy_movement >= 200:
            oldtime_enemy_movement = now_enemy_movement
            self.y += random.randint(-2, 3) * 3


class Projectile(object):
    def __init__(self, x, y, radius, color, bullet_speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.bullet_speed = bullet_speed
        self.x_speed = 0
        self.y_speed = 0

        self.check()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def check(self):
        global bullet_speed

        if (0 < self.x < screen_Width) or (0 < self.y < screen_Height):

            if facing_up_right:
                self.y_speed = -bullet_speed - 2
                self.x_speed = bullet_speed + 2
            elif facing_up_left:
                self.y_speed = -bullet_speed - 2
                self.x_speed = -bullet_speed - 2
            elif facing_down_right:
                self.y_speed = bullet_speed + 2
                self.x_speed = bullet_speed + 2
            elif facing_down_left:
                self.y_speed = bullet_speed + 2
                self.x_speed = -bullet_speed - 2
            elif facing_up:
                self.y_speed = -bullet_speed - 2
            elif facing_left:
                self.x_speed = -bullet_speed - 4
            elif facing_right:
                self.x_speed = bullet_speed + 4
            elif facing_down:
                self.y_speed = bullet_speed + 3
            elif standing:
                self.y_speed = -bullet_speed - 2
            else:
                self.x_speed = 0
                self.y_speed = 0


class Medkit(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        screen.blit(medkitimage, (self.x, self.y))


class ProjectileEnemy(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.bullet_speed = bullet_speed
        self.x_speed = 0
        self.y_speed = bullet_speed + 3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def enemy_shoot(object):
    enemybullets.append(ProjectileEnemy(round(object.x + 35), object.y + 20, bullet_size, YELLOW))


def player_shoot():
    # WE SHOOT FROM THE GUN'S POINT BASED ON WHERE WE'RE FACING
    if facing_up:
        bullets.append(
            Projectile(round(player.x + player.width - 25), round(player.y), bullet_size, YELLOW, bullet_speed))
    if facing_down:
        bullets.append(
            Projectile(round(player.x + player.width / 2 - 15), round(player.y + player_height), bullet_size, YELLOW,
                       bullet_speed))
    if facing_left:
        bullets.append(
            Projectile(round(player.x), round(player.y + player_width / 2 - 10), bullet_size, YELLOW, bullet_speed))
    if facing_right:
        bullets.append(
            Projectile(round(player.x + player_width), round(player.y + player_width / 2 + 5), bullet_size, YELLOW,
                       bullet_speed))
    if facing_up_left:
        bullets.append(Projectile(round(player.x), round(player.y), bullet_size, YELLOW, bullet_speed))
    if facing_up_right:
        bullets.append(
            Projectile(round(player.x + player.width - 5), round(player.y), bullet_size, YELLOW, bullet_speed))
    if facing_down_left:
        bullets.append(
            Projectile(round(player.x), round(player.y + player_height - 5), bullet_size, YELLOW, bullet_speed))
    if facing_down_right:
        bullets.append(
            Projectile(round(player.x + player.width), round(player.y + player_height - 10), bullet_size, YELLOW,
                       bullet_speed))
    if standing:
        bullets.append(
            Projectile(round(player.x + player.width - 25), round(player.y), bullet_size, YELLOW, bullet_speed))


def reloadlevel():
    player.x = (screen_Width / 2 - 30)
    player.y = (screen_Height - 200)
    enemies.append(Enemy((screen_Width / 2 - 100), (screen_Height - 650), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 3), (screen_Height - 800), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 8), (screen_Height - 920), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 2), (screen_Height - 990), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 4), (screen_Height - 1060), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 6), (screen_Height - 1115), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width - 50), (screen_Height - 1180), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 2), (screen_Height - 1290), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 4), (screen_Height - 1290), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 8), (screen_Height - 1450), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 3), (screen_Height - 1620), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 2), (screen_Height - 1750), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 4), (screen_Height - 1820), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 6), (screen_Height - 1820), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 2), (screen_Height - 1900), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width), (screen_Height - 1950), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 4), (screen_Height - 2100), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 3), (screen_Height - 2350), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 4), (screen_Height - 2540), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 2), (screen_Height - 2580), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width), (screen_Height - 3000), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 9), (screen_Height - 3090), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 6), (screen_Height - 3250), enemy_width, enemy_height))
    enemies.append(Enemy((screen_Width / 2), (screen_Height - 3300), enemy_width, enemy_height))
    finalboss = Enemy((screen_Width / 2), (screen_Height - 4650), enemy_width, enemy_height)
    finalboss.health = 20
    finalboss.speed = 8
    finalbosslist.append(finalboss)

    medkits.append(Medkit((screen_Width / 6), (screen_Height - 1115), 50, 50))
    medkits.append(Medkit((screen_Width - 50), (screen_Height - 1940), 50, 50))
    medkits.append(Medkit((screen_Width / 6), (screen_Height - 2650), 50, 50))
    medkits.append(Medkit((screen_Width - 50), (screen_Height - 3400), 50, 50))
    medkits.append(Medkit((screen_Width / 6), (screen_Height - 3860), 50, 50))
    medkits.append(Medkit((screen_Width - 200), (screen_Height - 4000), 50, 50))




def clearlevel():
    enemies.clear()
    bullets.clear()
    enemybullets.clear()
    medkits.clear()
    finalbosslist.clear()


enemies = []
bullets = []
enemybullets = []
medkits = []
finalbosslist = []
player = Player((screen_Width / 2 - 30), (screen_Height - 200), player_width, player_height)

running = True
while running:

    clock.tick(FPS)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_p: state = PAUSE
            if event.key == pygame.K_c: state = current_state
            if event.key == pygame.K_RETURN: state = DIFFICULTY
            if event.key == pygame.K_1:
                clearlevel()
                reloadlevel()
                player.health = 10
                player.score = 0
                background_x = 0
                background_y = -4622 + screen_Height
                state = RUNNING_EASY
                current_state = state
            if event.key == pygame.K_2:
                clearlevel()
                reloadlevel()
                player.health = 7
                player.score = 0
                background_x = 0
                background_y = -4622 + screen_Height
                state = RUNNING_NORMAL
                current_state = state
            if event.key == pygame.K_3:
                clearlevel()
                reloadlevel()
                player.health = 3
                player.score = 0
                background_x = 0
                background_y = -4622 + screen_Height
                state = RUNNING_HARD
                current_state = state
            if event.key == pygame.K_h: state = HELP

    if state == STARTING_SCREEN:

        screen.blit(starting_screen, (0, 0))
        pygame.display.update()

    elif state == DIFFICULTY:
        current_state = DIFFICULTY

        screen.blit(difficulty_screen, (0, 0))
        easyhighscore = score_font.render('Highscore: ' + str(player.easyhighscore), True, WHITE)
        screen.blit(easyhighscore, (screen_Width / 2 + 120, 90))
        normalhighscore = score_font.render('Highscore: ' + str(player.normalhighscore), True, WHITE)
        screen.blit(normalhighscore, (screen_Width / 2 + 120, 310))
        experthighscore = score_font.render('Highscore: ' + str(player.experthighscore), True, WHITE)
        screen.blit(experthighscore, (screen_Width / 2 + 130, 520))
        pygame.display.update()

    elif state == RUNNING_EASY:
        current_state = RUNNING_EASY

        if keys[pygame.K_LEFT] and keys[pygame.K_UP] and player.x > -5 and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed - 1.2
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed

                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed

            player.x -= player_speed - 1.2

            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = True
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

            enemy_moving = False

        elif keys[pygame.K_UP] and keys[
            pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed - 1.2
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed

                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed
            player.x += player_speed - 1.2

            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = True
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_DOWN] and keys[
            pygame.K_LEFT] and player.x >= 0 and player.y < screen_Height - player.height - player_speed:
            player.x -= player_speed - 1.2
            player.y += player_speed - 1.2
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = True
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_DOWN] and keys[
            pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed and player.y < screen_Height - player.height - player_speed:
            player.x += player_speed - 1.2
            player.y += player_speed - 1.2
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = True
            standing = False
            player.draw(screen)

        elif keys[pygame.K_LEFT] and player.x > -5:
            player.x -= player_speed
            facing_left = True
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed:
            player.x += player_speed
            facing_left = False
            facing_right = True
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_UP] and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed
                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed

            facing_left = False
            facing_right = False
            facing_up = True
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            playerWalkCount += 1

            player.draw(screen)

        elif keys[pygame.K_DOWN] and player.y < screen_Height - player.height - player_speed:
            player.y += player_speed
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = True
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        else:
            playerWalkCount = 0
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = True

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - oldtime >= bulletDelay:
                oldtime = now
                if len(bullets) < 5:
                    player_shoot()

        screen.blit(background, (background_x, background_y))
        player.draw(screen)

        for m in medkits:
            m.draw(screen)

        for f in finalbosslist:
            for eb in enemybullets:
                if (eb.y < player.y + player.height and eb.y > player.y) and (
                        eb.x > player.x and eb.x < player.x + player.width):
                    player.hit()

                    enemybullets.pop(enemybullets.index(eb))

        for f in finalbosslist:
            f.updateboss()
            f.draw(screen)
            for bullet in bullets:
                if (bullet.y < f.y + f.height and bullet.y > f.y) and (
                        bullet.x > f.x and bullet.x < f.x + enemy.width):
                    f.hit()
                    bullets.pop(bullets.index(bullet))
                    if f.health == 0:
                        finalbosslist.pop(finalbosslist.index(f))
                        player.score += 100

            if (f.y > screen_Height):
                finalbosslist.pop(finalbosslist.index(f))
            if (player.y - f.y < 400 and abs(player.x - f.x) < 40):
                now_enemy_shoot = pygame.time.get_ticks()
                if now_enemy_shoot - oldtime_enemy_shoot >= finalbossBulletDelay:
                    oldtime_enemy_shoot = now_enemy_shoot
                    enemy_shoot(f)
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
            for bullet in bullets:
                if (bullet.y < enemy.y + enemy.height and bullet.y > enemy.y) and (
                        bullet.x > enemy.x and bullet.x < enemy.x + enemy.width):
                    enemy.hit()
                    bullets.pop(bullets.index(bullet))
                    if enemy.health == 0:
                        enemies.pop(enemies.index(enemy))
                        player.score += 100

            if (enemy.y > screen_Height):
                enemies.pop(enemies.index(enemy))
            if (player.y - enemy.y < 400 and abs(player.x - enemy.x) < 40):
                now_enemy_shoot = pygame.time.get_ticks()
                if now_enemy_shoot - oldtime_enemy_shoot >= enemyBulletDelay:
                    oldtime_enemy_shoot = now_enemy_shoot
                    enemy_shoot(enemy)

            for eb in enemybullets:
                if (eb.y < player.y + player.height and eb.y > player.y) and (
                        eb.x > player.x and eb.x < player.x + player.width):
                    player.hit()

                    enemybullets.pop(enemybullets.index(eb))

        # REMOVE THE BULLET IF IT GOES OUT OF BOUNDS
        for bullet in bullets:
            bullet.x += bullet.x_speed
            bullet.y += bullet.y_speed
            if (bullet.x < -5 or bullet.x > 705) or (bullet.y > 705 or bullet.y < -5):
                bullets.pop(bullets.index(bullet))
            bullet.draw(screen)
        # MOVE ENEMY BULLETS
        for eb in enemybullets:
            eb.x += eb.x_speed
            eb.y += eb.y_speed
            eb.draw(screen)

        for medkit in medkits:
            if (medkit.y < player.y + player_height and medkit.y > player.y) and (
                    medkit.x > player.x and medkit.x < player.x + player_width):
                player.health += 1
                medkits.pop(medkits.index(medkit))

        if player.easyhighscore <= player.score:
            player.easyhighscore = player.score
        if player.score < 0:
            player.score = 0
        if player.health == 0:
            player.health = 0
            state = DEAD

        score = score_font.render('Score: ' + str(player.score), True, WHITE)
        screen.blit(score, (screen_Width - 160, 0))
        easyhighscore = score_font.render('Highscore: ' + str(player.easyhighscore), True, WHITE)
        screen.blit(easyhighscore, (screen_Width - 400, 0))
        lives = score_font.render(str(player.health), True, WHITE)
        screen.blit(heart, (0, 0))
        screen.blit(lives, (40, 0))

        # WON SCREEN
        if (player.y < 10):
            if (player.x > 270 and player.x < 340):
                if len(finalbosslist) == 0:
                    state = WON

        pygame.display.update()

    elif state == RUNNING_NORMAL:
        current_state = RUNNING_NORMAL

        if keys[pygame.K_LEFT] and keys[pygame.K_UP] and player.x > -5 and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed - 1.2
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed

                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed

            player.x -= player_speed - 1.2

            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = True
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

            enemy_moving = False

        elif keys[pygame.K_UP] and keys[
            pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed - 1.2
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed

                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed
            player.x += player_speed - 1.2

            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = True
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_DOWN] and keys[
            pygame.K_LEFT] and player.x >= 0 and player.y < screen_Height - player.height - player_speed:
            player.x -= player_speed - 1.2
            player.y += player_speed - 1.2
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = True
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_DOWN] and keys[
            pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed and player.y < screen_Height - player.height - player_speed:
            player.x += player_speed - 1.2
            player.y += player_speed - 1.2
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = True
            standing = False
            player.draw(screen)

        elif keys[pygame.K_LEFT] and player.x > -5:
            player.x -= player_speed
            facing_left = True
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed:
            player.x += player_speed
            facing_left = False
            facing_right = True
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_UP] and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed
                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed

            facing_left = False
            facing_right = False
            facing_up = True
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            playerWalkCount += 1

            player.draw(screen)

        elif keys[pygame.K_DOWN] and player.y < screen_Height - player.height - player_speed:
            player.y += player_speed
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = True
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        else:
            playerWalkCount = 0
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = True

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - oldtime >= bulletDelay:
                oldtime = now
                if len(bullets) < 5:
                    player_shoot()

        screen.blit(background, (background_x, background_y))
        player.draw(screen)

        for m in medkits:
            m.draw(screen)

        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
            for bullet in bullets:
                if (bullet.y < enemy.y + enemy.height and bullet.y > enemy.y) and (
                        bullet.x > enemy.x and bullet.x < enemy.x + enemy.width):
                    enemy.hit()
                    bullets.pop(bullets.index(bullet))
                    if enemy.health == 0:
                        enemies.pop(enemies.index(enemy))
                        player.score += 100

            if (enemy.y > screen_Height):
                enemies.pop(enemies.index(enemy))
            if (player.y - enemy.y < 400 and abs(player.x - enemy.x) < 40):
                now_enemy_shoot = pygame.time.get_ticks()
                if now_enemy_shoot - oldtime_enemy_shoot >= enemyBulletDelay:
                    oldtime_enemy_shoot = now_enemy_shoot
                    enemy_shoot(enemy)

            for eb in enemybullets:
                if (eb.y < player.y + player.height and eb.y > player.y) and (
                        eb.x > player.x and eb.x < player.x + player.width):
                    player.hit()

                    enemybullets.pop(enemybullets.index(eb))

        for f in finalbosslist:
            f.updateboss()
            f.draw(screen)
            for bullet in bullets:
                if (bullet.y < f.y + f.height and bullet.y > f.y) and (
                        bullet.x > f.x and bullet.x < f.x + enemy.width):
                    f.hit()
                    bullets.pop(bullets.index(bullet))
                    if f.health == 0:
                        finalbosslist.pop(finalbosslist.index(f))
                        player.score += 100

            if (f.y > screen_Height):
                finalbosslist.pop(finalbosslist.index(f))
            if (player.y - f.y < 400 and abs(player.x - f.x) < 40):
                now_enemy_shoot = pygame.time.get_ticks()
                if now_enemy_shoot - oldtime_enemy_shoot >= finalbossBulletDelay:
                    oldtime_enemy_shoot = now_enemy_shoot
                    enemy_shoot(f)
        for f in finalbosslist:
            for eb in enemybullets:
                if (eb.y < player.y + player.height and eb.y > player.y) and (
                        eb.x > player.x and eb.x < player.x + player.width):
                    player.hit()

                    enemybullets.pop(enemybullets.index(eb))


        # REMOVE THE BULLET IF IT GOES OUT OF BOUNDS
        for bullet in bullets:
            bullet.x += bullet.x_speed
            bullet.y += bullet.y_speed
            if (bullet.x < -5 or bullet.x > 705) or (bullet.y > 705 or bullet.y < -5):
                bullets.pop(bullets.index(bullet))
            bullet.draw(screen)
        # MOVE ENEMY BULLETS
        for eb in enemybullets:
            eb.x += eb.x_speed
            eb.y += eb.y_speed
            eb.draw(screen)

        for medkit in medkits:
            if (medkit.y < player.y + player_height and medkit.y > player.y) and (
                    medkit.x > player.x and medkit.x < player.x + player_width):
                player.health += 1
                medkits.pop(medkits.index(medkit))

        if player.normalhighscore <= player.score:
            player.normalhighscore = player.score
        if player.score < 0:
            player.score = 0
        if player.health == 0:
            player.health = 0
            state = DEAD

        score = score_font.render('Score: ' + str(player.score), True, WHITE)
        screen.blit(score, (screen_Width - 160, 0))
        normalhighscore = score_font.render('Highscore: ' + str(player.normalhighscore), True, WHITE)
        screen.blit(normalhighscore, (screen_Width - 400, 0))
        lives = score_font.render(str(player.health), True, WHITE)
        screen.blit(heart, (0, 0))
        screen.blit(lives, (40, 0))

        # WON SCREEN
        if (player.y < 10):
            if (player.x > 270 and player.x < 340):
                if len(finalbosslist) == 0:
                    state = WON

        pygame.display.update()

    elif state == RUNNING_HARD:
        current_state = RUNNING_HARD
        medkits.clear()

        if keys[pygame.K_LEFT] and keys[pygame.K_UP] and player.x > -5 and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed - 1.2
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed

                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed

            player.x -= player_speed - 1.2

            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = True
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

            enemy_moving = False

        elif keys[pygame.K_UP] and keys[
            pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed - 1.2
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed

                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed
            player.x += player_speed - 1.2

            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = True
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_DOWN] and keys[
            pygame.K_LEFT] and player.x >= 0 and player.y < screen_Height - player.height - player_speed:
            player.x -= player_speed - 1.2
            player.y += player_speed - 1.2
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = True
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_DOWN] and keys[
            pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed and player.y < screen_Height - player.height - player_speed:
            player.x += player_speed - 1.2
            player.y += player_speed - 1.2
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = True
            standing = False
            player.draw(screen)

        elif keys[pygame.K_LEFT] and player.x > -5:
            player.x -= player_speed
            facing_left = True
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_RIGHT] and player.x < screen_Width - player.width - player_speed:
            player.x += player_speed
            facing_left = False
            facing_right = True
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        elif keys[pygame.K_UP] and player.y >= 0:
            if player.y > 400:
                player.y -= player_speed
            if player.y < 400:
                if background_y < 0:
                    background_y += background_moving_speed
                    for enemy in enemies:
                        enemy.y += background_moving_speed
                    for medkit in medkits:
                        medkit.y += background_moving_speed
                    for f in finalbosslist:
                        f.y += background_moving_speed
                if background_y > 0:
                    background_y = 0
                if background_y == 0:
                    player.y -= player_speed

            facing_left = False
            facing_right = False
            facing_up = True
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            playerWalkCount += 1

            player.draw(screen)

        elif keys[pygame.K_DOWN] and player.y < screen_Height - player.height - player_speed:
            player.y += player_speed
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = True
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = False
            player.draw(screen)

        else:
            playerWalkCount = 0
            facing_left = False
            facing_right = False
            facing_up = False
            facing_down = False
            facing_up_left = False
            facing_up_right = False
            facing_down_left = False
            facing_down_right = False
            standing = True

        if keys[pygame.K_SPACE]:
            now = pygame.time.get_ticks()
            if now - oldtime >= bulletDelay:
                oldtime = now
                if len(bullets) < 5:
                    player_shoot()

        screen.blit(background, (background_x, background_y))
        player.draw(screen)

        for f in finalbosslist:
            f.updateboss()
            f.draw(screen)
            for bullet in bullets:
                if (bullet.y < f.y + f.height and bullet.y > f.y) and (
                        bullet.x > f.x and bullet.x < f.x + enemy.width):
                    f.hit()
                    bullets.pop(bullets.index(bullet))
                    if f.health == 0:
                        finalbosslist.pop(finalbosslist.index(f))
                        player.score += 100

            if (f.y > screen_Height):
                finalbosslist.pop(finalbosslist.index(f))
            if (player.y - f.y < 400 and abs(player.x - f.x) < 40):
                now_enemy_shoot = pygame.time.get_ticks()
                if now_enemy_shoot - oldtime_enemy_shoot >= finalbossBulletDelay:
                    oldtime_enemy_shoot = now_enemy_shoot
                    enemy_shoot(f)

        for f in finalbosslist:
            for eb in enemybullets:
                if (eb.y < player.y + player.height and eb.y > player.y) and (
                        eb.x > player.x and eb.x < player.x + player.width):
                    player.hit()

                    enemybullets.pop(enemybullets.index(eb))


        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
            for bullet in bullets:
                if (bullet.y < enemy.y + enemy.height and bullet.y > enemy.y) and (
                        bullet.x > enemy.x and bullet.x < enemy.x + enemy.width):
                    enemy.hit()
                    bullets.pop(bullets.index(bullet))
                    if enemy.health == 0:
                        enemies.pop(enemies.index(enemy))
                        player.score += 100

            if (enemy.y > screen_Height):
                enemies.pop(enemies.index(enemy))
            if (player.y - enemy.y < 400 and abs(player.x - enemy.x) < 40):
                now_enemy_shoot = pygame.time.get_ticks()
                if now_enemy_shoot - oldtime_enemy_shoot >= enemyBulletDelay:
                    oldtime_enemy_shoot = now_enemy_shoot
                    enemy_shoot(enemy)

            for eb in enemybullets:
                if (eb.y < player.y + player.height and eb.y > player.y) and (
                        eb.x > player.x and eb.x < player.x + player.width):
                    player.hit()

                    enemybullets.pop(enemybullets.index(eb))

        # REMOVE THE BULLET IF IT GOES OUT OF BOUNDS
        for bullet in bullets:
            bullet.x += bullet.x_speed
            bullet.y += bullet.y_speed
            if (bullet.x < -5 or bullet.x > 705) or (bullet.y > 705 or bullet.y < -5):
                bullets.pop(bullets.index(bullet))
            bullet.draw(screen)
        # MOVE ENEMY BULLETS
        for eb in enemybullets:
            eb.x += eb.x_speed
            eb.y += eb.y_speed
            eb.draw(screen)

        if player.experthighscore <= player.score:
            player.experthighscore = player.score
        if player.score < 0:
            player.score = 0
        if player.health == 0:
            player.health = 0
            state = DEAD

        score = score_font.render('Score: ' + str(player.score), True, WHITE)
        screen.blit(score, (screen_Width - 160, 0))
        experthighscore = score_font.render('Highscore: ' + str(player.experthighscore), True, WHITE)
        screen.blit(experthighscore, (screen_Width - 400, 0))
        lives = score_font.render(str(player.health), True, WHITE)
        screen.blit(heart, (0, 0))
        screen.blit(lives, (40, 0))

        # WON SCREEN
        if (player.y < 10):
            if (player.x > 270 and player.x < 340):
                if len(finalbosslist) == 0:
                    state = WON

        pygame.display.update()

    elif state == PAUSE:
        text1 = pause_font.render('Pause', True, WHITE)
        screen.blit(text1, (screen_Width / 2 - 40, screen_Height / 2 - 150))
        pygame.display.update()

    elif state == DEAD:
        screen.blit(death, (0, 0))
        if current_state == RUNNING_EASY:
            if player.easyhighscore <= player.score:
                player.easyhighscore = player.score
            easyhighscore = score_font.render('Highscore: ' + str(player.easyhighscore), True, WHITE)
            screen.blit(easyhighscore, (screen_Width / 2 - 80, 500))
            score = score_font.render('Score: ' + str(player.score), True, WHITE)
            screen.blit(score, (screen_Width / 2 - 80, 450))
        if current_state == RUNNING_NORMAL:
            if player.normalhighscore <= player.score:
                player.normalhighscore = player.score
            normalhighscore = score_font.render('Highscore: ' + str(player.normalhighscore), True, WHITE)
            screen.blit(normalhighscore, (screen_Width / 2 - 80, 500))
            score = score_font.render('Score: ' + str(player.score), True, WHITE)
            screen.blit(score, (screen_Width / 2 - 80, 450))
        if current_state == RUNNING_HARD:
            if player.experthighscore <= player.score:
                player.experthighscore = player.score
            experthighscore = score_font.render('Highscore: ' + str(player.experthighscore), True, WHITE)
            screen.blit(experthighscore, (screen_Width / 2 - 80, 500))
            score = score_font.render('Score: ' + str(player.score), True, WHITE)
            screen.blit(score, (screen_Width / 2 - 80, 450))

        pygame.display.update()

    elif state == WON:
        screen.blit(won, (0, 0))
        if current_state == RUNNING_EASY:
            if player.easyhighscore <= player.score:
                player.easyhighscore = player.score
            easyhighscore = score_font.render('Highscore: ' + str(player.easyhighscore), True, WHITE)
            screen.blit(easyhighscore, (screen_Width / 2 - 80, 500))
            score = score_font.render('Score: ' + str(player.score), True, WHITE)
            screen.blit(score, (screen_Width / 2 - 80, 450))
        if current_state == RUNNING_NORMAL:
            if player.normalhighscore <= player.score:
                player.normalhighscore = player.score
            normalhighscore = score_font.render('Highscore: ' + str(player.normalhighscore), True, WHITE)
            screen.blit(normalhighscore, (screen_Width / 2 - 80, 500))
            score = score_font.render('Score: ' + str(player.score), True, WHITE)
            screen.blit(score, (screen_Width / 2 - 80, 450))
        if current_state == RUNNING_HARD:
            if player.experthighscore <= player.score:
                player.experthighscore = player.score
            experthighscore = score_font.render('Highscore: ' + str(player.experthighscore), True, WHITE)
            screen.blit(experthighscore, (screen_Width / 2 - 80, 500))
        score = score_font.render('Score: ' + str(player.score), True, WHITE)
        screen.blit(score, (screen_Width / 2 - 80, 450))
        pygame.display.update()

    elif state == HELP:
        screen.blit(help_screen, (0, 0))
        pygame.display.update()


pygame.display.quit()
pygame.quit()
