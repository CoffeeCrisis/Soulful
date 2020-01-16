import pygame
import os
import random
import copy

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
extra = pygame.sprite.Group()
clouds = pygame.sprite.Group()


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
        super().__init__(extra)
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
    return level, fps

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
    return level, fps

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
    return level, fps

def level_two():
    level = 2
    fps = 100
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("the_bad_guy.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 96
    all_sprites.add(sprite)
    return level, fps

def level_three():
    level = 3
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("evil.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 96
    all_sprites.add(sprite)
    fps = 100
    return level, fps

def level_four():
    level = 4
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("cafe.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 150
    all_sprites.add(sprite)
    fps = 100
    return level, fps

def level_five():
    level = 5
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("girl.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 98
    all_sprites.add(sprite)
    fps = 100
    return level, fps

def level_six():
    level = 6
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("light.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 110
    all_sprites.add(sprite)
    fps = 100
    return level, fps

def level_seven():
    level = 7
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("plan.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 76
    all_sprites.add(sprite)
    fps = 100
    return level, fps

def before_town():
    level = 'town'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("clock.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 85
    all_sprites.add(sprite)
    fps = 1
    return level, fps

def town():
    level = 'town'
    for elem in all_sprites:
        elem.kill()
    for i in range(8):
        for j in range(4):
            sprite = pygame.sprite.Sprite()
            sprite.image = load_image("bricks.png", None)
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = i * 100
            sprite.rect.y = 800 - j * 100
            all_sprites.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("house.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 75
    sprite.rect.y = 400
    all_sprites.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("curtain.png", (0, 0, 0))
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 475
    sprite.rect.y = 400
    all_sprites.add(sprite)
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("statue.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 600
    sprite.rect.y = 475
    all_sprites.add(sprite)       
    for _ in range(6):
        red_fire = AnimatedSprite(load_image("fire4_64_0.png", -1), 10, 6, 64, 64, random.randint(60, 180), random.randint(430, 520))
    fps = 20
    return level, fps

def before_dark():
    level = 'dark'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("arson.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 100
    all_sprites.add(sprite)
    fps = 1
    return level, fps

def dark():
    level = 'dark'
    for elem in all_sprites:
        elem.kill()
    for elem in rvn:
        elem.rect.x = random.randint(0, 600)
        elem.rect.y = random.randint(0, 600)
    fps = 20
    return level, fps

def after_dark():
    level = 'town'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("chaos.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.y = 100
    all_sprites.add(sprite)
    fps = 1
    return level, fps

def before_maze():
    level = 'maze'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("red room.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 91
    all_sprites.add(sprite)
    fps = 1
    return level, fps

def maze():
    level = 'maze'
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
    return level, fps

def after_maze():
    level = 'town'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("rr.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 106
    all_sprites.add(sprite)
    fps = 1
    return level, fps
    
def before_cafe():
    level = 'cafe'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("flower.png", None)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    fps = 1
    return level, fps

def cafe():
    level = 'cafe'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("the_girl.png", None)
    sprite.rect = sprite.image.get_rect()
    all_sprites.add(sprite)
    fps = 100
    return level, fps

def end():
    level = 'end'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("angel.png", None)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 100
    all_sprites.add(sprite)
    fps = 0.75
    return level, fps

def final():
    level = 'end'
    for elem in all_sprites:
        elem.kill()
    sprite = pygame.sprite.Sprite()
    sprite.image = load_image("the end.png", -1)
    sprite.rect = sprite.image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 100
    all_sprites.add(sprite)    
    return level, fps

level = 0
running = True
been = set()
monsters = []
sprite = pygame.sprite.Sprite()
sprite.image = load_image("cloud3.png", None)
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 25
sprite.rect.y = 50
clouds.add(sprite)
sprite = pygame.sprite.Sprite()
sprite.image = load_image("cloud3.png", None)
sprite.rect = sprite.image.get_rect()
sprite.rect.x = 625
sprite.rect.y = 50
clouds.add(sprite)
for _ in range(30):
    raven = RavenSprite()
for _ in range(30):
    monsters.append([random.choice([-4, -3, -2, -1, 1, 2, 3, 4]), random.choice([-4, -3, -2, -1, 1, 2, 3, 4])])
most = 30
n = 0  # for length of pictures
k = 0  # for finding pictures in all_sprites
count = 0
clock = pygame.time.Clock()
level, fps = start()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if level == 0:
                if 337 <= event.pos[0] <= 462 and 338 <= event.pos[1] <= 461:
                    n = 0
                    level, fps = passage_one()
            if level == 1 and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790:
                    answer = 1
                    n = 0
                    level, fps = level_two()
                if 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    answer = 2
                    n = 0
                    level, fps = level_two()                    
            if level == 2 and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790 or 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = level_three()                  
            if level == 3 and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790:
                    answer = 1
                    n = 0
                    level, fps = level_four()
                if 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    answer = 2
                    n = 0
                    level, fps = level_four()
            if level == 4 and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790 or 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = level_five()
            if level == 5 and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790 or 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = level_six()
            if level == 6 and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790 or 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = level_seven()
            if level == 7 and n > 1:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = before_town()
            if level == 'town' and n > 1:
                if 100 <= event.pos[0] <= 300 and 750 <= event.pos[1] <= 790:
                    n = 0
                    count = 0
                    most = 30
                    rvn = extra.copy()                    
                    level, fps = before_dark()
                if 500 <= event.pos[0] <= 700 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = before_maze()
                if 300 <= event.pos[0] <= 500 and 700 <= event.pos[1] <= 740 and len(been) == 2:
                    n = 0
                    level, fps = before_cafe()
            if level == 'dark' and n > 2:
                z = 0
                for elem in rvn:
                    if z < most:
                        if elem.rect.x <= event.pos[0] and elem.rect.x + 200 >= event.pos[0] and elem.rect.y <= event.pos[1] and elem.rect.y + 200 >= event.pos[1]:
                            create_particles(pygame.mouse.get_pos())
                            rvn.remove(elem)
                            count += 1
                            most -= 1
                    z += 1
                if count == 30:
                    n = 0
                    level, fps = after_dark()
            if level == 'cafe' and n > 0:
                if 300 <= event.pos[0] <= 500 and 750 <= event.pos[1] <= 790:
                    n = 0
                    level, fps = end()
        if event.type == pygame.KEYDOWN and level == 'maze':
            k = 0
            for elem in all_sprites:
                if k == 2:
                    if 307 <= elem.rect.x <= 461 and 291 <= elem.rect.y <= 446:
                        n = 0
                        level, fps = after_maze()
                k += 1
    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    if level == 0:
        font = pygame.font.SysFont('yugothicmediumyugothicuiregular', 20)
        text1 = font.render("START", 1, (229, 76, 255))
        font = pygame.font.SysFont('segoescript', 50)
        text2 = font.render("ПУТЬ В НИКУДА", 1, (229, 76, 255))
        screen.blit(text1, (368, 390))
        screen.blit(text2, (150, 150))
    if level == 1:
        if n == 1:
            level, fps = level_one()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
            pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
            font = pygame.font.SysFont('candara', 20)
            text1 = font.render("Что? Ни черта не помню... Ничего не понимаю. Ну, хотя бы голова на месте...", 1, (255, 255, 255))
            font = pygame.font.SysFont('candara', 20)
            text2 = font.render("И что же мне делать? J'ai une âme solitaire.... Ой, кто-то стучится в дверь.", 1, (255, 255, 255))
            font = pygame.font.SysFont('impact', 20)
            text3 = font.render("Открыть дверь", 1, (0, 0, 0))
            font = pygame.font.SysFont('impact', 20)
            text4 = font.render("Не открывать дверь", 1, (0, 0, 0))
            screen.blit(text1, (80, 700))
            screen.blit(text2, (80, 720))
            screen.blit(text3, (118, 755))
            screen.blit(text4, (518, 755))
        n += 1
    if level == 2:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
        pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
        font = pygame.font.SysFont('candara', 20)
        if answer == 1:
            text1 = font.render("Ну спасибо, что наконец-то впустил старого знакомого.", 1, (170, 170, 255))
        if answer == 2:
            text1 = font.render("Нехорошо так поступать со старыми знакомыми.", 1, (170, 170, 255))
        font = pygame.font.SysFont('candara', 20)
        text2 = font.render("Не бывает действий без последствий, но бывает волшебство.", 1, (170, 170, 255))
        font = pygame.font.SysFont('impact', 20)
        text3 = font.render("Мы знакомы?", 1, (0, 0, 0))
        font = pygame.font.SysFont('impact', 20)
        text4 = font.render("Кто вы?", 1, (0, 0, 0))
        screen.blit(text1, (80, 700))
        screen.blit(text2, (80, 720))
        screen.blit(text3, (118, 755))
        screen.blit(text4, (518, 755))
        n += 1
    if level == 3:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
        pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
        font = pygame.font.SysFont('candara', 20)
        text1 = font.render("Ты меня знаешь, я здесь и у тебя дома. Не веришь?", 1, (170, 170, 255))
        font = pygame.font.SysFont('candara', 20)
        text2 = font.render("Можешь позвонить себе на домашний, если хочешь.", 1, (170, 170, 255))
        font = pygame.font.SysFont('impact', 20)
        text3 = font.render("Поверить", 1, (0, 0, 0))
        font = pygame.font.SysFont('impact', 20)
        text4 = font.render("Позвонить", 1, (0, 0, 0))
        screen.blit(text1, (80, 700))
        screen.blit(text2, (80, 720))
        screen.blit(text3, (118, 755))
        screen.blit(text4, (518, 755))
        n += 1
    if level == 4:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
        pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
        font = pygame.font.SysFont('candara', 20)
        if answer == 1:
            text1 = font.render("Знаешь, я в двух местах, потому что в одном месте.", 1, (170, 170, 255))
        if answer == 2:
            text1 = font.render('ГОЛОС В ТРУБКЕ: "я в двух местах, потому что в одном месте."', 1, (170, 170, 255))
        font = pygame.font.SysFont('candara', 20)
        text2 = font.render("Кстати, будет возможность, попробуй здешний кофе. Потрясающий.", 1, (170, 170, 255))
        font = pygame.font.SysFont('impact', 20)
        text3 = font.render("Хорошо", 1, (0, 0, 0))
        font = pygame.font.SysFont('impact', 20)
        text4 = font.render("Не люблю кофе", 1, (0, 0, 0))
        screen.blit(text1, (80, 700))
        screen.blit(text2, (80, 720))
        screen.blit(text3, (118, 755))
        screen.blit(text4, (518, 755))
        n += 1
    if level == 5:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
        pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
        font = pygame.font.SysFont('candara', 20)
        text1 = font.render('Правда, этот кофе просто нечто. Вкус создаётся у тебя в голове.', 1, (170, 170, 255))
        font = pygame.font.SysFont('candara', 20)
        text2 = font.render("А помнишь... ? Когда-то... Один твой сон...", 1, (170, 170, 255))
        font = pygame.font.SysFont('impact', 20)
        text3 = font.render("Что?", 1, (0, 0, 0))
        font = pygame.font.SysFont('impact', 20)
        text4 = font.render("Какой?", 1, (0, 0, 0))
        screen.blit(text1, (80, 700))
        screen.blit(text2, (80, 720))
        screen.blit(text3, (118, 755))
        screen.blit(text4, (518, 755))
        n += 1
    if level == 6:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
        pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
        font = pygame.font.SysFont('candara', 20)
        text1 = font.render('Это не важно... Ответь, кто этот спящий?', 1, (170, 170, 255))
        font = pygame.font.SysFont('candara', 20)
        text2 = font.render("Ещё не понял, где ты?", 1, (170, 170, 255))
        font = pygame.font.SysFont('impact', 20)
        text3 = font.render("Нет", 1, (0, 0, 0))
        font = pygame.font.SysFont('impact', 20)
        text4 = font.render("Возможно", 1, (0, 0, 0))
        screen.blit(text1, (80, 700))
        screen.blit(text2, (80, 720))
        screen.blit(text3, (118, 755))
        screen.blit(text4, (518, 755))
        n += 1     
    if level == 7:
        pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
        pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
        font = pygame.font.SysFont('candara', 20)
        text1 = font.render('Я не могу ничего больше тебе сказать.', 1, (170, 170, 255))
        font = pygame.font.SysFont('candara', 20)
        text2 = font.render("Может быть найдёшь ответы где-нибудь... не здесь", 1, (170, 170, 255))
        font = pygame.font.SysFont('impact', 20)
        text3 = font.render("Пойти гулять", 1, (0, 0, 0))
        screen.blit(text1, (80, 700))
        screen.blit(text2, (80, 720))
        screen.blit(text3, (318, 755))
        n += 1
    if level == 'town':
        if n == 1:
            level, fps = town()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((100, 750), (200, 40)))
            pygame.draw.rect(screen, (255, 255, 127), ((500, 750), (200, 40)))
            font = pygame.font.SysFont('candara', 20)
            text1 = font.render('Куда же пойти?', 1, (255, 255, 255))
            font = pygame.font.SysFont('impact', 20)
            text2 = font.render("Тёплое тёмное место", 1, (0, 0, 0))
            font = pygame.font.SysFont('impact', 20)
            text3 = font.render("Красная комната", 1, (0, 0, 0))
            screen.blit(text1, (80, 700))
            screen.blit(text2, (108, 755))
            screen.blit(text3, (518, 755))
            if len(been) == 2:
                pygame.draw.rect(screen, (170, 0, 127), ((300, 700), (200, 40)))
                font = pygame.font.SysFont('impact', 20)
                text4 = font.render("В кофейню", 1, (0, 0, 0))
                screen.blit(text4, (318, 705))
            for elem in clouds:
                elem.rect.x += 1
                if elem.rect.x == 800:
                    elem.rect.x = -360
            clouds.draw(screen)            
        n += 1
    if level == 'dark':
        if n == 1:
            been.add('dark')
            level, fps = dark()
        if n > 1:
            font = pygame.font.SysFont('trebuchetms', 20)
            text1 = font.render(f"Убито: {count}/30", 1, (255, 0, 0))
            screen.blit(text1, (650, 50))
            rvn.update()
            rvn.draw(screen)
            k = 0
            for elem in rvn:
                if k < most:
                    if elem.rect.x >= 800:
                        elem.rect.x =-200
                        monsters[k][0] = random.choice([3, 4])
                    if elem.rect.x <= -200:
                        elem.rect.x = 800
                        monsters[k][0] = random.choice([-3, -4])
                    if elem.rect.y >= 800:
                        elem.rect.y=-200
                        monsters[k][1] = random.choice([3, 4])
                    if elem.rect.y <= -200:
                        elem.rect.y = 800
                        monsters[k][1] = random.choice([-3, -4])
                    elem.rect.x += monsters[k][0]
                    elem.rect.y += monsters[k][1]
                k += 1
        n += 1
    if level == 'cafe':
        if n == 1:
            been.add('cafe')
            level, fps = cafe()
        if n > 1:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            pygame.draw.rect(screen, (255, 255, 127), ((300, 750), (200, 40)))
            font = pygame.font.SysFont('candara', 18)
            text1 = font.render("Не ищи все ответы сразу. Когда строят дорогу, камни укладывают один за другим.", 1, (170, 170, 255))
            font = pygame.font.SysFont('candara', 20)
            text2 = font.render("Что?", 1, (255, 255, 255))
            font = pygame.font.SysFont('candara', 20)
            text3 = font.render("Рай - это очень большое и интересное место, сэр.", 1, (170, 170, 255))
            font = pygame.font.SysFont('impact', 20)
            text4 = font.render("Выпить кружку кофе", 1, (0, 0, 0))
            screen.blit(text1, (80, 650))
            screen.blit(text2, (80, 670))
            screen.blit(text3, (80, 690))
            screen.blit(text4, (310, 755))
        n += 1
    if level == 'end':
        if n == 1:
            level, fps = final()
        n += 1
    if level == 'maze':
        n += 1
        if n == 2:
            been.add('maze')
            level, fps = maze()
        if n > 2:
            pygame.draw.rect(screen, (0, 0, 0), ((0, 700), (800, 100)))
            font = pygame.font.SysFont('candara', 20)
            text1 = font.render("Нужно дойти до центра лабиринта, управляя стрелочками.", 1, (255, 255, 255))
            font = pygame.font.SysFont('candara', 20)
            text2 = font.render('Помни: Совы не то, чем они кажутся', 1, (255, 255, 255))
            screen.blit(text1, (80, 700))
            screen.blit(text2, (80, 720))
        if event.type == pygame.KEYDOWN:
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
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
