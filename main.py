import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Main game loop
    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Draw the game.
        screen.fill((0, 0, 0))
        pygame.display.flip()

        # Convert delta time to seconds and store it.
        dt = clock.tick(TARGET_FPS) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
