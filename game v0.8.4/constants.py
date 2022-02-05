import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = pygame.Color('orange')

settings = open("GameUserSettings.txt", mode="r", encoding="utf8")
sss = settings.readlines()
str_settings = [_.split('=')[-1][:-1] for _ in sss[:-1]] + [sss[-1].split('=')[-1]]
settings.close()

number_of_character = 2
names_of_all_characters = ['aim', 'virtus', 'doon']
count_of_characters = len(names_of_all_characters)
character = names_of_all_characters[number_of_character - 1]

size = WIDTH, HEIGHT = int(str_settings[0]), int(str_settings[1])
music_volume = float(str_settings[2])
music_on = str_settings[3]
if music_on == 'True':
    music_on = True
else:
    music_on = False
sound_on = str_settings[4]
if sound_on == 'True':
    sound_on = True
else:
    sound_on = False
fps_on = str_settings[5]
if fps_on == 'True':
    fps_on = True
else:
    fps_on = False
crit_is_on = True
FPS = 60
mouse_clicked = False
cell_size = WIDTH // 20
spawn_points = []

all_sprites = pygame.sprite.Group()
view_sprites = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
airbombs_group = pygame.sprite.Group()
smokes_group = pygame.sprite.Group()
breakable_blocks_group = pygame.sprite.Group()
unshootable_walls_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
hud_group = pygame.sprite.Group()
players_group = pygame.sprite.Group()