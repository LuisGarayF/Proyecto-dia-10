import pygame
import random
import sys
import math

# Inicializar pygame
pygame.init()

# Configurar tamaño de pantalla

pantalla = pygame.display.set_mode((800,600))

# Titulo de la ventana
pygame.display.set_caption('Alien Invaders')
# Icono de la ventana
icono = pygame.image.load('img/ufo_ico.png').convert()
pygame.display.set_icon(icono)
fondo = pygame.image.load('img/fondo.jpg').convert()

# Variables Jugador
img_jugador = pygame.image.load('img/cohete-espacial.png')

# La pantalla es de 800 x 600, 800/2 = 400 - 32 = 368 (Los 32 corresponden a la mitad del ancho de la imagen de la nave)
jugador_x = 368 
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

# Variables Enemigo con un ciclo con 8 enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('img/ufo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,300))
    enemigo_x_cambio.append(0.4)
    enemigo_y_cambio.append(50) 

# Variables Bala
img_bala = pygame.image.load('img/bala.png')
bala_x = 0
bala_y = 500
bala_y_cambio = 3
bala_visible = False
img_explosion = pygame.image.load('img/explosion.png')

# Variable puntaje
puntaje = 0

# Funcion jugador
def jugador(x, y):
    # blit arroja al juador en la pantalla
    pantalla.blit(img_jugador,(x, y))

# Funcion enemigo
def enemigo(x, y, ene):
    # blit arroja al juador en la pantalla
    pantalla.blit(img_enemigo[ene],(x, y))

# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x + 16,  y + 10))
    
# Función detectar colisiones
def colisiones(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2)+ math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else: 
        return False



# Ciclo de juego
en_ejecucion = True
while en_ejecucion:
    # Pinta la pantalla formato rgb
    #pantalla.fill((205,144,228))
    pantalla.blit(fondo,(0,0))
    
    # Evento cerrar ventana
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            en_ejecucion = False
            pygame.quit()
            sys.exit()
            
        # Cilo para eventos de teclado
        
        # Al presionar las teclas
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.4
            elif evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.4
            
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)
                
        # Evento al soltar las teclas
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modifica ubicacion jugador
    jugador_x += jugador_x_cambio
    
    # Limites pantalla
    
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
        
    # Modifica ubicacion enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]
      # Limites pantalla
    
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.4
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.4
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # LLamar a la funcion colisiones
        colision = colisiones(enemigo_x[e],enemigo_y[e], bala_x,bala_y)
        
        if colision:
            pantalla.blit(img_explosion, (enemigo_x[e],enemigo_y[e]))# no la muestra
            bala_y = 500
            bala_visible = False
            puntaje += 1
        
        #print(puntaje)
        
        enemigo_x[e] = random.randint(0,736)
        enemigo_y[e] = random.randint(50,300)

        # Llamamos a la funcion enemigo
        enemigo(enemigo_x[e], enemigo_y[e], e)
        
    # Movimiento bala
    if bala_y <=-64:
        bala_y = 500
        bala_visible = False
        
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio
    
    
        
    # Llamamos a la funcion jugador        
    jugador(jugador_x, jugador_y)     
  
    
    
       
    # Actualiza la pantalla
    pygame.display.update()
