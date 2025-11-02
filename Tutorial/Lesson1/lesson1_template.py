# --- Lezione 1: Impostare la finestra di gioco e le costanti ---

import pygame  # TODO: importa la libreria pygame
import random  # TODO: importa la libreria random per i colori casuali

# --- Inizializzazione di Pygame ---
pygame.init()  # TODO: inizializza pygame

# --- Costanti di gioco ---
# TODO: definisci la larghezza e altezza della finestra
# TODO: definisci il numero di righe e colonne di blocchi
# TODO: calcola la larghezza e l’altezza di ogni blocco in base alla finestra
# TODO: imposta le dimensioni del paddle e della pallina
# TODO: definisci i colori principali (es. bianco e rosa)
# TODO: imposta i frame per secondo (FPS)

# Esempio (da completare o correggere):
WIDTH, HEIGHT = 480, 640
BLOCK_ROWS = 5
BLOCK_COLS = 8
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 8
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
FPS = 60

# --- Imposta la finestra ---
# TODO: crea la finestra di gioco con pygame.display.set_mode()
# TODO: imposta il titolo della finestra
# TODO: crea un orologio per controllare gli FPS
# TODO: imposta un font per il testo

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Pygame")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# --- Test iniziale ---
# TODO: crea un semplice ciclo principale in cui lo sfondo è bianco
# (Serve solo a verificare che la finestra funzioni)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
