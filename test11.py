import pygame
import os
import random

def load_image(name, colorkey=-1):
    fullname = os.path.join('game', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()     
    return image

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
pygame.display.flip()

all_sprites = pygame.sprite.Group()
rvn = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, coords1, coords2):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(coords1, coords2)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, 
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

        
class RavenSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(rvn)
        self.frames = []
        self.frames.append(load_image('raven-black0001.png'))
        self.frames.append(load_image('raven-black0002.png'))
        self.frames.append(load_image('raven-black0003.png'))
        self.frames.append(load_image('raven-black0004.png'))
        self.frames.append(load_image('raven-black0005.png'))
        self.frames.append(load_image('raven-black0006.png'))
        self.frames.append(load_image('raven-black0007.png'))
        self.frames.append(load_image('raven-black0008.png'))
        self.frames.append(load_image('raven-black0009.png'))
        self.frames.append(load_image('raven-black0010.png'))
        self.frames.append(load_image('raven-black0011.png'))
        self.frames.append(load_image('raven-black0012.png'))
        self.frames.append(load_image('raven-black0013.png'))
        self.frames.append(load_image('raven-black0014.png'))
        self.frames.append(load_image('raven-black0015.png'))
        self.frames.append(load_image('raven-black0016.png'))
        self.frames.append(load_image('raven-black0017.png'))
        self.frames.append(load_image('raven-black0018.png'))
        self.frames.append(load_image('raven-black0019.png'))
        self.frames.append(load_image('raven-black0020.png'))
        self.frames.append(load_image('raven-black0021.png'))
        self.frames.append(load_image('raven-black0022.png'))
        self.frames.append(load_image('raven-black0023.png'))
        self.frames.append(load_image('raven-black0024.png'))
        self.frames.append(load_image('raven-black0025.png'))
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 210
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

screen_rect = (0, 0, width, height)


class Particle(pygame.sprite.Sprite):
    fire = [load_image("rsz_12.png", -1)]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 1

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()
            
def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))

