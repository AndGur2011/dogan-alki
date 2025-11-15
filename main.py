import pygame

pygame.init()

window = pygame.display.set_mode((700,600))

window.fill((255, 218, 115))

background = pygame.image.load("fone.jfif")
background = pygame.transform.scale(background, (700,600))

character = pygame.image.load("persik.png")
character = pygame.transform.scale(character, (100,180))

fps = pygame.time.Clock()

x_char = 100
y_char = 300

move_l = [
pygame.image.load("walk1.png"),pygame.image.load("walk2.png"),
pygame.image.load("walk3.png"),pygame.image.load("walk4.png"),
pygame.image.load("walk5.png"),pygame.image.load("walk6.png")
]

game = True

while game:
    window.blit(background, (0,0))
    window.blit(character, (x_char, y_char))
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            game = False
        if eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_LEFT:
                x_char -= 10
            if eve.key == pygame.K_RIGHT:
                x_char += 10
            if eve.key == pygame.K_UP:
                y_char -= 10
            if eve.key == pygame.K_DOWN:
                y_char += 10

    pygame.display.update()