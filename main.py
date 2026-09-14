import pygame

from constants import(
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialises pygame
    pygame.init()

    # Sets the pygame.display size from the screen width and height constants
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Gets the games state and logs it
        log_state()

        # Processes events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Sets the screen to solid black, then updates it
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
