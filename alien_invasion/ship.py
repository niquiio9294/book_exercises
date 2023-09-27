import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class to created a Ship."""

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen  # aca definimos la pantalla en la que se colocara la nave
        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")  # aca cargamos la imagen
        self.rect = self.image.get_rect()  # convierte la imagen en un rectangulo, esto nos permite usar coordenadas (x,y) para posicionarlo.
        self.screen_rect = screen.get_rect() #hacemos lo mismo con la pantalla

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movment Flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movment flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:    # mientras que moving_right sea TRUE (osea mientras este presionada la tecla) se va a mover la nave.
            self.rect.centerx += 1.5 # lo cual nos permite un movimiento continuo
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 2
        

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # esta funcion dibuja la imagen en la pantalla en la posicion definida.

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx