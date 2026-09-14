import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    # Initialises pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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
