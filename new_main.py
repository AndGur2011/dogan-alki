import pygame

pygame.init()

window = pygame.display.set_mode((700,600))

window.fill((255, 218, 115))

background = pygame.image.load("fone.jfif")
background = pygame.transform.scale(background, (700,600))
fps = pygame.time.Clock()

move_r = [
pygame.image.load("walk1.png"),pygame.image.load("walk2.png"),
pygame.image.load("walk3.png"),pygame.image.load("walk4.png"),
pygame.image.load("walk5.png"),pygame.image.load("walk6.png")
]

move_l = [
pygame.image.load("walk1-l.png"),pygame.image.load("walk2-l.png"),
pygame.image.load("walk3-l.png"),pygame.image.load("walk4-l.png"),
pygame.image.load("walk5-l.png"),pygame.image.load("walk6-l.png")
]

class Sprite():
    def __init__(self,kartinka,x,y,width,height):
        self.image = pygame.image.load(kartinka)
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

man = Sprite("walk1.png",100,101,69,101)

game = True
right = False
left = False
count = 0
count_l = 0
while game:
    window.fill((255,218, 115))
    man.draw()
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            game = False

        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_RIGHT:
                right = True
            if eve.key == pygame.K_LEFT:
                left = True

        if eve.type == pygame.KEYUP:
            if eve.key == pygame.K_RIGHT:
                right = False
            if eve.key == pygame.K_LEFT:
                left = False

    if right == True:
        window.blit(move_r[count], (man.rect.x , man.rect.y))
        man.rect.x += 5
        if count == 5:
            count = 0
        else:
            count += 1

    if left == True:
        window.blit(move_l[count_l], (man.rect.x , man.rect.y))
        man.rect.x -= 5
        if count_l == 5:
            count_l = 0
        else:
            count_l += 1

    pygame.display.update()

    fps.tick(60)
