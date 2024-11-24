import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento de una imagen con flechas")

# Cargar la imagen y asignarla a una variable
# Cambia "ruta_de_tu_imagen.png" por la ruta de la imagen en tu PC
imagen = pygame.image.load('brian.png')

# Opcional: Escalar la imagen para que tenga un tamaño específico (ejemplo 50x50)
imagen = pygame.transform.scale(imagen, (50, 50))

# Posición inicial de la imagen
x, y = 100, 100
velocidad = 1  # Velocidad de movimiento

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Obtener las teclas presionadas
    teclas = pygame.key.get_pressed()
    
    # Mover la imagen con las flechas
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    
    # Rellenar la pantalla de color blanco
    pantalla.fill((255, 255, 255))
    
    # Dibujar la imagen en la nueva posición
    pantalla.blit(imagen, (x, y))
    
    # Actualizar la pantalla
    pygame.display.flip()
