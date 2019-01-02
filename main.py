import pygame

import config
from scenes import Level1Scene


def game_loop():

    current_scene = Level1Scene(screen)

    while True:
        if pygame.event.get(pygame.QUIT):
            current_scene.cleanup()
            break

        for event in pygame.event.get():
            new_scene = current_scene.handle_event(event)

            if new_scene:
                current_scene = new_scene

        current_scene.draw(screen)
        current_scene.update()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pygame.init()
    pygame.key.set_repeat(10, 10)
    config.init_fonts()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

    game_loop()

    pygame.quit()
