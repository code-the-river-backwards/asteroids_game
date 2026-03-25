import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # initializing pygame
    pygame.init()
    
    # resolution
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # fps and frame time logic from pygame
    clock = pygame.time.Clock()
    dt = 0

    # Player Object( instance
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)

    # main game loop
    while True:
        
        log_state()
        
        # working quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        
        # drawing the player
        player.draw(screen)

        pygame.display.flip()

        # FPS and frame time
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
