import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a Bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0,0) and then set correct position.
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
#como no usamos una imagen, creamos la bala con self.rect. este nos pide (cordenada x, cordenada y,ancho, alto)
# ahora hacemos q la posicion de la bala sea la misma que la de la nave
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)  # esto lo hacemos para tener un mejor maejo en el ajuste de la velocidad
# ahora le asignamos el valor del color y de la velocidad
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of th bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
# usamos draw.rect() para dibujar las balas.
        pygame.draw.rect(self.screen, self.color, self.rect)