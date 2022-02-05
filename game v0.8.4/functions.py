import os
import pygame
from constants import *
from levels import *
from random import randint, choice


class Airbomb(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = airbomb_image
        self.damage = 1000
        self.x, self.y = x, y
        self.size = 0
        self.time_to_explode = randint(FPS * 2.5, FPS * 4)
        self.rect = self.image.get_rect()
        self.rect.left = cell_size * x + background_map_rect.x
        self.rect.top = cell_size * y + background_map_rect.y

    def update(self):
        self.size += 100 / self.time_to_explode
        if self.size > 100:
            hit_players = pygame.sprite.spritecollide(self, players_group, False)
            for i in hit_players:
                i.take_damage(self)
            self.kill()
        self.image = pygame.transform.scale(airbomb_image, (cell_size * self.size / 100, cell_size * self.size / 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = cell_size * self.x + background_map_rect.x + cell_size * 0.5
        self.rect.centery = cell_size * self.y + background_map_rect.y + cell_size * 0.5


class Breakable_block(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = breakable_block_image_3000
        self.rect = self.image.get_rect()
        self.rect.left = cell_size * x + background_map_rect.x
        self.rect.top = cell_size * y + background_map_rect.y
        self.hp = 3000

    def take_damage(self, bullet):
        self.hp -= bullet.damage
        if self.hp <= 0:
            bullet.kill()
            self.kill()
        elif self.hp <= 1000:
            self.image = breakable_block_image_1000
        elif self.hp <= 2000:
            self.image = breakable_block_image_2000


class Unbreakable_block(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = unbreakable_block_image
        self.rect = self.image.get_rect()
        self.rect.left = cell_size * x + background_map_rect.x
        self.rect.top = cell_size * y + background_map_rect.y


class Spawn_point(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = spawn_point_image
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.left = cell_size * x + background_map_rect.x
        self.rect.top = cell_size * y + background_map_rect.y


class Abyss(pygame.sprite.Sprite):
    def __init__(self, y, x, *group):
        pygame.sprite.Sprite.__init__(self, *group)
        self.image = abyss_image
        self.rect = self.image.get_rect()
        self.rect.left = cell_size * x + background_map_rect.x
        self.rect.top = cell_size * y + background_map_rect.y


def custom_cursor(screen, x, y, clicked):
    if pygame.mouse.get_focused():
        if clicked:
            screen.blit(cursor_clicked, (x, y))
        else:
            screen.blit(cursor_default, (x, y))


def get_cell_pos(pos_x1, pos_y1, pos_x2, pos_y2):
    return ((pos_x1 - pos_x2) // cell_size, (pos_y1 - pos_y2) // cell_size)


def load_image(name, colorkey=None):
    fullname = os.path.join(os.path.dirname(__file__), name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        pass
    return image


def load_all_images():
    pass


def load_all_sounds():
    pass


def load_info_about_characters():
    dic1 = {}
    n = 0
    for name in names_of_all_characters:
        n += 1
        dic = {}
        f = open(f'characters/{name}.txt', mode="r", encoding="utf8")
        a = [x.split('\n')[0] for x in f.readlines()]
        dic['name'] = a[0]
        dic['class'] = a[1]
        dic['rarity'] = a[2]
        ll = []
        ll1 = []
        for i in a[3:]:
            if i == '':
                ll1.append(ll)
                ll = []
            else:
                ll.append(i)
        ll1.append(ll)
        dic['discription'] = ll1
        dic1[n] = dic
        f.close()
    return dic1


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


def load_spawn_points(level):
    for y in range(len(level)):
        for x in range(len(level[0])):
            if level[y][x] == 4:
                spawn_points.append((x + 1, y + 1))


# картинки
aim_bullet_image = load_image(r'images\aim_bullet_image.png')
aim_bullet_image_rect = aim_bullet_image.get_rect()
aim_bullet_image = pygame.transform.scale(aim_bullet_image, ((cell_size * 1), (cell_size * 0.4)))

doon_bullet_image = load_image(r'images\doon_bullet_image.png')
doon_bullet_image_rect = doon_bullet_image.get_rect()
doon_bullet_image = pygame.transform.scale(doon_bullet_image, ((cell_size * 0.8), (cell_size * 0.3)))

virtus_bullet_image = load_image(r'images\virtus_bullet_image.png')
virtus_bullet_image_rect = aim_bullet_image.get_rect()
virtus_bullet_image = pygame.transform.scale(virtus_bullet_image, ((cell_size * 0.2), (cell_size * 0.2)))

'''
virtus_sword_image = load_image(r'images\virtus_sword_image.png')
virtus_sword_image_rect = virtus_sword_image.get_rect()
virtus_sword_image = pygame.transform.scale(virtus_sword_image, ((cell_size * 1.2), (cell_size * 1.2)))
virtus_sword_image = pygame.transform.rotate(virtus_sword_image, 45)
# aim_bullet_image = pygame.transform.scale(aim_bullet_image, (5, 5))
'''

airbomb_image = load_image(r'images\airbomb_image.png')
airbomb_image_rect = airbomb_image.get_rect()
airbomb_image = pygame.transform.scale(airbomb_image, (cell_size, cell_size))

smoke_image = load_image(r'images\smoke_image.png')
smoke_image_rect = smoke_image.get_rect()
smoke_image = pygame.transform.scale(smoke_image, (cell_size, cell_size))

breakable_block_image_3000 = load_image(r'images\breakable_block_image_3000.png')
breakable_block_image_3000_rect = breakable_block_image_3000.get_rect()
breakable_block_image_3000 = pygame.transform.scale(breakable_block_image_3000, (cell_size, cell_size))

breakable_block_image_2000 = load_image(r'images\breakable_block_image_2000.png')
breakable_block_image_2000_rect = breakable_block_image_2000.get_rect()
breakable_block_image_2000 = pygame.transform.scale(breakable_block_image_2000, (cell_size, cell_size))

breakable_block_image_1000 = load_image(r'images\breakable_block_image_1000.png')
breakable_block_image_1000_rect = breakable_block_image_1000.get_rect()
breakable_block_image_1000 = pygame.transform.scale(breakable_block_image_1000, (cell_size, cell_size))

unbreakable_block_image = load_image(r'images\unbreakable_block_image.png')
unbreakable_block_image_rect = unbreakable_block_image.get_rect()
unbreakable_block_image = pygame.transform.scale(unbreakable_block_image, (cell_size, cell_size))

abyss_image = load_image(r'images\abyss_image.png')
abyss_image_rect = abyss_image.get_rect()
abyss_image = pygame.transform.scale(abyss_image, (cell_size, cell_size))

spawn_point_image = load_image(r'images\spawn_point_image.png')
spawn_point_image_rect = spawn_point_image.get_rect()
spawn_point_image = pygame.transform.scale(spawn_point_image, (cell_size, cell_size))

search_image_1 = load_image(r'images\search_image_1.png')
search_image_1 = pygame.transform.scale(search_image_1, (HEIGHT / 3, HEIGHT / 3))
search_image_2 = load_image(r'images\search_image_2.png')
search_image_2 = pygame.transform.scale(search_image_2, (HEIGHT / 3, HEIGHT / 3))
search_image_3 = load_image(r'images\search_image_3.png')
search_image_3 = pygame.transform.scale(search_image_3, (HEIGHT / 3, HEIGHT / 3))
search_image_4 = load_image(r'images\search_image_4.png')
search_image_4 = pygame.transform.scale(search_image_4, (HEIGHT / 3, HEIGHT / 3))

background_lobby = load_image(r'images\background_lobby.png')
background_lobby_rect = background_lobby.get_rect()
background_lobby = pygame.transform.scale(background_lobby, (WIDTH, HEIGHT))

background_characters = load_image(r'images\background_characters.png')
background_characters_rect = background_characters.get_rect()
background_characters = pygame.transform.scale(background_characters, (WIDTH, HEIGHT))

background_search = load_image(r'images\background_search.png')
background_search_rect = background_search.get_rect()
background_search = pygame.transform.scale(background_search, (WIDTH, HEIGHT))

background_map = load_image(r'images\background_map.png')
background_map_rect = background_map.get_rect()
background_map = pygame.transform.scale(background_map, (WIDTH * 5, HEIGHT * 5))

cursor_default = load_image('images\cursor_default.png')
# cursor_default.set_colorkey(WHITE)
cursor_clicked = load_image('images\cursor_clicked.png')
# cursor_clicked = pygame.transform.scale(cursor_clicked, (32, 32))
# cursor_clicked.set_colorkey(WHITE)

arrow_left_button = load_image(r'images\arrow_left.png')
arrow_left_button = pygame.transform.scale(arrow_left_button, (HEIGHT / 8, HEIGHT / 8))

arrow_left_button_clicked = load_image(r'images\arrow_left_clicked.png')
arrow_left_button_clicked = pygame.transform.scale(arrow_left_button_clicked, (HEIGHT / 8, HEIGHT / 8))

arrow_right_button = load_image(r'images\arrow_right.png')
arrow_right_button = pygame.transform.scale(arrow_right_button, (HEIGHT / 8, HEIGHT / 8))

arrow_right_button_clicked = load_image(r'images\arrow_right_clicked.png')
arrow_right_button_clicked = pygame.transform.scale(arrow_right_button_clicked, (HEIGHT / 8, HEIGHT / 8))

green_button = load_image(r'images\green_button.png')
green_button = pygame.transform.scale(green_button, (HEIGHT / 4, HEIGHT / 10))

resolution_button = load_image(r'images\resolution_button.png')
resolution_button = pygame.transform.scale(resolution_button, (HEIGHT / 4, HEIGHT / 10))

red_button = load_image(r'images\red_button.png')
red_button = pygame.transform.scale(red_button, (HEIGHT / 4, HEIGHT / 10))

back_button_image = load_image(r'images\back_button.png')
back_button_image = pygame.transform.scale(back_button_image, (HEIGHT / 10, HEIGHT / 10))

settings_button = load_image(r'images\settings_button.png')
settings_button = pygame.transform.scale(settings_button, (HEIGHT / 10, HEIGHT / 10))

characters_button = load_image(r'images\characters_button.png')
characters_button = pygame.transform.scale(characters_button, (HEIGHT / 4, HEIGHT / 10))

# init
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

# звуки
shoot_sound_aim = pygame.mixer.Sound(r'sounds/aim_bullet.mp3')
shoot_sound_aim.set_volume(0.1)
shoot_sound_virtus = pygame.mixer.Sound(r'sounds/virtus_bullet.mp3')
shoot_sound_virtus.set_volume(0.1)
skill_sound = pygame.mixer.Sound(r'sounds/skill.mp3')
skill_sound.set_volume(0.1)

pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'sounds\main_theme.mp3'))
pygame.mixer.music.set_volume(music_volume)
if music_on:
    pygame.mixer.music.play(loops=-1)

# шрифты
font0 = pygame.font.Font(None, int(cell_size * 0.2))  # 16
font1 = pygame.font.Font(None, int(cell_size * 0.4))  # 32
font2 = pygame.font.Font(None, int(cell_size * 0.6))  # 48
font3 = pygame.font.Font(None, int(cell_size * 0.8))  # 64
font4 = pygame.font.Font(None, int(cell_size * 1))  # 80

# игровой уровень
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