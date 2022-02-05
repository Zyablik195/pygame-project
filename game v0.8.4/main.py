import pygame
import math
from random import randint, choice
from levels import level1
from functions import *


def update_fps():
    if fps_on:
        fps = str(int(clock.get_fps()))
        fps_text = font3.render(fps, 1, pygame.Color("coral"))
        return fps_text
    return font3.render('', 1, pygame.Color("coral"))


def create_player(character):
    global player
    if character == 'aim':
        player = Aim(player_x, player_y)
    elif character == 'doon':
        player = Doon(player_x, player_y)
    elif character == 'virtus':
        player = Virtus(player_x, player_y)
    player.rect.x += cell_size * 0.025
    player.rect.y += cell_size * 0.025


def load_level(level):
    for y in range(len(level)):
        for x in range(len(level[0])):
            if level[y][x] == 1:
                Unbreakable_block(y, x, all_sprites, walls_group, unshootable_walls_group)
            elif level[y][x] == 2:
                Breakable_block(y, x, all_sprites, walls_group, unshootable_walls_group, breakable_blocks_group)
            elif level[y][x] == 3:
                Abyss(y, x, all_sprites, walls_group)
            elif level[y][x] == 4:
                Spawn_point(y, x, all_sprites)


class Hud_skill_e(pygame.sprite.Sprite):
    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = pygame.Surface((cell_size * 2.4, cell_size * 0.5))
        self.image.fill(GREEN)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH // 3
        self.rect.top = HEIGHT - cell_size * 0.6

    def update(self):
        pygame.draw.rect(screen, pygame.Color('white'), (
        self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),
        cell_size * 2.4 + int(cell_size * 0.025), cell_size * 0.5 + int(cell_size * 0.0375)))

        self.rect.left = WIDTH // 3
        self.rect.top = HEIGHT - cell_size * 0.6
        self.image = pygame.transform.scale(self.image, (cell_size * 2.4 * player.skill_e_now / player.skill_e_max, cell_size * 0.5))
        self.image.fill(YELLOW)
        # pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.05), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))

    def draw(self):
        pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),cell_size * 2.4 + int(cell_size * 0.025), cell_size * 0.5 + int(cell_size * 0.0375)), int(cell_size * 0.025))
        pygame.draw.line(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025) + cell_size * 0.8, self.rect.top - int(cell_size * 0.025)), (self.rect.left - int(cell_size * 0.025) + cell_size * 0.8, self.rect.top - int(cell_size * 0.025) + cell_size * 0.5 + int(cell_size * 0.0375)), width=int(cell_size * 0.025))
        pygame.draw.line(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025) + cell_size * 1.6, self.rect.top - int(cell_size * 0.025)), (self.rect.left - int(cell_size * 0.025) + cell_size * 1.6, self.rect.top - int(cell_size * 0.025) + cell_size * 0.5 + int(cell_size * 0.0375)), width=int(cell_size * 0.025))
        if player.skill_e_cooldown:
            text1 = font3.render(f'{player.skill_e_cooldown // FPS}', 1, BLUE)
            textpos1 = text1.get_rect()
            textpos1.centerx = self.rect.centerx
            textpos1.y = self.rect.top - cell_size * 0.5
            screen.blit(text1, textpos1)

        text11 = font3.render(f'E', 1, BLUE)
        textpos11 = text11.get_rect()
        textpos11.centerx = self.rect.centerx
        textpos11.y = self.rect.top
        screen.blit(text11, textpos11)


class Hud_skill_x(pygame.sprite.Sprite):
    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = pygame.Surface((cell_size, cell_size * 0.5))
        self.image.fill(GREEN)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH // 2 - cell_size * 0.5
        self.rect.top = HEIGHT - cell_size * 0.6

    def update(self):
        pygame.draw.rect(screen, pygame.Color('white'), (
        self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),
        cell_size + int(cell_size * 0.025), cell_size * 0.5 + int(cell_size * 0.0375)))

        self.rect.left = WIDTH // 2 - cell_size * 0.5
        self.rect.top = HEIGHT - cell_size * 0.6
        self.image = pygame.transform.scale(self.image, (cell_size * player.skill_x_now, cell_size * 0.5))
        self.image.fill(YELLOW)
        # pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.05), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))

    def draw(self):
        pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),cell_size + int(cell_size * 0.025), cell_size * 0.5 + int(cell_size * 0.0375)), int(cell_size * 0.025))

        if player.skill_x_cooldown:
            text2 = font3.render(f'{player.skill_x_cooldown // FPS}', 1, BLUE)
            textpos2 = text2.get_rect()
            textpos2.centerx = self.rect.centerx
            textpos2.y = self.rect.top - cell_size * 0.5
            screen.blit(text2, textpos2)

        text22 = font3.render(f'X', 1, BLUE)
        textpos22 = text22.get_rect()
        textpos22.centerx = self.rect.centerx
        textpos22.y = self.rect.top
        screen.blit(text22, textpos22)


class Hud_skill_t(pygame.sprite.Sprite):
    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = pygame.Surface((cell_size * 2.4, cell_size * 0.5))
        self.image.fill(GREEN)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH - WIDTH // 3 - cell_size * 2.4
        self.rect.top = HEIGHT - cell_size * 0.6

    def update(self):
        pygame.draw.rect(screen, pygame.Color('white'), (
        self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),
        cell_size * 2.4 + int(cell_size * 0.025), cell_size * 0.5 + int(cell_size * 0.0375)))

        self.rect.left = WIDTH - WIDTH // 3 - cell_size * 2.4
        self.rect.top = HEIGHT - cell_size * 0.6
        self.image = pygame.transform.scale(self.image, (cell_size * 2.4 * player.skill_t_now / player.skill_t_max, cell_size * 0.5))
        self.image.fill(YELLOW)
        # pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.05), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))

    def draw(self):
        pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),cell_size * 2.4 + int(cell_size * 0.025), cell_size * 0.5 + int(cell_size * 0.0375)), int(cell_size * 0.025))
        pygame.draw.line(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025) + cell_size * 1.2, self.rect.top - int(cell_size * 0.025)), (self.rect.left - int(cell_size * 0.025) + cell_size * 1.2, self.rect.top - int(cell_size * 0.025) + cell_size * 0.5 + int(cell_size * 0.0375)), width=int(cell_size * 0.025))
        if player.skill_t_cooldown:
            text3 = font3.render(f'{player.skill_t_cooldown // FPS}', 1, BLUE)
            textpos3 = text3.get_rect()
            textpos3.centerx = self.rect.centerx
            textpos3.y = self.rect.top - cell_size * 0.5
            screen.blit(text3, textpos3)

        text33 = font3.render(f'T', 1, BLUE)
        textpos33 = text33.get_rect()
        textpos33.centerx = self.rect.centerx
        textpos33.y = self.rect.top
        screen.blit(text33, textpos33)


