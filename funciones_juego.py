import pygame
import json

def dividir_lista(lista):
    '''Divide una lista en sub listas '''
    preguntas = []
    opcion_a = []
    opcion_b = []
    opcion_c = []
    respuestas_correctas = []
    for datos in lista:
        preguntas.append(datos['pregunta'])
        opcion_a.append(datos['a'])
        opcion_b.append(datos['b'])
        opcion_c.append(datos['c'])
        respuestas_correctas.append(datos['correcta'])
    return preguntas, opcion_a, opcion_b, opcion_c, respuestas_correctas

def pantalla_inicio(screen, font):
    '''Recibe por parametros la pantalla y tipo de funte. Pantalla de incio. Retorna los botones JUGAR, PREGUNTAR Y SALIR '''
    nombre = "PREGUNTADOS"
    icono = pygame.image.load("icono_preguntados.webp")
    logo = pygame.image.load("logo_inicio.png")
    logo = pygame.transform.scale(logo, (407,180))
    pygame.display.set_caption(nombre)
    pygame.display.set_icon(icono)
    screen.fill((255, 230, 235))
    screen.blit(logo, (70,50))

    jugar = pygame.Rect(215, 235, 140, 50)
    top_puntaje = pygame.Rect(215, 315, 140, 50)
    salir = pygame.Rect(215, 395, 140, 50)
    text_juego = font.render("JUGAR", True, (60, 60, 60))
    text_top_puntaje = font.render("PUNTAJES", True, (60, 60, 60))
    text_salir = font.render("SALIR", True, (60, 60, 60))
    
    #sombra de botones
    shadow_offset = (5, 5)
    shadow_color = (60, 60, 60)
    pygame.draw.rect(screen, shadow_color, (jugar.left + shadow_offset[0], jugar.top + shadow_offset[1], jugar.width, jugar.height), border_radius=15)
    pygame.draw.rect(screen, shadow_color, (top_puntaje.left + shadow_offset[0], top_puntaje.top + shadow_offset[1], top_puntaje.width, top_puntaje.height), border_radius=15)
    pygame.draw.rect(screen, shadow_color, (salir.left + shadow_offset[0], salir.top + shadow_offset[1], salir.width, salir.height), border_radius=15)

    #botones jugar, puntaje y salir
    pygame.draw.rect(screen, (255, 255, 255), jugar, border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), top_puntaje, border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), salir, border_radius=15)
    screen.blit(text_juego, (253, 250))
    screen.blit(text_top_puntaje, (240, 330))
    screen.blit(text_salir, (257, 411))
    return jugar, top_puntaje, salir

#Sonido de pantalla incial
def iniciar_musica():
    '''Inicia la musica'''
    pygame.mixer.music.load("Y2meta.app - sonido de entrada 1 de Preguntados (128 kbps).mp3")
    pygame.mixer.music.play(-1)

#Detener sonido
def detener_musica():
    '''Detine la musica''' 
    pygame.mixer.music.stop() 

def pantalla_puntajes(screen, font, lista_puntaje):
    '''Recibe por parametros la pantalla, el tipo de letra y la lista. Pantalla de puntajes. Retorna los botones de apagar sonido y de volver hacia atras'''
    nombre = "PREGUNTADOS"
    icono = pygame.image.load("icono_preguntados.webp")
    pygame.display.set_caption(nombre)
    pygame.display.set_icon(icono)
    screen.fill((255, 230, 235))
    personajes = pygame.image.load("personajes.png")
    personajes = pygame.transform.scale(personajes, (400,250))
    screen.blit(personajes, (90,5))

    mejores_puntajes = pygame.Rect(168, 248, 220, 50)
    text_mejores_puntajes = font.render("MEJORES PUNTAJES", True, (60, 60, 60))
    shadow_offset = (5, 5)
    shadow_color = (60, 60, 60)
    pygame.draw.rect(screen, shadow_color, (mejores_puntajes.left + shadow_offset[0], mejores_puntajes.top + shadow_offset[1], mejores_puntajes.width, mejores_puntajes.height), border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), mejores_puntajes, border_radius=15)
    screen.blit(text_mejores_puntajes, (198, 263))

    flecha_volver = pygame.image.load("flecha.png")
    flecha_volver = pygame.transform.scale(flecha_volver, (60, 60))
    flecha_volver_rect = pygame.Rect(10,5,60,60)
    apagar_musica = pygame.image.load("sonido.png")
    apagar_musica = pygame.transform.scale(apagar_musica, (50, 50))
    apagar_musica_rect = pygame.Rect(502,10,50,50)
    screen.blit(flecha_volver, (10,5))
    screen.blit(apagar_musica, (502,10))

    for i in range(3):
        if i < len(lista_puntaje):
            puntajes = lista_puntaje[i]
            texto = font.render(f"{i + 1}. {puntajes['nombre']}: {puntajes['puntaje']} puntos", True, (60, 60, 60))
            screen.blit(texto, (190, 330 + i * 40))

    return flecha_volver_rect, apagar_musica_rect

