from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('среншин инфаркт')
background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()
FPS = 60 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 30:
            self.rect.y += self.speed
    def fire(self):
        pylu = pyli('palka.png', self.rect.centerx, self.rect.top, 15, 20, 20)
        pylus.add(pylu)

pylus = sprite.Group()

lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 600:
            self.rect.y = 0
            x = randint(0, 500)
            lost = lost + 1
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
font3 = font.Font(None, 36)
killer = 0
healf = 10
class pyli(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class asteriod(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 600:
            self.rect.y = 0
            x = randint(0, 500)
            

palka = Player('palka.png', 1, 1, 150, 150, 5)
ufos = sprite.Group()
for i in range(1):
    vrag = Enemy('mach.png', randint(0,650), randint(-100,0), 50, 50, randint(1,5))
    ufos.add(vrag)

asters = sprite.Group()
for i in range(1):
    asterio = asteriod('fon.jpg', randint(0,650), randint(-100,0), 50, 50, randint(1,5))
    asters.add(asterio)

game = True
while game:
    
    lose = font2.render('ne ok', 1, (255,255,255))
    win = font2.render('ok', 1, (255,255,255))

    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

    

    text_lose1 = font1.render('пропушено:' + str(lost), 1, (255, 255, 255))
    window.blit(text_lose1, (10, 200))

    text_lose = font2.render('счет:' + str(killer), 1, (255, 255, 255))
    window.blit(text_lose, (10, 20))

    text_lose2 = font3.render('жизни:' + str(healf), 1, (255, 255, 255))
    window.blit(text_lose2, (10, 400))

    palka.reset()
    palka.update()

    ufos.draw(window)
    ufos.update()

    pylus.draw(window)
    pylus.update()

    asters.draw(window)
    asters.update()

   

    clock.tick(FPS)
    display.update()