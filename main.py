import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.container = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable.add(player)
    drawable.add(player)

    while True:
        log_state()
        screen.fill('black')

        updatable.update(dt)
        for inst in drawable:
            inst.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000




    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}", f"Screen height: {SCREEN_HEIGHT}", sep='\n')


if __name__ == "__main__":
    main()