def pantalla_nombre(screen, font, nombre_usuario):
    '''Recibe por parametros la pantalla, el tipo de fuente y el nombre ingresado. Pantalla de ingresar nombre.'''
    nombre = "PREGUNTADOS"
    icono = pygame.image.load("icono_preguntados.webp")
    logo = pygame.image.load("logo_inicio.png")
    logo = pygame.transform.scale(logo, (407,180))
    pygame.display.set_caption(nombre)
    pygame.display.set_icon(icono)
    screen.fill((255, 230, 235))
    screen.blit(logo, (70,50))

    input_box = pygame.Rect(140, 320, 300, 50)
    fondo = pygame.Rect(140, 228, 300, 50)
    input_prompt = font.render("INGRESA TU NOMBRE:", True, (60, 60, 60))

    shadow_offset = (5, 5)
    shadow_color = (60, 60, 60)
    pygame.draw.rect(screen, shadow_color, (fondo.left + shadow_offset[0], fondo.top + shadow_offset[1], fondo.width, fondo.height), border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), fondo, border_radius=15)
    screen.blit(input_prompt, (215, 245))

    pygame.draw.rect(screen, (60, 60, 60), input_box, 2)
    nombre_surface = font.render(nombre_usuario, True, (60, 60, 60))
    screen.blit(nombre_surface, (input_box.x + 5, input_box.y + 15))

def pantalla_juego(screen, font, puntos_totales, nombre_usuario):
    '''Recibe por parametros la pantalla, el tipo de fuente, los puntos totales y el nombre del usuario. Pantalla del juego. '''
    nombre = "PREGUNTADOS"
    icono = pygame.image.load("icono_preguntados.webp")
    logo = pygame.image.load("icono_preguntados.webp")
    logo = pygame.transform.scale(logo, (150,150))
    pygame.display.set_caption(nombre)
    pygame.display.set_icon(icono)
    score = font.render("SCORE:", True, (70, 70, 70))
    puntos = font.render(str(puntos_totales), True, (70, 70, 70))
    screen.fill((255, 230, 235))
    screen.blit(logo, (12,12))
    screen.blit(score, (311, 100))
    screen.blit(puntos, (376, 100))
    nombre_text = font.render(nombre_usuario, True, (70, 70, 70))
    screen.blit(nombre_text, (311, 130))

#botones de pregunta y reiniciar (pantalla juego)
def botones(screen, font):
    '''Recibe por parametros la pantalla y el tipo de fuente. Retorna los botones de pregunta y reiniciar'''
    pregunta = pygame.Rect (303, 15, 120, 50)
    reiniciar = pygame.Rect (234, 454, 120, 50)
    text_pregunta = font.render("PREGUNTA", True, (255, 255, 255))
    text_reiniciar = font.render("REINICIAR", True, (255, 255, 255))
    pygame.draw.rect(screen, (255, 105, 170), pregunta, border_radius=15)
    pygame.draw.rect(screen, (255, 105, 170), reiniciar, border_radius=15)
    screen.blit(text_pregunta, (318, 30))
    screen.blit(text_reiniciar, (250, 470))
    return pregunta, reiniciar

