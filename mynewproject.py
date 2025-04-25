from pygame import *
from random import *
mixer.init()
clock=time.Clock()
font.init()

class GameSprite(sprite.Sprite):

   def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):       
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.image1 = transform.scale(image.load(player_image), (size_x, size_y))
        self.image2 = transform.scale(image.load('mario1.png'), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.base_x = player_x
        self.rect.y = player_y 
        self.base_y = player_y
        self.size_x = size_x
        self.size_y = size_y
        self.isJump = False
        self.jumpCount = 10
        self.smth = -10

   def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
  
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.image = self.image2
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < win_width - self.size_x:
            self.image = self.image1
            self.rect.x += self.speed


        if keys[K_SPACE]:
            self.isJump = True
        
        if self.isJump == True:
            if self.jumpCount >= self.smth:

                if self.jumpCount < 0:
                    self.rect.y += (self.jumpCount ** 2) // 2
                else:
                    self.rect.y -= (self.jumpCount ** 2) // 2

                self.jumpCount -= 1

                wall.update()

            else:
                self.isJump = False
                self.jumpCount = 10



class Wall(GameSprite):

    def update(self):
        if sprite.collide_rect(player, wall):
            player.isJump = False
            player.rect.y = self.rect.y - player.size_y
        if sprite.collide_rect(player, wall) != True and player.rect.y == self.rect.y:
            player.rect.y = player.base_y


playersizex = 40
playersizey = 70

win_width = 1300
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("super mario?")



background = transform.scale(image.load('background.jpg'), (win_width, win_height))
player = Player("mario.png", 0, win_height / 1.33, 5, playersizex, playersizey)
wall = Wall('wall.png', 450, 500, 0, 200, 50)




finish = False
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))
        wall.reset()
        player.update()
        

        player.reset()

        display.update()
        clock.tick(60)