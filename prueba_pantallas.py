import pygame

def pantalla_final (screen, font):
    screen.fill((255, 230, 235))
    nombre = "PREGUNTADOS"
    icono = pygame.image.load("JUEGO_PARCIAL/icono_preguntados.webp")
    logo = pygame.image.load("JUEGO_PARCIAL/logo_inicio.png")
    logo = pygame.transform.scale(logo, (407,180))
    pygame.display.set_caption(nombre)
    pygame.display.set_icon(icono)
    screen.fill((255, 230, 235))
    screen.blit(logo, (70,50))
    text_final = font.render("JUEGO FINALIZADO!", True, (60, 60, 60))
    text_puntos_finales = font.render ("PUNTUACION:", True, (60, 60, 60))
    screen.blit(text_final, (217, 250))
    screen.blit(text_puntos_finales,(230, 300))
    
    ver_puntajes = pygame.Rect(180, 360, 190, 50)
    text_ver_puntajes = font.render("VER PUNTAJES", True, (60, 60, 60))
    shadow_offset = (5, 5)
    shadow_color = (60, 60, 60)
    pygame.draw.rect(screen, shadow_color, (ver_puntajes.left + shadow_offset[0], ver_puntajes.top + shadow_offset[1], ver_puntajes.width, ver_puntajes.height), border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), ver_puntajes, border_radius=15)
    screen.blit(text_ver_puntajes, (205, 375))

pygame.init()
running = True

font = pygame.font.SysFont("Arial", 14)
screen = pygame.display.set_mode((570, 530))
while running:
    pantalla_final(screen, font,)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}")
        pygame.display.flip()
pygame.quit() 