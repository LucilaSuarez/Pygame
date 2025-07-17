import pygame
from datos import lista
from funciones_juego import *
import json

pygame.init()

#Variables
preguntas, opcion_a, opcion_b, opcion_c, respuestas_correctas = dividir_lista(lista)
font = pygame.font.Font("BowlbyOne-Regular.otf", 14)
screen = pygame.display.set_mode((570, 530))
puntos_totales = 0
pregunta_numero = 0
intento = 0

#Variables para mostrar pantallas
running = True
play = False
ver_puntaje = False
fin_juego = False
musica_encendida = True 

#Variables JSON puntajes
path_puntajes = "C:/Users/lulis/OneDrive/Escritorio/Curso_de_ingreso_PYTHON/Progrmacion1/JUEGO_PARCIAL/puntuaciones.json"
lista_puntaje = cargar_puntajes(path_puntajes)

#Nombre usuario
nombre_usuario = ""
ingreso_usuario = False

#Estado de Respuestas (sin estado)
opcion_a_correcta = None
opcion_b_correcta = None
opcion_c_correcta = None
estado_respuesta = None

iniciar_musica()

while running:
    #todas las pantallas apagadas, se muestra la inicial
    if play == False and ver_puntaje == False and ingreso_usuario == False and fin_juego == False:
        jugar, top_puntaje, salir = pantalla_inicio(screen, font)
    #pantalla de ingresar usuario prendida    
    elif ingreso_usuario:
        pantalla_nombre(screen, font, nombre_usuario)
    #pantalla de juego prendida    
    elif play:
        #si llego al final de las preguntas, guardo el puntaje y el nombre del jugador
        if pregunta_numero >= len(preguntas): 
            fin_juego = True
            guardar_puntajes(path_puntajes, lista_puntaje, nombre_usuario, puntos_totales)
            play = False
        #si no llego al final de las preguntas, pantalla de juego prendida
        else:
            detener_musica()
            pantalla_juego(screen, font, puntos_totales, nombre_usuario)
            pregunta, reiniciar = botones(screen, font)
            respuesta_a, respuesta_b, respuesta_c = preguntas_respuestas(screen, font, preguntas, opcion_a, opcion_b, opcion_c, pregunta_numero, opcion_a_correcta, opcion_b_correcta, opcion_c_correcta)
            #manejo el estado de las respuestas
            if estado_respuesta is None:
                opcion_a_correcta = None
                opcion_b_correcta = None
                opcion_c_correcta = None
            elif estado_respuesta is True:
                # La respuesta fue correcta, actualizar estado cuando sea necesario
                pass
            elif estado_respuesta is False:
                # La respuesta fue incorrecta, actualizar estado cuando sea necesario
                pass
    #pantalla de puntajes prendida
    elif ver_puntaje:
        lista_puntaje = cargar_puntajes(path_puntajes)
        flecha_volver_rect , apagar_musica_rect = pantalla_puntajes(screen, font, lista_puntaje)
    #pantalla de final de juego prendida    
    elif fin_juego:
        ver_puntajes_finales = pantalla_final(screen, font, puntos_totales)
        listar_puntajes(nombre_usuario, puntos_totales, lista_puntaje)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            #obtengo el nombre
            if ingreso_usuario:
                if event.key == pygame.K_RETURN:
                    print(f"Nombre ingresado: {nombre_usuario}") #pruebo si se guardo correctamente el nombre
                    ingreso_usuario = False
                    play = True
                #borra caracteres
                elif event.key == pygame.K_BACKSPACE:
                    nombre_usuario = nombre_usuario[:-1] 
                else:
                    nombre_usuario += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"Mouse down: {event.pos}") #prubo cordendas

            if play == False and ver_puntaje == False and fin_juego == False:
                if jugar.collidepoint(event.pos):
                    ingreso_usuario = True
                elif top_puntaje.collidepoint(event.pos):
                    ver_puntaje = True
                elif salir.collidepoint(event.pos):
                    running = False

            elif play and pregunta_numero < len(preguntas):
                if pregunta.collidepoint(event.pos):
                    print("Apreto pregunta")
                    pregunta_numero += 1
                    intento = 0
                    opcion_a_correcta = None
                    opcion_b_correcta = None
                    opcion_c_correcta = None

                if reiniciar.collidepoint(event.pos):
                    print("Apreto reinciar")
                    pregunta_numero = 0
                    puntos_totales = 0
                    intento = 0
                    opcion_a_correcta = None
                    opcion_b_correcta = None
                    opcion_c_correcta = None

                if respuesta_a.collidepoint(event.pos):
                    puntos, pregunta_numero, intento, estado_respuesta = respuesta_puntaje(respuestas_correctas[pregunta_numero], 'a', pregunta_numero, intento)
                    puntos_totales += puntos 
                    opcion_a_correcta = estado_respuesta

                if respuesta_b.collidepoint(event.pos):
                    puntos, pregunta_numero, intento, estado_respuesta = respuesta_puntaje(respuestas_correctas[pregunta_numero], 'b', pregunta_numero, intento)
                    puntos_totales += puntos
                    opcion_b_correcta = estado_respuesta

                if respuesta_c.collidepoint(event.pos):
                    puntos, pregunta_numero, intento, estado_respuesta = respuesta_puntaje(respuestas_correctas[pregunta_numero], 'c', pregunta_numero, intento)
                    puntos_totales += puntos
                    opcion_c_correcta = estado_respuesta

            elif fin_juego:
                if ver_puntajes_finales.collidepoint(event.pos):
                    ver_puntaje = True
                    fin_juego = False

            elif ver_puntaje:
                if flecha_volver_rect.collidepoint(event.pos):
                    play = False
                    ver_puntaje = False
                    ingreso_usuario = False
                    fin_juego = False
                if apagar_musica_rect.collidepoint(event.pos):
                    if musica_encendida:
                        detener_musica()
                        musica_encendida = False
                    else:
                        iniciar_musica()
                        musica_encendida = True

    pygame.display.flip()
pygame.quit() 