#Botones de preguntas y respuestas (pantalla juego)
def preguntas_respuestas(screen, font, preguntas, opcion_a, opcion_b, opcion_c, pregunta_numero, opcion_a_correcta, opcion_b_correcta, opcion_c_correcta):
    '''Recibe por parametros la pantalla, el tipo de fuente, las preguntas con sus opciones. Retorna los botones de las respuestas. Pantalla del juego'''
    if pregunta_numero < len(preguntas):
        text_preguntas = font.render(preguntas[pregunta_numero], True, (0, 0, 0))

        respuesta_a = pygame.Rect(50, 270, 190, 50)
        respuesta_b = pygame.Rect(330, 270, 190, 50)
        respuesta_c = pygame.Rect(200, 355, 190, 50)

        text_a = font.render(opcion_a[pregunta_numero], True, (60, 60, 60))
        text_b = font.render(opcion_b[pregunta_numero], True, (60, 60, 60))
        text_c = font.render(opcion_c[pregunta_numero], True, (60, 60, 60))

        shadow_offset = (5, 5)
        shadow_color = (60, 60, 60)
        pygame.draw.rect(screen, shadow_color, (respuesta_a.left + shadow_offset[0], respuesta_a.top + shadow_offset[1], respuesta_a.width, respuesta_a.height), border_radius=15)
        pygame.draw.rect(screen, shadow_color, (respuesta_b.left + shadow_offset[0], respuesta_b.top + shadow_offset[1], respuesta_b.width, respuesta_b.height), border_radius=15)
        pygame.draw.rect(screen, shadow_color, (respuesta_c.left + shadow_offset[0], respuesta_c.top + shadow_offset[1], respuesta_c.width, respuesta_c.height), border_radius=15)

        color_a = (255, 255, 255)
        color_b = (255, 255, 255)
        color_c = (255, 255, 255)

        if opcion_a_correcta == True:
            color_a = (49, 204, 35)
            opcion_a_correcta = None
        elif opcion_a_correcta == False:
            respuesta_a = pygame.Rect(0, 0, 0, 0)

        if opcion_b_correcta == True:
            color_b = (49, 204, 35)
            opcion_b_correcta = None
        elif opcion_b_correcta == False:
            respuesta_b = pygame.Rect(0, 0, 0, 0)

        if opcion_c_correcta == True:
            color_c = (49, 204, 35)
            opcion_c_correcta = None
        elif opcion_c_correcta == False:
            respuesta_c = pygame.Rect(0, 0, 0, 0)
        
        pygame.draw.rect(screen, color_a, respuesta_a, border_radius=15)
        pygame.draw.rect(screen, color_b, respuesta_b, border_radius=15)
        pygame.draw.rect(screen, color_c, respuesta_c, border_radius=15)

        screen.blit(text_preguntas, (6, 212))
        screen.blit(text_a, (60, 286))
        screen.blit(text_b, (340, 286))
        screen.blit(text_c, (210, 375))
        return respuesta_a, respuesta_b, respuesta_c

def pantalla_final (screen, font, puntos_totales):
    '''Recibe por parametros la pantalla, el tipo de fuente y los puntos totales. Pantalla final. Retorna el boton de ver puntajes finales'''
    screen.fill((255, 230, 235))
    nombre = "PREGUNTADOS"
    icono = pygame.image.load("icono_preguntados.webp")
    logo = pygame.image.load("logo_inicio.png")
    logo = pygame.transform.scale(logo, (407,180))
    pygame.display.set_caption(nombre)
    pygame.display.set_icon(icono)
    screen.fill((255, 230, 235))
    screen.blit(logo, (70,50))
    text_final = font.render("JUEGO FINALIZADO!", True, (60, 60, 60))
    text_puntos_finales = font.render (f" PUNTUACION: {puntos_totales}", True, (60, 60, 60))
    screen.blit(text_final, (205, 250))
    screen.blit(text_puntos_finales,(205, 300))

    ver_puntajes_finales = pygame.Rect(160, 360, 245, 50)
    text_ver_puntajes = font.render("VER MEJORES PUNTAJES", True, (60, 60, 60))
    shadow_offset = (5, 5)
    shadow_color = (60, 60, 60)
    pygame.draw.rect(screen, shadow_color, (ver_puntajes_finales.left + shadow_offset[0], ver_puntajes_finales.top + shadow_offset[1], ver_puntajes_finales.width, ver_puntajes_finales.height), border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), ver_puntajes_finales, border_radius=15)
    screen.blit(text_ver_puntajes, (180, 375))
    return ver_puntajes_finales

