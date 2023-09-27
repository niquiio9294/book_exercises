import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship_1, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:  # si la presionada es la flecha/tecla derecha (K_RIGHT), hacemos que se mueva de a 1 a la derecha.
    # Move the ship to the right.
        ship_1.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship_1.moving_left = True
    elif event.key == pygame.K_SPACE:  # cuando se preciona la barra espaciodara crearemos una bala
        fire_bullet(ai_settings, screen, ship_1, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship_1, bullets):
    """Fire a bullet if limit not reach yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship_1) # creamos una nueva bala
        bullets.add(new_bullet) # la bala nueva la agregamos al grupo de balas creado


def check_keyup_events(event, ship_1):
    """Respond to a key releases."""
    if event.key == pygame.K_RIGHT:  # cuando lo detecta, detiene el movimiento.
        ship_1.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship_1.moving_left = False


def chack_event(ai_settings, screen, stats, sb, play_button, ship_1, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():  # con event.get() accedemos a los eventos que detecta pygame
        if event.type == pygame.QUIT:  #pygame.QUIT es el evento de cerrar la ventana de juego. cuando este evento se detecta, acciona la func sys.exit() para que se cierre.
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #KEYDOWN detecta si una tecla fue presionada
            check_keydown_events(event, ai_settings, screen, ship_1, bullets)
        elif event.type == pygame.KEYUP:  # KEYUP detecta cuando se dejo de apretar la flecha.
            check_keyup_events(event, ship_1)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()  # esta func nos da la posicion en (x, y) en la cual se clickeo el mouse
# esa posicion la usamos para saber si coincide con la posicion del boton, ya que si coincide es como si se lo estuviera apretando.            
            check_play_button(ai_settings, screen, stats, sb, play_button, ship_1, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False) # esta fucion le dice a python que esconda el cursor
        # Reset the game statistics.
        stats.reset_stats()  # al resetear hacemos q tengan 3 naves de nuevo
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width # aca obtenemos el espacio disponible que es el ancho de la pantalla menos los margenes (el cual tomamos como 2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width)) # ahora calculamos la cantidad de aliens q entran en la pantalla.
# esto lo hacemos dividiendo el espacio disponible por el alien mas el espacio que lo separa del otro alien (en este caso 2*alien_width)
# lo pasamos a enteros para no crear aliens parciales.
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of row of aliens that fit on the screen."""
    available_space_y =(ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)  # creamos un alien para tener de referencia (este no va a ser parte del grupo)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien) # aca agregamos cada alien creado al grupo de aliens.


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)  # creamos un alien para tener de referencia (este no va a ser parte del grupo)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fileet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_screen(ai_settings, screen, stats, sb, ship_1, aliens, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the sreen during each pass through the loop
    screen.fill(ai_settings.screen_colour) # esta funcion le da color a la pantalla.
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites(): #sprites() devuelve una lista con todas las balas del grupo balas
        bullet.draw_bullet() # entonces hacemos un for para dibujar las balas a medida que se disparan

    ship_1.blitme()  # pegamos la nave en la pantalla.
    aliens.draw(screen)  # con draw() nos permite dibujar cada elemento de un grupo en la poicion definida por rect.
    
    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently draw screen visible.
    pygame.display.flip()  # esta funcion muestra la pantalla dibujada mas reciente
# cuando movemos los elementos del juego, esta func actualizara la patalla constantemente
# lo que creara una ilusion de movimiento de los elementos.


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullets position.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that hace collided.
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
# la funcion groupcollide() nos permite saber si dos rect (o grupo de rects) colisionan
# y si colisionan, se pueden borrar ambos o uno de ellos. En este caso al poner True, True se borran ambos
# si poniamos False, True solo se borra el alien. Y la bala seguiria borrando los aliens a medida q los toca 

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

# ahora vamos a hacer que cuando se eliminen todos los aliens, aparezca otro grupo.
    if len(aliens) == 0:  # chequeo si el grupo de aliens esta en cero (xq los destruimos todos)
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()  # si esta en cero, vacio el grupo de balas que me quedan con la func empty()
        ai_settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)  # y creo una nueva flota de aliens


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1
        # Update scoreboard.
        sb.prep_ships()
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check if any aliens have reach the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Check is the fleet is at an edge,
    and then update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for aliens-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
# la funcion spritecollideany() revisa si un sprite (ship) y un grupo (aliens) colsionan.
# si lo hacen, este metodo detiene el loop.

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()