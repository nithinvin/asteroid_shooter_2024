import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid shooter")
clock = pygame.time.Clock()

ship_surf = pygame.image.load("./graphics/ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center =(640,360))
back_surf = pygame.image.load("./graphics/background.png").convert()

font = pygame.font.Font("./graphics/subatomic.ttf",50)
text_surf = font.render("Space", True, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(120)
    display_surface.fill((0,0,0))
    display_surface.blit(back_surf,(0,0))
    if ship_rect.top > 0:
       ship_rect.y -= 4
    display_surface.blit(ship_surf,ship_rect)
    display_surface.blit(text_surf,(500,200))

    pygame.display.update()