#Respuesta correcta suma puntos y pasa a la siguiente pregunta.Respuesta incorrecta tiene 2 intentos y luego pasa a la siguiente pregunta.
def respuesta_puntaje(respuesta_correcta, opcion, pregunta_numero, intento ):
    '''Recibe por parametros la respuesta correcta, las opciones y la cantidad de intentos. Pantalla del juego. Retorna los puntos totales, el numero de pregunta, los intentos y si la respuesta fue correcta o incorrecta'''
    puntos_totales = 0
    estado_respuesta = None
    if respuesta_correcta == opcion:
        musica_correcto()
        puntos_totales += 10
        intento = 0
        estado_respuesta = True
    else:
        puntos_totales += 0
        musica_incorrecto()
        estado_respuesta = False
        intento += 1
        if intento >= 2:
            intento = 0
            pregunta_numero += 1
            estado_respuesta = None
    return puntos_totales, pregunta_numero, intento, estado_respuesta

#sonido de respuesta correcta
def musica_correcto():
    '''Sonido de respuesta correcta'''
    respuesta_correcta = pygame.mixer.Sound("Y2meta.app - Sonido de correcto de Preguntados (128 kbps).mp3 ")
    respuesta_correcta.play()

#sonido de respuesta incorrecta
def musica_incorrecto():
    '''Sonido de respuesta incorrecta'''
    respuesta_incorrecta = pygame.mixer.Sound("Y2meta.app - Sonido de incorrecto de Preguntados (128 kbps).mp3")
    respuesta_incorrecta.play()

def listar_puntajes(nombre_usuario, puntos_totales, lista_puntaje):
    '''recibe por parametros el nombre del usuario, los puntos totales obtenidos por el usuario y la lista de diccionarios. Agrega un nuevo puntaje a la lista de puntajes.'''
    lista_puntaje.append({'nombre': nombre_usuario, 'puntaje': puntos_totales})

def guardar_puntajes(path: str, lista_puntaje, nombre_usuario, puntos_totales):
    '''Recibe por parametros la ruta del archivo donde se guardarán los puntajes, la lista de diccionarios con los puntajes previos, el nombre del usuario y los puntos totales obtenidos por el usuario. Agrega un nuevo puntaje a la lista de puntajes.'''
    lista_puntaje.append({'nombre': nombre_usuario, 'puntaje': puntos_totales})
    with open (path, 'w') as archivo:
        json.dump(lista_puntaje, archivo, indent = 4)

def cargar_puntajes(path: str, indicador = "des"):
    '''Recibe por parametros path: Ruta del archivo desde donde se cargarán los puntajes y el indicador: Indica si los puntajes deben ordenarse de forma descendente. Carga y ordena los puntajes desde un archivo JSON. Retorna la lista de los tres mejores puntajes, ordenados según el indicador'''
    with open(path, 'r') as archivo:
        lista_puntaje = json.load(archivo)
    if indicador == "des":
        for i in range(len(lista_puntaje)-1): 
            for j in range(i+1, len(lista_puntaje)):
                if  lista_puntaje[i]['puntaje'] < lista_puntaje[j]['puntaje']:
                    aux = lista_puntaje[i]
                    lista_puntaje[i] = lista_puntaje[j]
                    lista_puntaje[j] = aux
    # Retornar los tres primeros puntajes
    return lista_puntaje[:3]