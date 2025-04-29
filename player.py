from circleshape import *
from constants import *
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.timer = 0.0
    def triangle(self): #
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        #print(a)
        #print(b)
        #print(c)
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) #
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys [pygame.K_a]:
            self.rotate(-1 * dt)
        if keys [pygame.K_d]:
            self.rotate(dt)
        if keys [pygame.K_w]:
            self.move(dt)
        if keys [pygame.K_s]:
            self.move(-1 * dt)
        if keys [pygame.K_SPACE]:
            if self.timer <= 0:
                print(PLAYER_SHOOT_SPEED)
                self.shoot(PLAYER_SHOOT_SPEED, self.rotation)
                self.timer = PLAYER_SHOOT_COOLDOWN
            else:
                pass
    def shoot(self, velo, playrot):
        Shot(self.position.x, self.position.y, SHOT_RADIUS, playrot)
class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.velocity = ((pygame.Vector2(0,1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED)
        print("shot created")
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
    def update(self, dt):
        self.position += (self.velocity * dt)
