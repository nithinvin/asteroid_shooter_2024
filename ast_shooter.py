import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid shooter")

test_surf = pygame.Surface((400,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display_surface.fill((15,140,122))        
    display_surface.blit(test_surf,(1100,600))

    pygame.display.update()
