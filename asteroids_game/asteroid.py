from circleshape import *
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    # splitting the asteroids after it's shot - logic
    def split(self):
        self.kill()

        # if it's already a small asteroid, do nothing
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        # if not, splitting logic time!
        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)

        new_vector1 = self.velocity.rotate(random_angle)
        new_vector2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)
        new_asteroid2 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius)

        new_asteroid1.velocity = new_vector1 * 1.2
        new_asteroid2.velocity = new_vector2 * 1.2