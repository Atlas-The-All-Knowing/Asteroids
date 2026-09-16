import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    # Initialises pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0.0



    # Game Loop
    while True:
        # Gets the games state and logs it
        log_state()

        # Processes exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Iterates through members of the updatable group running .update on them
        updatable.update(dt)

        # Iterates through all objects in the asteroids group to check if any collide with the player
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Sets the screen to solid black
        screen.fill("black")

        # Iterates through members of the drawable group running .draw on each one
        for obj in drawable:
            obj.draw(screen)

        # Refreshes the display
        pygame.display.flip()

        # Limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
