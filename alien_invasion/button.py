import pygame.font  # este modulo permite a pyton escribir textos en la pantalla

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # (fuente, tamaño) al poner None en la fuente, utiliza la que tiene por defecto.

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) # font.render() transforma el msg en una imagen
    # es necesario transformarlo a imagen xq es la forma en que pygame lo puede procesar
        self.msg_image_rect = self.msg_image.get_rect() # aca transformamos la imagen a un rect
        self.msg_image_rect.center = self.rect.center # aca lo centramos.
    
    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)