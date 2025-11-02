import pygame          # Importa la libreria Pygame per creare giochi
import random          # Serve più avanti per i colori dei blocchi

# Inizializza Pygame
pygame.init()

# --- Costanti di gioco ---
WIDTH, HEIGHT = 480, 640
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 8
WHITE = (255, 255, 255)
PINK = (255, 105, 180)
FPS = 60

# --- Imposta la finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Pygame")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# --- TODO: Crea il paddle (barra controllata dal giocatore) ---


# --- TODO: Crea la pallina sopra il paddle ---


# --- Loop principale del gioco ---
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # --- Gestione eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- TODO: Movimento del paddle con frecce sinistra e destra ---


    # --- TODO: Challenge (facoltativo): cambia velocità con tasti A e D ---
 

    # --- TODO: Disegna paddle e pallina ---

    pygame.display.flip()

# --- Chiude il gioco ---
pygame.quit()
