import pygame
from circleshape import *
from player import *
from constants import *
from constants import ASTEROID_SPAWN_RATE
from asteroid import Asteroid
from asteroidfield import AsteroidField
clock = pygame.time.Clock()
dt = clock.tick(60)/1000
killer = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
shots = pygame.sprite.Group()
Shot.containers = (shots, drawable, updatable)
Asteroid.containers = (asteroids, killer, updatable, drawable)
AsteroidField.containers = (updatable)
asteroidfield = AsteroidField()
Player.containers = (updatable, drawable)
player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #print(player.rotation)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill("black")
    #player.draw(screen)
    while True == True:
        print(f"StartLoop:{player.rotation}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for entity in killer:
            if entity.collision_check(player) == True:
                print("Game Over!")
                return
        for entity in killer:
            for shot in shots:
                if entity.collision_check(shot) == True:
                    entity.split()
                    shot.kill()
        for entity in updatable:
            entity.update(dt)
        print(f"After Update: {player.rotation}")
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        print(f"After Draw: {player.rotation}")
        pygame.display.update()
        print(f"After Display Update: {player.rotation}")
        #print(dt)
        #print(player.rotation)
        clock.tick(60)
if __name__ == "__main__":
    main()
