import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.rotation = 0

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH )

    # rotation logic
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation

    # move forward / backwards logic
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    # updating player position after rotation or movement or both
    def update(self, dt):
       keys = pygame.key.get_pressed()

        # rotation keys
       if keys[pygame.K_a]:
           self.rotate(-dt)
       if keys[pygame.K_d]:
           self.rotate(dt)

        # move up / down keys
       if keys[pygame.K_w]:
           self.move(dt)
       if keys[pygame.K_s]:
           self.move(-dt)

        # shooting
       if keys[pygame.K_SPACE]:
           self.shoot()

    # shooting logic
    def shoot(self):

        new_shot = Shot(x=self.position.x, y=self.position.y, radius=SHOT_RADIUS)

        new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    