class Hud_hp(pygame.sprite.Sprite):
    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = pygame.Surface((cell_size * 1.4, cell_size * 0.25))
        self.image.fill(GREEN)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = player.rect.x - cell_size * 0.2
        self.rect.top = player.rect.y - cell_size * 0.6
        #self.rect.centery = HEIGHT // 2
        #self.rect.centerx = WIDTH // 2
        #self.rect.bottom = HEIGHT / 2
        
    def update(self):
        self.rect.left = player.rect.x - cell_size * 0.2
        self.rect.top = player.rect.y - cell_size * 0.6

        pygame.draw.rect(screen, pygame.Color('white'), (
        self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),
        cell_size * 1.4 + int(cell_size * 0.025), cell_size * 0.25 + int(cell_size * 0.0375)))

        self.image = pygame.transform.scale(self.image, (cell_size * 1.4 * player.hp / player.maxhp, cell_size * 0.25))
        if player.hp / player.maxhp * 100 > 75:
            self.image.fill(GREEN)
        elif player.hp / player.maxhp * 100 > 50:
            self.image.fill(ORANGE)
        elif player.hp / player.maxhp * 100 > 25:
            self.image.fill(YELLOW)
        elif player.hp / player.maxhp * 100 > 0:
            self.image.fill(RED)
        # pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.05), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))
        
    def draw(self):
        pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.025), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))
        text1 = font1.render(f'{player.hp}', 1, BLUE)
        textpos1 = text1.get_rect()
        textpos1.centerx = self.rect.centerx
        textpos1.y = self.rect.top
        screen.blit(text1, textpos1)


class Hud_heat(pygame.sprite.Sprite):
    def __init__(self, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = pygame.Surface((cell_size * 1.4, cell_size * 0.25))
        self.image.fill(GREEN)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = player.rect.x - cell_size * 0.2
        self.rect.top = player.rect.y - cell_size * 0.25
        #self.rect.centery = HEIGHT // 2
        #self.rect.centerx = WIDTH // 2
        #self.rect.bottom = HEIGHT / 2
        
    def update(self):
        self.rect.left = player.rect.x - cell_size * 0.2
        self.rect.top = player.rect.y - cell_size * 0.25

        pygame.draw.rect(screen, pygame.Color('white'), (
        self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025),
        cell_size * 1.4 + int(cell_size * 0.025), cell_size * 0.25 + int(cell_size * 0.0375)))

        self.image = pygame.transform.scale(self.image, (cell_size * 1.4 * player.overheat / 100, cell_size * 0.25))
        if player.overheat > 75:
            self.image.fill(RED)
        elif player.overheat > 50:
            self.image.fill(ORANGE)
        elif player.overheat > 25:
            self.image.fill(YELLOW)
        else:
            self.image.fill(GREEN)
        # pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.05), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))
        
    def draw(self):
        pygame.draw.rect(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025), self.rect.top - int(cell_size * 0.025), cell_size * 1.4 + int(cell_size * 0.025), cell_size * 0.25 + int(cell_size * 0.0375)), int(cell_size * 0.025))
        pygame.draw.line(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025) + cell_size * 0.35, self.rect.top - int(cell_size * 0.025)), (self.rect.left - int(cell_size * 0.025) + cell_size * 0.35, self.rect.top - int(cell_size * 0.025) + cell_size * 0.25 + int(cell_size * 0.0375)), width=int(cell_size * 0.025))
        pygame.draw.line(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025) + cell_size * 0.7, self.rect.top - int(cell_size * 0.025)), (self.rect.left - int(cell_size * 0.025) + cell_size * 0.7, self.rect.top - int(cell_size * 0.025) + cell_size * 0.25 + int(cell_size * 0.0375)), width=int(cell_size * 0.025))
        pygame.draw.line(screen, pygame.Color('black'), (self.rect.left - int(cell_size * 0.025) + cell_size * 1.05, self.rect.top - int(cell_size * 0.025)), (self.rect.left - int(cell_size * 0.025) + cell_size * 1.05, self.rect.top - int(cell_size * 0.025) + cell_size * 0.25 + int(cell_size * 0.0375)), width=int(cell_size * 0.025))


class SearchSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, all_sprites)

        self.default_image = search_image_1
        self.image = search_image_1

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.angle = 0
        self.step = 1

    def update(self):
        self.image = pygame.transform.rotate(self.default_image , int(self.angle))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.angle -= 1.5
        if self.angle % 120 == 0:
            self.step += 1
            if self.step == 5:
                self.step = 1
            self.default_image = eval(f'search_image_{self.step}')


