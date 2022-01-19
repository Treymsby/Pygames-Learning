import pygame 
from sys import exit 


def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = text_font.render(f'Score: {(round(current_time/1000))}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)

pygame.init()

width, height = 800, 400 # width and height

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock() #Clock Obejct
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0



sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

game_over_surface = text_font.render("Game Over", False, "White")
game_over_rect = game_over_surface.get_rect(center = (400, 50))

snail_pos = (800, 300)
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (snail_pos))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Uninistiales Pygame
            exit()
        if pygame.mouse.get_pressed()[0]:
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint((event.pos)): 
                    player_gravity = -20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 300:
                    player_gravity = -20
            if event.key == pygame.K_RETURN:
                if game_active == False:
                    snail_rect.left = 800
                    game_active = True
                    start_time = pygame.time.get_ticks()
        

    if game_active:
        screen.blit(sky_surface,(0,0)) #Puts one surface over another
        screen.blit(ground_surface,(0,300))
        
        #text
        display_score()

        snail_rect.left += -4
        if snail_rect.right <= 0: snail_rect.left = 800

        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 0.90 
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surface, player_rect)


        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    elif game_active == False:
        screen.fill("Black")
        screen.blit(game_over_surface, game_over_rect)
        

    pygame.display.update() #to update dispay
    clock.tick(60) # loop will only run 60x Per Min

if __name__ == '__main__':
    main()