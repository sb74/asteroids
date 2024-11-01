import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.tick() / 1000


if __name__ == "__main__":
    main()
