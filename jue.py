import pygame
import sys

pygame.init()

ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("juebo con graficos python", "julio")

negro = (0,0,0)
blanco = pygame.image.load(C:\Users\julio\Desktop\flora\fotos\f0027823.jpg)
                           
blanco = pygame.transform.scale(blanco,(50,50))
x,y = 100,100
velocidad = 5
ancho_cuadrado = 50
alto_cuadrado = 50

reloj = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    
    if x < 0 : x = 0
    if x > ancho - ancho_cuadrado : x = ancho - ancho_cuadrado
    if y < 0 : y = 0
    if y > alto - alto_cuadrado : y = alto_cuadrado
    pantalla.fill(negro)

    pygame.draw.rect(pantalla,blanco,(x,y,ancho_cuadrado,alto_cuadrado))
    pygame.display.flip()

    reloj.tick(30)