class Smoke(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = smoke_image.copy()
        self.life_time = FPS * 8
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.left = cell_size * x + background_map_rect.x
        self.rect.top = cell_size * y + background_map_rect.y

    def update(self):
        self.life_time -= 1
        if self.life_time < FPS:
            self.image.set_alpha(255 / FPS * self.life_time)
        if self.life_time == 0:
            self.kill()


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__(all_sprites)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(players_group, all_sprites)
        """
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = cell_size * x
        self.rect.y = cell_size * y"""

    def take_damage(self, bullet):
        self.hp -= bullet.damage
        if self.hp <= 0:
            bullet.kill()
            self.kill()

    def update(self):
        if not self.shoot_cooldown:
            self.overheat = max(0, self.overheat - self.overheat_step / FPS / 2)
            
        keystate = pygame.key.get_pressed()
        right = False
        down = False
        left = False
        up = False
        if self.shoot_cooldown:
            self.shoot_cooldown -= 1
        if self.skill_e_cooldown:
            self.skill_e_cooldown -= 1
        if self.skill_x_cooldown:
            self.skill_x_cooldown -= 1
        if self.skill_t_cooldown:
            self.skill_t_cooldown -= 1
        if self.return_speed_cooldown:
            self.return_speed_cooldown -= 1
        elif self.return_speed_cooldown == 0:
            self.return_speed()
            
        if keystate[pygame.K_a]:
            self.rect.x += -self.speed
            stop = pygame.sprite.spritecollideany(player, walls_group)
            if stop:
                self.rect.x += self.speed
            else:
                left = True
        elif keystate[pygame.K_d]:
            self.rect.x += self.speed
            stop = pygame.sprite.spritecollideany(player, walls_group)
            if stop:
                self.rect.x -= self.speed
            else:
                right = True
        if keystate[pygame.K_w]:
            self.rect.y += -self.speed
            stop = pygame.sprite.spritecollideany(player, walls_group)
            if stop:
                self.rect.y += self.speed
            else:
                up = True
        elif keystate[pygame.K_s]:
            self.rect.y += self.speed
            stop = pygame.sprite.spritecollideany(player, walls_group)
            if stop:
                self.rect.y -= self.speed
            else:
                down = True

        if not right and not left and not down and not up:
            self.step = 6
            if self.last_side == 'up_right':
                self.image = self.images_up_right[self.step]
            elif self.last_side == 'right':
                self.image = self.images_right[self.step]
            elif self.last_side == 'right_down':
                self.image = self.images_right_down[self.step]
            elif self.last_side == 'down':
                self.image = self.images_down[self.step]
            elif self.last_side == 'down_left':
                self.image = self.images_down_left[self.step]
            elif self.last_side == 'left':
                self.image = self.images_left[self.step]
            elif self.last_side == 'left_up':
                self.image = self.images_left_up[self.step]
            elif self.last_side == 'up':
                self.image = self.images_up[self.step]
        if right:
            if up:
                self.image = self.images_up_right[self.step]
                self.last_side = 'up_right'
            elif down:
                self.image = self.images_right_down[self.step]
                self.last_side = 'right_down'
            else:
                self.image = self.images_right[self.step]
                self.last_side = 'right'
        if down:
            if left:
                self.image = self.images_down_left[self.step]
                self.last_side = 'down_left'
            elif right:
                self.image = self.images_right_down[self.step]
                self.last_side = 'right_down'
            else:
                self.image = self.images_down[self.step]
                self.last_side = 'down'
        if left:
            if up:
                self.image = self.images_left_up[self.step]
                self.last_side = 'left_up'
            elif down:
                self.image = self.images_down_left[self.step]
                self.last_side = 'down_left'
            else:
                self.image = self.images_left[self.step]
                self.last_side = 'left'
        if up:
            if right:
                self.image = self.images_up_right[self.step]
                self.last_side = 'up_right'
            elif left:
                self.image = self.images_left_up[self.step]
                self.last_side = 'left_up'
            else:
                self.image = self.images_up[self.step]
                self.last_side = 'up'
            
        """if stop:
            print(stop.rect, self.rect)
            if stop.rect.left < self.rect.left < stop.rect.right or stop.rect.left < self.rect.right < stop.rect.right:
                self.rect.x -= x_move
            if stop.rect.top < self.rect.top < stop.rect.bottom or stop.rect.top < self.rect.bottom < stop.rect.bottom:
                self.rect.y -= y_move"""
        if self.wait != 0:
            self.wait -= 1
            self.image = self.image_on_shoot
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            
        if self.start_image_speed == self.image_speed:
            self.start_image_speed = 0
            self.step = (self.step + 1) % 16
        else:
            self.start_image_speed += 1
        #print(background_map_rect, 1)

# ----------------------------------------------------------------------------------------------------------------------------------------
class Aim(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.basic_speed = int(cell_size * 0.025)  # 2
        self.speed = int(cell_size * 0.025)  # 2
        self.maxhp = 3200
        self.hp = 3200
        self.overheat = 0
        self.overheat_step = 25

        self.skill_e_max = 3
        self.skill_e_now = self.skill_e_max
        self.skill_x_max = 1
        self.skill_x_now = self.skill_x_max
        self.skill_t_max = 2
        self.skill_t_now = self.skill_t_max

        self.images_right = []
        self.images_right_down = []
        self.images_down = []
        self.images_down_left = []
        self.images_left = []
        self.images_left_up = []
        self.images_up = []
        self.images_up_right = []
        self.shoot_cooldown = 0
        self.skill_e_cooldown = 0
        self.skill_x_cooldown = 0
        self.skill_t_cooldown = 0
        self.return_speed_cooldown = 0
        self.last_side = 'right'
        self.wait = 0
        self.step = 6
        self.start_image_speed = 0
        self.image_speed = FPS // 30 // (self.speed // 2)  # в случае если скорость отличается от стандартной картинки меняются быстрее на коэфф между скоростями
        for i in range(16):
            aim_image = load_image(fr'images\aim_gif\{i}.png')
            aim_image_rect = aim_image.get_rect()
            right = pygame.transform.scale(aim_image, ((cell_size * 0.95), (cell_size * 0.95)))
            right_down = pygame.transform.rotate(right, -45)
            down = pygame.transform.rotate(right, -90)
            down_left = pygame.transform.rotate(right, -135)
            left = pygame.transform.rotate(right, 180)
            left_up = pygame.transform.rotate(right, 135)
            up = pygame.transform.rotate(right, 90)
            up_right = pygame.transform.rotate(right, 45)
            
            self.images_right.append(right)
            self.images_right_down.append(right_down)
            self.images_down.append(down)
            self.images_down_left.append(down_left)
            self.images_left.append(left)
            self.images_left_up.append(left_up)
            self.images_up.append(up)
            self.images_up_right.append(up_right)            
        
        self.image = self.images_right[7]
        self.rect = self.image.get_rect()
        self.rect.x = cell_size * x
        self.rect.y = cell_size * y

    def skill_e(self):
        if not self.skill_e_cooldown and self.skill_e_now:
            x, y = get_cell_pos(player.rect.centerx, player.rect.centery, background_map_rect.x, background_map_rect.y)
            coords = ((-1, -2), (0, -2), (1, -2), (-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1), (-1, 2), (0, 2), (1, 2),
                      (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2))
            for x1, y1 in coords:
                Smoke(y + y1, x + x1, all_sprites, smokes_group)
            self.skill_e_cooldown = FPS * 15
            self.skill_e_now -= 1

    def skill_x(self):
        if not self.skill_x_cooldown and self.skill_x_now:
            x, y = get_cell_pos(player.rect.centerx, player.rect.centery, background_map_rect.x, background_map_rect.y)
            n = 0
            list1 = []
            while n < 10:
                x1, y1 = (randint(-8, 8), randint(-4, 4))
                new_x, new_y = x + x1, y + y1
                if new_x < 0 or new_x > 100 or new_y < 0 or new_y > 56 or (new_x, new_y) in list1:
                    continue
                Airbomb(new_y, new_x, all_sprites, airbombs_group)
                list1.append((new_x, new_y))
                n += 1
            self.skill_x_cooldown = FPS * 30
            self.skill_x_now -= 1

    def skill_t(self):
        if not self.skill_t_cooldown and self.skill_t_now:
            self.overheat = 0
            self.shoot_cooldown = 0
            self.skill_t_cooldown = FPS * 20
            self.skill_t_now -= 1

    def return_speed(self):
        self.speed = self.basic_speed

    def shoot(self, pos):
        if not self.shoot_cooldown and 100 - self.overheat >= self.overheat_step:
            self.overheat += self.overheat_step
            self.weapon = AimBullet(self.rect.centerx, self.rect.centery, pos[0], pos[1])
            self.shoot_cooldown = FPS
            if sound_on:
                shoot_sound_aim.play()


class AimBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, x1, y1):
        super().__init__(all_sprites, bullets_group)
        self.life_time = 0
        self.speed = FPS * 0.6
        basic_damage = 1100
        self.shoot_range = cell_size * 8
        self.damage = 10 * randint((basic_damage) * 0.09, (basic_damage) * 0.11) if crit_is_on else basic_gamage

        # ------------------------------------------
        gip = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        small_coof = self.shoot_range / gip
        big_coof = 1 - small_coof
        x1 = x * big_coof + x1 * small_coof
        y1 = y * big_coof + y1 * small_coof
        # ------------------------------------------
        
        # откуда и куда
        self.from_x = x
        self.from_y = y
        self.to_x = x1
        self.to_y = y1
        

        if self.to_x - self.from_x != 0:
            tgn = (self.to_y - self.from_y) / (self.to_x - self.from_x)
            delta_x = self.to_x - self.from_x
            delta_y = self.to_y - self.from_y
            self.speed_x = delta_x
            self.speed_y = self.speed_x * tgn
            self.speed_x = self.speed_x / self.speed
            self.speed_y = self.speed_y / self.speed
            angle = math.degrees(math.acos((delta_x) / self.shoot_range))
            if self.to_y > self.from_y:
                angle *= -1            
        else:
            self.speed_x = 0
            self.speed_y = (self.to_y - self.from_y) / self.speed
            angle = 90
            if self.speed_y > 0:
                angle = -90

        self.image = pygame.transform.rotate(aim_bullet_image, int(angle))
        player.image_on_shoot = pygame.transform.rotate(player.images_right[player.step], int(angle))
        rect = player.image_on_shoot.get_rect()
        player.wait = self.speed
        self.rect = self.image.get_rect()
        self.rect.centerx = x + self.speed_x * 3
        self.rect.centery = y + self.speed_y * 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.life_time += 1
        if self.life_time > self.speed:
            self.kill()
# ------------------------------------------------------------------

class Virtus(Player):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.basic_speed = int(cell_size * 0.025)
        self.speed = int(cell_size * 0.025)  # 2
        self.maxhp = 4900
        self.hp = 4900
        self.overheat = 0
        self.overheat_step = 25

        self.skill_e_max = 3
        self.skill_e_now = self.skill_e_max
        self.skill_x_max = 1
        self.skill_x_now = self.skill_x_max
        self.skill_t_max = 2
        self.skill_t_now = self.skill_t_max
        self.do_big_damage = False
        self.images_right = []
        self.images_right_down = []
        self.images_down = []
        self.images_down_left = []
        self.images_left = []
        self.images_left_up = []
        self.images_up = []
        self.images_up_right = []
        self.shoot_cooldown = 0
        self.skill_e_cooldown = 0
        self.skill_x_cooldown = 0
        self.skill_t_cooldown = 0
        self.return_speed_cooldown = 0
        self.last_side = 'right'
        self.wait = 0
        self.step = 6
        self.start_image_speed = 0
        self.image_speed = FPS // 30 // (
                    self.speed // 2)  # в случае если скорость отличается от стандартной картинки меняются быстрее на коэфф между скоростями
        for i in range(16):
            aim_image = load_image(fr'images\virtus_gif\{i}.png')
            aim_image_rect = aim_image.get_rect()
            right = pygame.transform.scale(aim_image, ((cell_size * 0.95), (cell_size * 0.95)))
            right_down = pygame.transform.rotate(right, -45)
            down = pygame.transform.rotate(right, -90)
            down_left = pygame.transform.rotate(right, -135)
            left = pygame.transform.rotate(right, 180)
            left_up = pygame.transform.rotate(right, 135)
            up = pygame.transform.rotate(right, 90)
            up_right = pygame.transform.rotate(right, 45)

            self.images_right.append(right)
            self.images_right_down.append(right_down)
            self.images_down.append(down)
            self.images_down_left.append(down_left)
            self.images_left.append(left)
            self.images_left_up.append(left_up)
            self.images_up.append(up)
            self.images_up_right.append(up_right)

        self.image = self.images_right[7]
        self.rect = self.image.get_rect()
        self.rect.x = cell_size * x
        self.rect.y = cell_size * y

    def skill_e(self):
        if not self.skill_e_cooldown and self.skill_e_now and not self.do_big_damage:
            self.do_big_damage = True
            self.skill_e_cooldown = FPS * 10
            self.skill_e_now -= 1

    def skill_x(self):
        if not self.skill_x_cooldown and self.skill_x_now:
            self.speed = int(1.5 * self.speed)
            self.return_speed_cooldown = FPS * 8
            self.skill_x_cooldown = FPS * 25
            self.skill_x_now -= 1

    def skill_t(self):
        if not self.skill_t_cooldown and self.skill_t_now and self.hp != self.maxhp:
            self.hp = int(min(self.maxhp, self.hp + self.maxhp * 0.3))
            self.skill_t_cooldown = FPS * 10
            self.skill_t_now -= 1

    def return_speed(self):
        self.speed = self.basic_speed
    
    def shoot(self, pos):
        if not self.shoot_cooldown and 100 - self.overheat >= self.overheat_step:
            self.overheat += self.overheat_step
            self.weapon = [VirtusBullet(self.rect.centerx, self.rect.centery, pos[0], pos[1], ang) for ang in range(-20, 21, 10)]
            self.do_big_damage = False
            self.shoot_cooldown = FPS * 0.7
            if sound_on:
                shoot_sound_virtus.play()


class VirtusBullet(pygame.sprite.Sprite):
    def __init__(self, x, y, x1, y1, angle_plus):
        super().__init__(all_sprites, bullets_group)
        self.speed_x = 0
        self.speed_y = 0

        self.life_time = 0
        self.speed = FPS * 0.5
        basic_damage = 400
        if player.do_big_damage:
            basic_damage *= 1.5
        self.shoot_range = cell_size * 4
        self.damage = randint(int(basic_damage * 0.9), int(basic_damage * 1.1)) if crit_is_on else basic_gamage

        # ------------------------------------------
        gip = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        small_coof = self.shoot_range / gip
        big_coof = 1 - small_coof
        x1 = x * big_coof + x1 * small_coof
        y1 = y * big_coof + y1 * small_coof
        # ------------------------------------------
        
        # откуда и куда
        self.from_x = x
        self.from_y = y
        self.to_x = x1
        self.to_y = y1


        if self.to_x - self.from_x != 0:
            delta_x = self.to_x - self.from_x
            angle = math.degrees(math.acos((delta_x) / self.shoot_range))
            if self.to_y > self.from_y:
                angle *= -1            
        else:
            angle = 90
            if self.speed_y > 0:
                angle = -90

        angle += angle_plus
        if angle < 0:
            angle = 360 - angle * -1
        if 0 <= angle < 90:
            self.give_x = self.shoot_range * math.cos(math.radians(angle))
            self.give_y = -self.shoot_range * math.sin(math.radians(angle))
            cof_x = 1
            cof_y = 1
        elif 90 <= angle < 180:
            self.give_x = -self.shoot_range * math.cos(math.radians(angle))
            self.give_y = -self.shoot_range * math.sin(math.radians(angle))
            cof_x = -1
            cof_y = 1
        elif 180 <= angle < 270:
            self.give_x = -self.shoot_range * math.cos(math.radians(angle))
            self.give_y = self.shoot_range * math.sin(math.radians(angle))
            cof_x = -1
            cof_y = -1
        else:
            self.give_x = self.shoot_range * math.cos(math.radians(angle))
            self.give_y = self.shoot_range * math.sin(math.radians(angle))
            cof_x = 1
            cof_y = -1

        self.to_x = self.from_x + self.give_x
        self.to_y = self.from_y + self.give_y

        if self.to_x - self.from_x != 0:
            tgn = (self.to_y - self.from_y) / (self.to_x - self.from_x)

            self.speed_x = self.give_x
            self.speed_y = self.speed_x * tgn
            self.speed_x = self.speed_x / self.speed
            self.speed_y = self.speed_y / self.speed         
        else:
            self.speed_x = 0
            self.speed_y = (self.to_y - self.from_y) / self.speed
     
        self.speed_x *= cof_x
        self.speed_y *= cof_y


        self.image = pygame.transform.rotate(virtus_bullet_image, int(angle))
        player.image_on_shoot = pygame.transform.rotate(player.images_right[player.step], int(angle))
        rect = player.image_on_shoot.get_rect()
        player.wait = self.speed
        self.rect = self.image.get_rect()
        self.rect.centerx = x + self.speed_x * 3
        self.rect.centery = y + self.speed_y * 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.life_time += 1
        if self.life_time > self.speed:
            self.kill()

'''
    def shoot(self, pos):
        if not self.shoot_cooldown:
            self.weapon = VirtusSword(self.rect.centerx, self.rect.centery, pos[0], pos[1])
            self.shoot_cooldown = FPS * 1

class VirtusSword(pygame.sprite.Sprite):
    def __init__(self, x, y, x1, y1):
        super().__init__(all_sprites, bullets_group)
        self.speed = FPS * 5 # 0.35
        self.angle_speed = 140 / FPS / (self.speed / FPS)
        basic_damage = 1700
        self.shoot_range = cell_size * 2
        self.damage = 10 * randint((basic_damage) * 0.09, (basic_damage) * 0.11) if crit_is_on else basic_gamage
        # ------------------------------------------
        gip = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        small_coof = self.shoot_range / gip
        big_coof = 1 - small_coof
        x1 = x * big_coof + x1 * small_coof
        y1 = y * big_coof + y1 * small_coof
        # ------------------------------------------

        # откуда и куда
        self.from_x = x
        self.from_y = y
        self.to_x = x1
        self.to_y = y1

        if self.to_x - self.from_x != 0:
            tgn = (self.to_y - self.from_y) / (self.to_x - self.from_x)
            delta_x = self.to_x - self.from_x
            delta_y = self.to_y - self.from_y
            self.speed_x = delta_x
            self.speed_y = self.speed_x * tgn
            self.speed_x = self.speed_x / self.speed
            self.speed_y = self.speed_y / self.speed
            self.angle = math.degrees(math.acos((delta_x) / self.shoot_range))
            if self.to_y > self.from_y:
                self.angle *= -1
        else:
            self.speed_x = 0
            self.speed_y = (self.to_y - self.from_y) / self.speed
            self.angle = 90
            if self.speed_y > 0:
                self.angle = -90
        self.start_angle = int(self.angle) + 70
        self.finish_angle = int(self.angle) - 70
        self.image = pygame.transform.rotate(virtus_sword_image, self.start_angle)
        # player.image_on_shoot = pygame.transform.rotate(player.images_right[player.step], int(self.angle))
        player.image_on_shoot = pygame.transform.rotate(player.images_right[player.step], int(self.start_angle))
        player.image_on_shoot = pygame.transform.scale(player.image_on_shoot, (cell_size * 1.1, cell_size * 1.1))
        rect = player.image_on_shoot.get_rect()
        player.wait = self.speed
        self.rect = self.image.get_rect()
        self.rect.centerx = self.from_x
        self.rect.centery = self.from_y

    def update(self):
        # if self.start_angle <= 0 or self.start_angle >= 45:
        #     self.start_angle += self.angle_speed
        #     self.angle_speed *= -1
        
        if self.start_angle < self.finish_angle:
            self.kill()
        self.start_angle -= self.angle_speed
        ang = int(self.start_angle)
        self.image = pygame.transform.rotate(virtus_sword_image, self.start_angle)
        self.rect = self.image.get_rect()
        if ang < -90:
            ang = 360 - ang * -1
        if 45 > ang >= 0:
            self.rect.centerx = player.rect.centerx + 70 - (ang // 3)
            self.rect.centery = player.rect.centery + 7 - ang
        elif 0 > ang >= -45:
            self.rect.centerx = player.rect.centerx + 70 + (ang // 3)
            self.rect.centery = player.rect.centery + 7 - ang
        elif 90 > ang >= 45:
            self.rect.centerx = player.rect.centerx + 50 - 43 * ((ang - 45) / 45)
            self.rect.centery = player.rect.centery - 40 - 18 * ((ang - 45) / 45)
        elif -45 > ang >= -90:
            self.rect.centerx = player.rect.centerx + 137 + 43 * ((ang - 45) / 45)
            self.rect.centery = player.rect.centery + 18 - 18 * ((ang - 45) / 45)
        elif 180 > ang >= 135:
            self.rect.centerx = player.rect.centerx + 5 - (ang // 3)
            self.rect.centery = player.rect.centery + 95 - ang + (ang - 135) / 90 * 180
        elif 225 > ang >= 180:
            self.rect.centerx = player.rect.centerx + 5 - (ang // 3) + (ang - 180) / 45 * 30
            self.rect.centery = player.rect.centery + 95 - ang + (ang - 135) / 90 * 180

        ########
        elif 90 > int(self.start_angle) >= 45:
            self.rect.centerx = player.rect.centerx + 50 - 43 * ((int(self.start_angle) - 45) / 45)
            self.rect.centery = player.rect.centery - 40 - 18 * ((int(self.start_angle) - 45) / 45)
        elif 135 > int(self.start_angle) >= 90:
            self.rect.centerx = player.rect.centerx + 105 - (int(self.start_angle) // 3) - self.rect.width / 2
            self.rect.centery = player.rect.centery - ((self.rect.h - cell_size) * (1 - (int(self.start_angle) - 90) / 90))
        elif 180 > int(self.start_angle) >= 135:
            self.rect.centerx = player.rect.centerx + 145 - 43 * ((int(self.start_angle) - 45) / 45) - self.rect.width / 2
            self.rect.centery = player.rect.centery - (75 * (1 - (int(self.start_angle) - 90) / 90))
        elif -45 <= int(self.start_angle) < 0:
            self.rect.centerx = player.rect.centerx + 70 + (int(self.start_angle) // 3)
            self.rect.centery = player.rect.centery
        elif -90 <= int(self.start_angle) < -45:
            self.rect.centerx = player.rect.centerx + 50 - 43 * ((int(self.start_angle) * -1 - 45) / 45)
            self.rect.centery = player.rect.centery
        ########

        ########
        if self.start_angle > self.finish_angle or True:
            self.start_angle -= self.angle_speed
            self.image = pygame.transform.rotate(virtus_sword_image, int(self.start_angle))
            self.rect.center = player.rect.center

            if self.start_angle > 90:
                print('1 четверть')
            elif self.start_angle > 0:
                if self.start_angle < 45:
                    self.rect.left = player.rect.centerx
                    self.rect.bottom = player.rect.centery
                else:
                    self.rect.bottom = player.rect.centery
                    self.rect.centerx = player.rect.centerx
            elif self.start_angle > -90:
                print('3 четверть')
            else:
                print('4 четверть')
        else:
            self.kill()
        ########
''' # мечник(в разработке)
# ----------------------------------------------------------------------------------------------------------------------------------------
class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.xx = cell_size // 2 - WIDTH // 2
        self.yy = cell_size // 2 - HEIGHT // 2
        self.border = cell_size * 2

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
        if obj in view_sprites:
            if not(WIDTH + self.border > obj.rect.right > -self.border and -self.border < obj.rect.bottom < HEIGHT + self.border):
                view_sprites.remove(obj)
        elif WIDTH + self.border > obj.rect.right > -self.border and -self.border < obj.rect.bottom < HEIGHT + self.border:
            view_sprites.add(obj)

    # позиционировать камеру на объекте target
    def update(self, target):
        # print(background_map_rect.x, target.rect.x, abs(background_map_rect.x) >= speed)
        '''print(target.rect.x, speed + WIDTH // 2 - target.rect.width, background_map_rect.x)'''
        background_map_rect.x += -(target.rect.x + self.xx)
        self.dx = -(target.rect.x + self.xx)
        if background_map_rect.x > 0:
            background_map_rect.x = 0
            self.dx = 0
        if background_map_rect.x < -WIDTH * 4:
            background_map_rect.x = -WIDTH * 4
            self.dx = 0
        background_map_rect.y += -(target.rect.y + self.yy)
        self.dy = -(target.rect.y + self.yy)
        if background_map_rect.y > 0:
            background_map_rect.y = 0
            self.dy = 0
        if background_map_rect.y < -HEIGHT * 4:
            background_map_rect.y = -HEIGHT * 4
            self.dy = 0
        # print(target.rect.y, speed + HEIGHT // 2 - target.rect.width // 2
        # background_map_rect.y += -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)
        # self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


screen = pygame.display.set_mode(size)
pygame.display.set_caption("игра моя")
game_window = 'lobby'
main_running = True

while main_running:
    if game_window == 'lobby':
        all_sprites = pygame.sprite.Group()
        settings_button_1 = Button(WIDTH - HEIGHT / 10, 0, settings_button)
        characters_button_1 = Button(0, 100, characters_button)
        start_game_text = font3.render(u'Новая игра', 1, (255, 255, 10))
        start_game_text_pos = pygame.Rect(WIDTH * 0.41, HEIGHT * 0.85, WIDTH * 0.155, HEIGHT * 0.05)
        running = True
        while running:
            screen.blit(background_lobby, background_lobby_rect)
            # -------------------
            # проверка на события
            # -------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_running = False
                elif event.type == pygame.MOUSEMOTION:
                    if start_game_text_pos.collidepoint(event.pos):
                        start_game_text = font3.render(u'Новая игра', 1, (255, 0, 0))
                        game_start = True
                    else:
                        game_start = False
                        start_game_text = font3.render(u'Новая игра', 1, (255, 255, 10))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True  # смена цвета курсора
                    if game_start:
                        running = False
                        game_window = 'search'
                    elif characters_button_1.rect.collidepoint(event.pos):
                        running = False
                        game_window = 'characters'
                    elif settings_button_1.rect.collidepoint(event.pos):
                        running = False
                        game_window = 'settings'
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_clicked = False  # смена цвета курсора

            # -------------------
            # основная часть цикла
            # -------------------

            all_sprites.draw(screen)
            # -------------------
            # конец цикла
            # -------------------
            screen.blit(start_game_text, start_game_text_pos)

            mouse_coords = pygame.mouse.get_pos()
            custom_cursor(screen, mouse_coords[0], mouse_coords[1], mouse_clicked)
            screen.blit(update_fps(), (10, 0))
            clock.tick(FPS)
            pygame.display.flip()

            # -------------------

    if game_window == 'settings':
        resolutions = [(1920, 1080), (1600, 900), (1280, 720)]
        ind = resolutions.index((WIDTH, HEIGHT))
        new_width = WIDTH
        new_height = HEIGHT
        all_sprites = pygame.sprite.Group()
        resolutions_button = Button(WIDTH * 0.55, HEIGHT * 0.10, resolution_button)
        if music_on:
            music_button = Button(WIDTH * 0.55, HEIGHT * 0.25, green_button)
        else:
            music_button = Button(WIDTH * 0.55, HEIGHT * 0.25, red_button)
        if sound_on:
            sound_button = Button(WIDTH * 0.55, HEIGHT * 0.40, green_button)
        else:
            sound_button = Button(WIDTH * 0.55, HEIGHT * 0.40, red_button)
        if fps_on:
            fps_button = Button(WIDTH * 0.55, HEIGHT * 0.55, green_button)
        else:
            fps_button = Button(WIDTH * 0.55, HEIGHT * 0.55, red_button)
        volume_plus = Button(WIDTH * 0.63, HEIGHT * 0.7, arrow_right_button)
        volume_minus = Button(WIDTH * 0.55, HEIGHT * 0.7, arrow_left_button)
        back_button = Button(0, 0, back_button_image)
        text1 = font4.render(u'Музыка', 1, (255, 255, 10))
        text1_pos = WIDTH * 0.25, HEIGHT * 0.25 + HEIGHT /40

        text2 = font4.render(u'Звуки', 1, (255, 255, 10))
        text2_pos = WIDTH * 0.25, HEIGHT * 0.40 + HEIGHT /40

        text3 = font4.render(f'Громкость {music_volume}', 1, (255, 255, 10))
        text3_pos = WIDTH * 0.25, HEIGHT * 0.70 + HEIGHT / 40

        text4 = font4.render(f'Фпс', 1, (255, 255, 10))
        text4_pos = WIDTH * 0.25, HEIGHT * 0.55 + HEIGHT /40

        text6 = font4.render(f'Разрешение', 1, (255, 255, 10))
        text6_pos = WIDTH * 0.25, HEIGHT * 0.10 + HEIGHT / 40

        text5 = font2.render(f'{WIDTH}:{HEIGHT}', 1, (255, 255, 10))
        text5_pos = WIDTH * 0.57, HEIGHT * 0.11 + HEIGHT / 40
        running = True
        while running:
            screen.blit(background_lobby, background_lobby_rect)
            # -------------------
            # проверка на события
            # -------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    changed = False
                    mouse_clicked = True  # смена цвета курсора
                    if back_button.rect.collidepoint(event.pos):
                        running = False
                        game_window = 'lobby'
                    if resolutions_button.rect.collidepoint(event.pos):
                        ind += 1
                        if ind > len(resolutions) - 1:
                            ind = 0
                        new_width, new_height = resolutions[ind]
                        changed = True
                    if music_button.rect.collidepoint(event.pos):
                        if music_on:
                            music_on = False
                            music_button.image = red_button
                            pygame.mixer.music.stop()
                        else:
                            music_on = True
                            music_button.image = green_button
                            pygame.mixer.music.play(loops=-1)
                        changed = True
                    if sound_button.rect.collidepoint(event.pos):
                        if sound_on:
                            sound_on = False
                            sound_button.image = red_button
                        else:
                            sound_on = True
                            sound_button.image = green_button
                        changed = True
                    if fps_button.rect.collidepoint(event.pos):
                        if fps_on:
                            fps_on = False
                            fps_button.image = red_button
                        else:
                            fps_on = True
                            fps_button.image = green_button
                        changed = True
                    if volume_plus.rect.collidepoint(event.pos):
                        music_volume = round(min(1.0, music_volume + 0.1), 1)
                        changed = True
                    if volume_minus.rect.collidepoint(event.pos):
                        music_volume = round(max(0, music_volume - 0.1), 1)
                        changed = True
                    if changed:
                        f1 = open("GameUserSettings.TXT", "w+")
                        f1.write(f'ScreenWidth={new_width}\n')
                        f1.write(f'ScreenHeight={new_height}\n')
                        f1.write(f'MenuMusicVolume={music_volume}\n')
                        f1.write(f'Sound={str(sound_on)}\n')
                        f1.write(f'Music={str(music_on)}\n')
                        f1.write(f'FPS={str(fps_on)}')
                        f1.close()
                        text3 = font4.render(f'Громкость {music_volume}', 1, (255, 255, 10))
                        text5 = font2.render(f'{new_width}:{new_height}', 1, (255, 255, 10))
                        pygame.mixer.music.set_volume(music_volume)
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_clicked = False  # смена цвета курсора

            # -------------------
            # основная часть цикла
            # -------------------

            all_sprites.draw(screen)
            # -------------------
            # конец цикла
            # -------------------
            screen.blit(text1, text1_pos)
            screen.blit(text2, text2_pos)
            screen.blit(text3, text3_pos)
            screen.blit(text4, text4_pos)
            screen.blit(text5, text5_pos)
            screen.blit(text6, text6_pos)
            mouse_coords = pygame.mouse.get_pos()
            custom_cursor(screen, mouse_coords[0], mouse_coords[1], mouse_clicked)
            screen.blit(update_fps(), (10, 0))
            clock.tick(FPS)
            pygame.display.flip()

            # -------------------

    elif game_window == 'characters':
        info_about_characters = load_info_about_characters()
        all_sprites = pygame.sprite.Group()
        back_button = Button(0, 0, back_button_image)
        cur = info_about_characters[number_of_character]

        name_of_current_character = cur['name']
        choose_character_text = font3.render(f'Выбрать {name_of_current_character}', 1, (255, 255, 10))
        name_of_current_character_text = font4.render(f"{cur['name']}", 1, (255, 255, 10))
        class_of_current_character_text = font3.render(f"{cur['class']}", 1, (255, 255, 10))
        rarity_of_current_character_text = font3.render(f"{cur['rarity']}", 1, (255, 255, 10))

        choose_character_text_pos = pygame.Rect(WIDTH * 0.41, HEIGHT * 0.85, WIDTH * 0.18, HEIGHT * 0.3)
        name_of_current_character_text_pos = WIDTH * 0.11, HEIGHT * 0.20
        class_of_current_character_text_pos = WIDTH * 0.13, HEIGHT * 0.25
        rarity_of_current_character_text_pos = WIDTH * 0.16, HEIGHT * 0.30

        arrow_left_1 = Button(0, HEIGHT // 2 - HEIGHT // 8, arrow_left_button)
        arrow_right_1 = Button(WIDTH - HEIGHT // 8, HEIGHT // 2 - HEIGHT // 8, arrow_right_button)
        name_of_current_character = 'Virtus'
        arrow_left_clicked = False
        arrow_right_clicked = False
        running = True
        while running:
            if start_game_text_pos.collidepoint(pygame.mouse.get_pos()):
                choose_character_text = font3.render(f'Выбрать {name_of_current_character}', 1, (255, 0, 0))
                game_start = True
            else:
                game_start = False
                choose_character_text = font3.render(f'Выбрать {name_of_current_character}', 1, (255, 255, 10))

            screen.blit(background_characters, background_characters_rect)
            # -------------------
            # проверка на события
            # -------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_running = False
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect.collidepoint(event.pos):
                        running = False
                        game_window = 'lobby'
                    mouse_clicked = True  # смена цвета курсора
                    if game_start:
                        running = False
                        game_window = 'lobby'
                        if name_of_current_character.lower() == 'doon':
                            pass
                        else:
                            character = name_of_current_character.lower()
                    elif arrow_left_1.rect.collidepoint(event.pos):
                        arrow_left_clicked = True
                        arrow_left_1.image = arrow_left_button_clicked
                    elif arrow_right_1.rect.collidepoint(event.pos):
                        arrow_right_clicked = True
                        arrow_right_1.image = arrow_right_button_clicked
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_clicked = False  # смена цвета курсора
                    if arrow_left_clicked and number_of_character != 1:
                        character_is_changed = True
                        arrow_left_clicked = False
                        arrow_left_1.image = arrow_left_button
                        number_of_character -= 1
                        if number_of_character == 1:
                            arrow_left_1.kill()
                        if number_of_character == count_of_characters - 1:
                            arrow_right_1 = Button(WIDTH - HEIGHT // 8, HEIGHT // 2 - HEIGHT // 8, arrow_right_button)
                    elif arrow_right_clicked and number_of_character != count_of_characters:
                        character_is_changed = True
                        arrow_right_clicked = False
                        arrow_right_1.image = arrow_right_button
                        number_of_character += 1
                        if number_of_character == count_of_characters:
                            arrow_right_1.kill()
                        if number_of_character == 2:
                            arrow_left_1 = Button(0, HEIGHT // 2 - HEIGHT // 8, arrow_left_button)
                    else:
                        character_is_changed = False
                    if character_is_changed:
                        cur = info_about_characters[number_of_character]
                        choose_character_text = font3.render(f'Выбрать {name_of_current_character}', 1, (255, 255, 10))
                        name_of_current_character = cur['name']
                        name_of_current_character_text = font4.render(f"{cur['name']}", 1, (255, 255, 10))
                        class_of_current_character_text = font3.render(f"{cur['class']}", 1, (255, 255, 10))
                        rarity_of_current_character_text = font3.render(f"{cur['rarity']}", 1, (255, 255, 10))
            # -------------------
            # основная часть цикла
            # -------------------
            all_sprites.draw(screen)
            # -------------------
            # конец цикла
            # -------------------
            cofff = 0
            for i in range(len(cur['discription'])):
                for k in range(len(cur['discription'][i])):
                    dd = font2.render(f"{cur['discription'][i][k]}", 1, (255, 255, 10))
                    screen.blit(dd, (WIDTH * 0.55, HEIGHT * (0.1 + 0.05 * cofff)))
                    cofff += 1
                cofff += 1
            screen.blit(name_of_current_character_text, name_of_current_character_text_pos)
            screen.blit(class_of_current_character_text, class_of_current_character_text_pos)
            screen.blit(rarity_of_current_character_text, rarity_of_current_character_text_pos)
            screen.blit(choose_character_text, choose_character_text_pos)
            mouse_coords = pygame.mouse.get_pos()
            custom_cursor(screen, mouse_coords[0], mouse_coords[1], mouse_clicked)
            screen.blit(update_fps(), (10, 0))
            clock.tick(FPS)
            pygame.display.flip()

    elif game_window == 'search':
        # print(f'игрок номер {player_num}')

        # running_thread = True
        # start_new_thread(client_send, (network.getServer(),))

        all_sprites = pygame.sprite.Group()
        sett = SearchSprite()
        start_game_text = font3.render(u'Выйти в меню', 1, (255, 255, 10))
        start_game_text_pos = pygame.Rect(WIDTH * 0.4, HEIGHT * 0.85, WIDTH * 0.2, HEIGHT * 0.05)
        info_text = font3.render(f'Загрузка игры', 1, (255, 255, 10))
        info_text_pos = (WIDTH * 0.4, HEIGHT * 0.1)
        running = True
        timer = 0
        while running:
            if timer == FPS * 5:
                game_window = 'game'
                running = False
            timer += 1
            screen.blit(background_search, background_search_rect)
            # -------------------
            # проверка на события
            # -------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_running = False
                elif event.type == pygame.MOUSEMOTION:
                    if start_game_text_pos.collidepoint(event.pos):
                        start_game_text = font3.render(u'Выйти в меню', 1, (255, 0, 0))
                        game_start = True
                    else:
                        game_start = False
                        start_game_text = font3.render(u'Выйти в меню', 1, (255, 255, 10))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True  # смена цвета курсора
                    if game_start:
                        running = False
                        game_window = 'lobby'
                    elif characters_button_1.rect.collidepoint(event.pos):
                        running = False
                        game_window = 'characters'
                    elif settings_button_1.rect.collidepoint(event.pos):
                        running = False
                        game_window = 'settings'
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_clicked = False  # смена цвета курсора

            # -------------------
            # основная часть цикла
            # -------------------
            all_sprites.update()
            all_sprites.draw(screen)
            # -------------------
            # конец цикла
            # -------------------
            screen.blit(start_game_text, start_game_text_pos)
            screen.blit(info_text, info_text_pos)

            mouse_coords = pygame.mouse.get_pos()
            custom_cursor(screen, mouse_coords[0], mouse_coords[1], mouse_clicked)
            screen.blit(update_fps(), (10, 0))
            clock.tick(FPS)

            pygame.display.flip()

        running_thread = False
        # network.client.close()
        for i in all_sprites:
            i.kill()

    elif game_window == 'game':
        load_spawn_points(level1)
        spawn_point = choice(spawn_points)
        spawn_point = (spawn_point[0] - 1, spawn_point[1] - 1)
        if spawn_point[0] <= 10:
            background_map_rect.x = 0
            player_x = spawn_point[0]
        elif spawn_point[0] >= 90:
            background_map_rect.x = -WIDTH * 4
            player_x = spawn_point[0] - 80
        else:
            background_map_rect.x = -cell_size * (spawn_point[0] - 5)
            player_x = 5
        if spawn_point[1] <= 5:
            background_map_rect.y = 0
            player_y = spawn_point[1]
        elif spawn_point[1] >= 47:
            background_map_rect.y = -HEIGHT * 4
            player_y = spawn_point[1] - 45
        else:
            background_map_rect.y = -cell_size * (spawn_point[1] - 5)
            player_y = 5

        camera = Camera()
        load_level(level1)
        create_player(character)
        hud_heat = Hud_heat(hud_group)
        hud_hp = Hud_hp(hud_group)
        hud_skill_e = Hud_skill_e(hud_group)
        hud_skill_x = Hud_skill_x(hud_group)
        hud_skill_t = Hud_skill_t(hud_group)

        running = True
        while running:
            screen.blit(background_map, background_map_rect)
            # -------------------
            # проверка на события
            # -------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    main_running = False
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_clicked = True  # смена цвета курсора
                    # FPS = 180
                    player.shoot(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_clicked = False  # смена цвета курсора
                    # FPS = 60
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        player.skill_e()
                        if sound_on:
                            skill_sound.play()
                    if event.key == pygame.K_x:
                        player.skill_x()
                        if sound_on:
                            skill_sound.play()
                    if event.key == pygame.K_t:
                        player.skill_t()
                        if sound_on:
                            skill_sound.play()

            # -------------------
            # основная часть цикла
            # -------------------
            hit_breakable_block = pygame.sprite.groupcollide(bullets_group, breakable_blocks_group, False, False)
            for i in hit_breakable_block:
                hit_breakable_block[i][0].take_damage(i)

            hits = pygame.sprite.groupcollide(unshootable_walls_group, bullets_group, False, True)

            # -------------------
            # конец цикла
            # -------------------
            all_sprites.update()
            # all_sprites.draw(screen)
            # изменяем ракурс камеры
            camera.update(player)
            # обновляем положение всех спрайтов
            for sprite in all_sprites:
                camera.apply(sprite)
            view_sprites.draw(screen)
            airbombs_group.draw(screen)
            players_group.draw(screen)
            bullets_group.draw(screen)
            smokes_group.draw(screen)

            hud_group.update()
            hud_group.draw(screen)
            for i in hud_group:
                i.draw()

            mouse_coords = pygame.mouse.get_pos()
            custom_cursor(screen, mouse_coords[0], mouse_coords[1], mouse_clicked)
            screen.blit(update_fps(), (10, 0))
            clock.tick(FPS)
            pygame.display.flip()

            # -------------------

pygame.quit()