def start():
    level = 0
    fps = 100
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("rsz_circulo-de-neon-com-efeito-de-luz-moldura-redonda-moderna-com-espaco-vazio_106065-49.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 300
    sprite.rect.y = 300
    all_sprites.add(sprite)
    font = pygame.font.SysFont('yugothicmediumyugothicuiregular', 20)
    text1 = font.render("START", 1, (229, 76, 255))
    font = pygame.font.SysFont('segoescript', 50)
    text2 = font.render("ДУШЕВНОЕ НЕЧТО", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 20)
    text3 = font.render("", 1, (229, 76, 255))    
    return text1, (368, 390), text2, (150, 150), text3, (0, 0), level, fps

def passage_one():
    level = 1
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("begin.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 100
    all_sprites.add(sprite)
    fps = 1
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, (0, 0), text2, (0, 0), text3, (0, 0), level, fps

def level_one():  # introduction
    level = 1
    fps = 100
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("character.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 75
    all_sprites.add(sprite)
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("Что? Ни черта не помню... Ничего не понимаю. Ну, хотя бы голова на месте...", 1, (255, 255, 255))
    font = pygame.font.SysFont('candara', 20)
    text2 = font.render("И что же мне делать? J'ai une âme solitaire.... О, какая-то записка...", 1, (255, 255, 255))
    font = pygame.font.SysFont('impact', 20)
    text3 = font.render("Прочитать записку", 1, (0, 0, 0))
    return text1, (80, 700), text2, (80, 720), text3, (318, 755), level, fps

def level_two():
    level = 2
    fps = 100
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("note.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = -400
    all_sprites.add(sprite)
    font = pygame.font.SysFont('impact', 28)
    text1 = font.render("Найти его в контактах и позвать", 1, (0, 0, 0))
    font = pygame.font.SysFont('segoeprint', 25)
    text2 = font.render("Его зовут Дейл. Если он назвался тобой - он солгал.", 1, (255, 255, 255))
    font = pygame.font.SysFont('segoeprint', 40)
    text3 = font.render("Он приятный собеседник.", 1, (255, 255, 255))
    return text1, (210, 500), text2, (20, 220), text3, (100, 260), level, fps

def level_three():
    level = 3
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("the_bad_guy.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 75
    all_sprites.add(sprite)
    fps = 100
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("Мы встречались, не так ли? У вас дома. На самом деле я и сейчас там.", 1, (85, 170, 0))
    font = pygame.font.SysFont('candara', 20)
    text2 = font.render("В общем, здесь неподалёку поселение ворон-мутантов. Ты должен их уничтожить.", 1, (85, 170, 0))
    font = pygame.font.SysFont('impact', 20)
    text3 = font.render("Выполнить миссию", 1, (0, 0, 0))
    return text1, (80, 700), text2, (80, 720), text3, (318, 755), level, fps

def passage_two():
    level = 4
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("travelling.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 100
    all_sprites.add(sprite)
    fps = 1
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, (0, 0), text2, (0, 0), text3, (0, 0), level, fps

def level_four():
    level = 4
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("killing.png", None)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("raven-black0001.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 300
    sprite.rect.y = 300
    all_sprites.add(sprite)
    fps = 100
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("Чтобы их убить нужно просто на них кликнуть, и они разлетятся пузырьками.", 1, (85, 170, 0))
    font = pygame.font.SysFont('candara', 17)
    text2 = font.render("Я предпочитаю по-своему запоминать события. Не обязательно так, как они на самом деле происходили.", 1, (85, 170, 0))
    font = pygame.font.SysFont('impact', 20)
    text3 = font.render("Начать", 1, (0, 0, 0))
    return text1, (80, 700), text2, (5, 720), text3, (375, 755), level, fps

def level_five():
    level = 5
    for elem in all_sprites:
        elem.kill()
    for elem in rvn:
        elem.rect.x = random.randint(0, 600)
        elem.rect.y = random.randint(0, 600)
    fps = 20
    font = pygame.font.SysFont('trebuchetms', 20)
    text1 = font.render(f"Убито: 0", 1, (255, 0, 0))
    font = pygame.font.SysFont('candara', 20)
    text2 = font.render("", 1, (85, 170, 0))
    font = pygame.font.SysFont('', 20)
    text3 = font.render("", 1, (0, 0, 0))
    return text1, (700, 50), text2, (80, 720), text3, (375, 755), level, fps

def passage_three():
    level = 6
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("chaos.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 100
    all_sprites.add(sprite)
    fps = 1
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, (0, 0), text2, (0, 0), text3, (0, 0), level, fps

def level_six():
    level = 6
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("plan.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x += 75
    all_sprites.add(sprite)
    fps = 100
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("Работа завершена. Есть время погулять, посмотреть на город.", 1, (255, 255, 255))
    font = pygame.font.SysFont('candara', 16)
    text2 = font.render("Порой, когда мы смотрим в глаза, случается, что мы видим глаза, глаза..., в которых не видно души, лишь темнота.", 1, (255, 255, 255))
    font = pygame.font.SysFont('impact', 20)
    text3 = font.render("Пойти гулять", 1, (0, 0, 0))
    return text1, (80, 700), text2, (5, 720), text3, (340, 755), level, fps

def town():
    level = 7
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("house.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 75
    sprite.rect.y = 400
    all_sprites.add(sprite)
    for _ in range(6):
        red_fire = AnimatedSprite(load_image("fire4_64_0.png", -1), 10, 6, 64, 64, random.randint(60, 180), random.randint(430, 520))
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("coffee.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 575
    sprite.rect.y = 75
    all_sprites.add(sprite)
    tree = AnimatedSprite(load_image("tree.png", -1), 15, 4, 326, 300, 400, 400)
    fps = 20
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("Куда же пойти?", 1, (255, 255, 255))
    font = pygame.font.SysFont('impact', 20)
    text2 = font.render("В дом", 1, (0, 0, 0))
    font = pygame.font.SysFont('impact', 20)
    text3 = font.render("В кофейню", 1, (0, 0, 0))
    return text1, (80, 700), text2, (170, 755), text3, (550, 755), level, fps

def passage_four():
    level = 8
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("arson.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 100
    all_sprites.add(sprite)
    fps = 1
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, (0, 0), text2, (0, 0), text3, (0, 0), level, fps    

def maze():
    level = 8
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("red.png", -1)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("maze.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 25
    sprite.rect.y = 50
    sprite.mask = pygame.mask.from_surface(sprite.image)
    all_sprites.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("owl.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 400
    sprite.rect.y = 625
    sprite.mask = pygame.mask.from_surface(sprite.image)
    all_sprites.add(sprite)    
    fps = 20
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("Нужно дойти до центра лабиринта, управляя стрелочками.", 1, (255, 255, 255))
    font = pygame.font.SysFont('candara', 20)
    text2 = font.render('Помни: Совы не то, чем они кажутся', 1, (255, 255, 255))
    font = pygame.font.SysFont('impact', 20)
    text3 = font.render("", 1, (0, 0, 0))
    return text1, (80, 700), text2, (80, 720), text3, (570, 755), level, fps

def passage_five():
    level = 9
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("flower.png", None)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    fps = 1
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, (0, 0), text2, (0, 0), text3, (0, 0), level, fps

def bar():
    level = 9
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("the_girl.png", None)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    fps = 100
    font = pygame.font.SysFont('candara', 18)
    text1 = font.render("Не ищи все ответы сразу. Когда строят дорогу, камни укладывают один за другим.", 1, (170, 170, 255))
    font = pygame.font.SysFont('candara', 20)
    text2 = font.render("Что?", 1, (255, 255, 255))
    font = pygame.font.SysFont('candara', 20)
    text3 = font.render("Рай - это очень большое и интересное место, сэр.", 1, (170, 170, 255))
    return text1, (80, 650), text2, (80, 670), text3, (80, 690), level, fps

def passage_six():
    level = 10
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("angel.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 100
    all_sprites.add(sprite)
    fps = 0.75
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 50)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, (0, 0), text2, (0, 0), text3, (0, 0), level, fps    

def final():
    level = 10
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("the end.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 100
    all_sprites.add(sprite)    
    font = pygame.font.SysFont('candara', 20)
    text1 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('segoescript', 50)
    text2 = font.render("", 1, (229, 76, 255))
    font = pygame.font.SysFont('candara', 20)
    text3 = font.render("", 1, (229, 76, 255))
    return text1, pos1, text2, pos2, text3, pos3, level, fps

level = 0
running = True
movement = False
been = set()
monsters = []
for _ in range(30):
    raven = RavenSprite()
for _ in range(30):
    monsters.append([random.choice([-4, -3, -2, -1, 1, 2, 3, 4]), random.choice([-4, -3, -2, -1, 1, 2, 3, 4])])
most = 30
n = 0  # for length of pictures
k = 0  # for finding pictures in all_sprites
tr = False
count = 0
clock = pygame.time.Clock()
text1, pos1, text2, pos2, text3, pos3, level, fps = start()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level == 0:
                if 337 <= event.pos[0] <= 462 and 338 <= event.pos[1] <= 461:
                    n = 0
                    text1, pos1, text2, pos2, text3, pos3, level, fps = passage_one()
            if level == 1:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    text1, pos1, text2, pos2, text3, pos3, level, fps = level_two()
            if level == 2:
                if 200 <= event.pos[0] <= 600 and 500 <= event.pos[1] <= 540:
                    text1, pos1, text2, pos2, text3, pos3, level, fps = level_three()
            if level == 3:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    n = 0
                    text1, pos1, text2, pos2, text3, pos3, level, fps = passage_two()
            if level == 4 and n > 0:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    movement = True
                    n = 0
                    text1, pos1, text2, pos2, text3, pos3, level, fps = level_five()
            if level == 5:
                z = 0
                for elem in rvn:
                    if z < most:
                        if elem.rect.x <= event.pos[0] and elem.rect.x + 200 >= event.pos[0] and elem.rect.y <= event.pos[1] and elem.rect.y + 200 >= event.pos[1]:
                            create_particles(pygame.mouse.get_pos())
                            elem.kill()
                            count += 1
                            most -= 1
                    z += 1
                font = pygame.font.SysFont('trebuchetms', 20)
                text1 = font.render(f"Убито: {count}", 1, (255, 0, 0))
                if count == 30:
                    n = 0
                    text1, pos1, text2, pos2, text3, pos3, level, fps = passage_three()
            if level == 6 and n > 1:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    text1, pos1, text2, pos2, text3, pos3, level, fps = town()
            if level == 7:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790:
                    n = 0
                    text1, pos1, text2, pos2, text3, pos3, level, fps = passage_four()
                if 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    n = 0
                    if len(been) == 1:
                        text1, pos1, text2, pos2, text3, pos3, level, fps = passage_five()
                    else:
                        tr = True
            if level == 9 and n > 0:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    n = 0
                    if len(been) == 2:
                        text1, pos1, text2, pos2, text3, pos3, level, fps = passage_six()
                    else:
                        text1, pos1, text2, pos2, text3, pos3, level, fps = town()
        if event.type == pygame.KEYDOWN and level == 8:
            k = 0
            for elem in all_sprites:
                if k == 2:
                    if 307 <= elem.rect.x <= 461 and 291 <= elem.rect.y <= 446:
                        n = 0
                        if len(been) == 2:
                            text1, pos1, text2, pos2, text3, pos3, level, fps = passage_six()
                        else:
                            text1, pos1, text2, pos2, text3, pos3, level, fps = town()
                k += 1
            k = 0
            if event.key == pygame.K_UP:
                for sprite in all_sprites:
                    if k == 2:
                        sprite.rect.y -= 10
                        z = 0
                        for elem in all_sprites:
                            if z == 1:
                                if pygame.sprite.collide_mask(sprite, elem):
                                    sprite.rect.y += 10
                            z += 1
                    k += 1
            if event.key == pygame.K_DOWN:
                for sprite in all_sprites:
                    if k == 2:
                        sprite.rect.y += 10
                        z = 0
                        for elem in all_sprites:
                            if z == 1:
                                if pygame.sprite.collide_mask(sprite, elem):
                                    sprite.rect.y -= 10
                            z += 1
                    k += 1
            if event.key == pygame.K_RIGHT:
                for sprite in all_sprites:
                    if k == 2:
                        sprite.rect.x += 10
                        z = 0
                        for elem in all_sprites:
                            if z == 1:
                                if pygame.sprite.collide_mask(sprite, elem):
                                    sprite.rect.x -= 10
                            z += 1
                    k += 1
            if event.key == pygame.K_LEFT:
                for sprite in all_sprites:
                    if k == 2:
                        sprite.rect.x -= 10
                        z = 0
                        for elem in all_sprites:
                            if z == 1:
                                if pygame.sprite.collide_mask(sprite, elem):
                                    sprite.rect.x += 10
                            z += 1
                    k += 1
    screen.fill((0, 0, 0))
    if movement:
        all_sprites.update()
        rvn.update()
        rvn.draw(screen)
    all_sprites.draw(screen)    
    if level == 1:
        if n == 1:
            text1, pos1, text2, pos2, text3, pos3, level, fps = level_one()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
        n += 1
    if level == 2:
        pygame.draw.rect(screen, (255, 255, 127), ((200, 500), (400, 40)))
    if level == 3:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
    if level == 4:
        if n == 1:
            text1, pos1, text2, pos2, text3, pos3, level, fps = level_four()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
        n += 1
    if level == 5:
        k = 0
        for elem in rvn:
            if k < most:
                if elem.rect.x >= 800:
                    elem.rect.x = -200
                    monsters[k][0] = 4
                if elem.rect.x <= -200:
                    elem.rect.x = 800
                    monsters[k][0] = -4
                if elem.rect.y >= 800:
                    elem.rect.y = -200
                    monsters[k][1] = 4
                if elem.rect.y <= -200:
                    elem.rect.y = 800
                    monsters[k][1] = -4
                elem.rect.x += monsters[k][0]
                elem.rect.y += monsters[k][1]                
            k += 1
    if level == 6:
        if n == 1:
            text1, pos1, text2, pos2, text3, pos3, level, fps = level_six()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
        n += 1     
    if level == 7:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
        pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
        k = 0
        for elem in all_sprites:
            if k == 9:
                elem.rect.x += 1
                if elem.rect.x == 800:
                    elem.rect.x = 0
            k += 1
        if tr:
            font = pygame.font.SysFont('candara', 20)
            text4 = font.render("Тебя ждут дома", 1, (255, 24, 35))
            screen.blit(text4, (315, 655))
    if level == 8:
        if n == 1:
            tr = False
            been.add('maze')
            text1, pos1, text2, pos2, text3, pos3, level, fps = maze()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        n += 1
    if level == 9:
        if n == 1:
            been.add('bar')
            text1, pos1, text2, pos2, text3, pos3, level, fps = bar()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
            font = pygame.font.SysFont('impact', 20)
            text4 = font.render("Выпить кружку кофе", 1, (0, 0, 0))
            screen.blit(text4, (310, 755))
        n += 1
    if level == 10:
        if n == 1:
            text1, pos1, text2, pos2, text3, pos3, level, fps = final()
        n += 1
    screen.blit(text1, pos1)
    screen.blit(text2, pos2)
    screen.blit(text3, pos3)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
