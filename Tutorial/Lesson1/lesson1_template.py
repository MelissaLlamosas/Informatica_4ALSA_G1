# --- Lezione 1: Impostare la finestra di gioco e le costanti ---

# TODO: importa la libreria pygame
# TODO: importa la libreria random per i colori casuali

# --- Inizializzazione di Pygame ---
pygame.init()

# --- Costanti di gioco ---

# TODO: definisci la larghezza e altezza della finestra

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

pygame.display.set_caption("Breakout Pygame")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

# --- Test iniziale ---

# TODO: crea un semplice ciclo principale in cui lo sfondo è bianco


pygame.quit()
