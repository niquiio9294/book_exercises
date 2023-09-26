import pygame
import settings
import ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game, settings and screen object.
    pygame.init()      # inicializa la configuracion de pygame para que funcione correctamente.
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # con esta funcion creamos la pantalla 
            # y la definimos con un tuple para que no se pueda modificar las dimensiones de la misma
    pygame.display.set_caption("Alien Invasion")  # esta funcion es la que muestra la surface creada
# una surface son todos los objetos que aparecen en la pantalla como la nave, el alien y la pantalla en si
    
    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets and a group of aliens    
    ship_1 = ship.Ship(screen)
    bullets = Group()      
    aliens = Group()

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship_1, aliens)

    # Start the main loop for the game.
    while True:
        gf.chack_event(ai_settings,screen, stats, play_button, ship_1, aliens, bullets) # verificamos todos los eventos posibles al tocar una tecla.
        if stats.game_active: # las siguientes partes son las que tienen q estar activas solo si el juego esta activo
            ship_1.update()  # hace que la nave se mueva cuando se presiona una tecla.
            gf.update_bullets(ai_settings, screen, ship_1, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship_1, aliens, bullets)
        gf.update_screen(ai_settings,screen,stats, sb, ship_1, aliens, bullets, play_button) #actuliza la pantalla a medida que ocurre un evento.


run_game()