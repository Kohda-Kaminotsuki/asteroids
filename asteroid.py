import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x, y, radius, *args):
        super().__init__( x, y, radius)
        self.velocity = pygame.Vector2(0,0)
        for arg in args:
            self.velocity = arg
        print("asteroid created")
    def draw(self, screen):
        print("trying to draw")
        pygame.draw.circle( screen, "white", self.position , self.radius, 2)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_modifier = random.uniform(20,50)
            random_angle = self.velocity.rotate(random_modifier) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius, random_angle)
            Asteroid(self.position.x, self.position.y, new_radius, -1 * random_angle)
