import pygame          # Importa la libreria Pygame per creare giochi
import random          # Serve per scegliere colori casuali per i blocchi

# Inizializza Pygame
pygame.init()

# --- Costanti di gioco ---
WIDTH, HEIGHT = 480, 640                      # Dimensioni finestra di gioco
BLOCK_ROWS = 5                                # Numero di righe di blocchi
BLOCK_COLS = 8                                # Numero di colonne di blocchi
BLOCK_WIDTH = WIDTH // BLOCK_COLS             # Larghezza singolo blocco
BLOCK_HEIGHT = 30                             # Altezza blocco
PADDLE_WIDTH = 80                             # Larghezza del paddle
PADDLE_HEIGHT = 15                            # Altezza del paddle
BALL_RADIUS = 8                               # Raggio della pallina
WHITE = (255, 255, 255)                       # Colore bianco (sfondo)
PINK = (255, 105, 180)                        # Colore rosa (pallina)
FPS = 60                                      # Frame per secondo

# --- Imposta finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Pygame")
clock = pygame.time.Clock()

# --- Loop principale ---
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempi la finestra di bianco
    screen.fill(WHITE)

    # Aggiorna la finestra
    pygame.display.flip()

# Chiudi il gioco
pygame.quit()
