import pygame
from circleshape import *
from player import *
from constants import *
dt = 0
player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    print(f" {player.radius}")
    screen.fill("black")
    #player.draw(screen)
    while True == True:
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
        clock.tick(60)
        dt = clock.tick(60)/1000
if __name__ == "__main__":
    main()
