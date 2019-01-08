import pygame
import random

import config


class Scene:
    def __init__(self):
        pass

    def render(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_event(self, event):
        raise NotImplementedError


class SpaceShip:
    def __init__(self):

        self._image = pygame.image.load('spaceship.png')
        self._direction = 0
        self._position = pygame.math.Vector2()
        self._trajectory = pygame.math.Vector2((0, 0))
        self._rect = None
        self._firing_laser = False
        self._laser_sound = pygame.mixer.Sound('laser.wav')

    def draw(self, surface):
        image = pygame.transform.rotate(self._image, self._direction)
        self._rect = surface.blit(image, self._position)

        if self._firing_laser:

            offset = pygame.math.Vector2()
            offset.from_polar((20, -self._direction))
            start = pygame.math.Vector2(self._rect.center) + offset

            offset = pygame.math.Vector2()
            offset.from_polar((300, -self._direction))
            end = start + offset

            pygame.draw.line(surface, (255, 255, 255), start, end, 1)

            self._firing_laser = False

    def centre(self, surface):
        self._position.x = (surface.get_width() - self._image.get_width()) / 2
        self._position.y = (surface.get_height() - self._image.get_height()) / 2

    def left_thrust(self):
        self._direction = (self._direction + config.ROTATIONAL_THRUST) % 360

    def right_thrust(self):
        self._direction = (self._direction - config.ROTATIONAL_THRUST) % 360

    def shoot_laser(self):
        self._laser_sound.play()
        self._firing_laser = True

    def shoot_cannon(self):
        pass

    def update(self):
            self._position += self._trajectory

            if self._position.x < 0:
                self._position.x = config.SCREEN_WIDTH

            elif self._position.x > config.SCREEN_WIDTH:
                self._position.x = 0

            if self._position.y < 0:
                self._position.y = config.SCREEN_HEIGHT

            elif self._position.y > config.SCREEN_HEIGHT:
                self._position.y = 0

    def forward_thrust(self):
        vec = pygame.math.Vector2()
        vec.from_polar((config.THRUST, -self._direction))
        self._trajectory += vec

    def reverse_thrust(self):
        vec = pygame.math.Vector2()
        vec.from_polar((config.THRUST, -self._direction))
        self._trajectory -= vec


class Level1Scene(Scene):
    def __init__(self, screen, *args, **kwargs):

        self._planet = self._image = pygame.image.load('jupiter.png')
        self._planet_rect = self._planet.get_rect(center=(screen.get_width()/2, screen.get_height()/2))

        self._ship = SpaceShip()
        self._ship.centre(screen)

        self._stars = [
            (random.randint(0, config.SCREEN_WIDTH), random.randint(0, config.SCREEN_HEIGHT)) for _ in range(200)]

    def draw(self, surface):

        surface.fill(config.COLOUR_BACKGROUND)

        for star in self._stars:
            surface.set_at(star, (255, 255, 255))

        surface.blit(self._planet, self._planet_rect)

        self._ship.draw(surface)

    def update(self):
        self._ship.update()

    def cleanup(self):
        pass

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self._ship.forward_thrust()
            elif event.key == pygame.K_DOWN:
                self._ship.reverse_thrust()
            elif event.key == pygame.K_RIGHT:
                self._ship.right_thrust()
            elif event.key == pygame.K_LEFT:
                self._ship.left_thrust()
            elif event.key == pygame.K_SPACE:
                self._ship.shoot_laser()
