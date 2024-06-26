import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroid shooter")
clock = pygame.time.Clock()

ship_surf = pygame.image.load("./graphics/ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center =(WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

back_surf = pygame.image.load("./graphics/background.png").convert()

laser_surf = pygame.image.load("./graphics/laser.png").convert_alpha()
laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)

font = pygame.font.Font("./graphics/subatomic.ttf",50)
text_surf = font.render("Space", True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH/2,WINDOW_HEIGHT-80))

test_rect = pygame.Rect(100,200,400,500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = clock.tick(120)/ 1000

    ship_rect.center = pygame.mouse.get_pos()

    print(laser_rect.y)
    print(dt)
    laser_rect.y -= round(200 * dt)

    display_surface.fill((0,0,0))
    display_surface.blit(back_surf,(0,0))

    display_surface.blit(text_surf,text_rect)
    pygame.draw.rect(display_surface,(255,255,255),text_rect.inflate(30,30), width = 8, border_radius = 5)
    
    display_surface.blit(laser_surf,laser_rect)
    display_surface.blit(ship_surf,ship_rect)

    pygame.display.update()
