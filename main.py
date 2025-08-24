import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Group management.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Would really prefer to do this on the class but I will follow along.
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    # Main game loop
    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update and draw the game.
        screen.fill((0, 0, 0))

        updatable.update(dt)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # Check for collision between player and asteroids.
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
        # Check for collision between shots and asteroids.
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()

        # Convert delta time to seconds and store it.
        dt = clock.tick(TARGET_FPS) / 1000

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
