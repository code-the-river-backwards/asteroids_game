import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *
from shot import *

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
    
    # 2 empty pygame groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # adding all future instances of the Player class to both groups (updatable and drawable)
    Player.containers = (updatable, drawable)
    # Player Object instance
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, radius=PLAYER_RADIUS)

    # new asteroids group
    asteroids = pygame.sprite.Group()
    # adding any future instances of the Asteroids class to the asteroids group
    Asteroid.containers = (asteroids, updatable, drawable)

    # new shots group
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    # adding the new AsteroidField class to only the updateable group
    AsteroidField.containers = (updatable)
    # and creating a new instance of the AsteroidField class as an object
    asteroidfield = AsteroidField()

    # main game loop
    while True:
        
        log_state()
        
        # working quit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        
        # drawing the player
        ## rotating the player before rendering
        updatable.update(dt)

        # checking for collisions in the asteroid group
        for asteroid in asteroids:
            if asteroid.collides_with(player) == True:
                log_event("player_hit")
                print ("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        # FPS and frame time
        clock.tick(60)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
