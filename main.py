import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    # Initialises pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0.0

    # Game Loop
    while True:
        # Gets the games state and logs it
        log_state()

        # Processes events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Sets the screen to solid black, then updates it
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # Limits the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
