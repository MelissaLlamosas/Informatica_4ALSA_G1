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
 
# --- Imposta la finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Crea finestra
pygame.display.set_caption("Breakout Pygame")      # Titolo finestra
clock = pygame.time.Clock()                        # Orologio per FPS
font = pygame.font.SysFont("Arial", 24)            # Font per testo
 
# --- Crea blocchi colorati ---
colors = [(192, 222, 234), (252, 186, 205), (208, 193, 251),
          (249, 181, 99), (196, 242, 240), (207, 252, 170)]   # Colori possibili
 
blocks = []  # Lista per salvare tutti i blocchi
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        color = random.choice(colors)
        blocks.append({'rect': rect, 'color': color})  # Ogni blocco è un dizionario con rettangolo e colore
 
# --- Crea paddle (rettangolo controllabile dal giocatore) ---
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 6  # Velocità di movimento del paddle
 
# --- Crea pallina (appoggiata sopra il paddle) ---
ball = pygame.Rect(paddle.centerx, paddle.top - BALL_RADIUS*2, BALL_RADIUS*2, BALL_RADIUS*2)
ball_dx = 4      # Direzione orizzontale
ball_dy = -4     # Direzione verticale
ball_active = False  # La pallina parte ferma, finché non premi spazio
 
# --- Punteggio iniziale ---
score = 0
 
# --- Funzione per disegnare tutti i blocchi ---
def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, block['color'], block['rect'])       # Disegna blocco colorato
        pygame.draw.rect(screen, (0, 0, 0), block['rect'], 1)          # Bordo nero per ogni blocco
 
# --- Loop principale del gioco ---
running = True
while running:
    clock.tick(FPS)                        # Mantiene il gioco a 60 FPS
    screen.fill(WHITE)                     # Riempie lo sfondo di bianco
 
    # --- Gestione eventi (es. tasti premuti) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False               # Se clicchi sulla X, esci dal gioco
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not ball_active:           # Se premi spazio, lancia la pallina
                ball_active = True
 
    # --- Movimento del paddle (frecce sinistra/destra) ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
        if not ball_active:  # Se la pallina è ferma, la sposti insieme al paddle
            ball.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed
        if not ball_active:
            ball.x += paddle_speed
 
    # --- Movimento della pallina ---
    if ball_active:
        ball.x += ball_dx
        ball.y += ball_dy
 
        # Rimbalzi sui bordi
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_dx *= -1
        if ball.top <= 0:
            ball_dy *= -1
        if ball.bottom >= HEIGHT:
            ball_active = False  # Se la pallina cade, reset
            # Rimetti la pallina sopra il paddle
            ball.x = paddle.centerx - BALL_RADIUS
            ball.y = paddle.top - BALL_RADIUS*2
 
        # Collisione con paddle
        if ball.colliderect(paddle):
            ball_dy *= -1
            # Cambia la direzione orizzontale in base a dove colpisce il paddle
            offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH / 2)
            ball_dx = BALL_RADIUS * offset * 1.5
 
        # Collisione con blocchi
        for block in blocks[:]:
            if ball.colliderect(block['rect']):
                blocks.remove(block)      # Rimuovi blocco colpito
                ball_dy *= -1             # Rimbalza
                score += 1                # Aumenta il punteggio
                break
 
    # --- Disegna tutto ---
    draw_blocks()                                # Blocchi colorati
    pygame.draw.rect(screen, (0, 0, 0), paddle)   # Paddle (nero)
    pygame.draw.circle(screen, PINK, ball.center, BALL_RADIUS)  # Pallina rosa
 
    # --- Mostra punteggio ---
    score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, HEIGHT - 30))
 
    # --- Vittoria se tutti i blocchi sono distrutti ---
    if not blocks:
        win_text = font.render("Hai Vinto!", True, (0, 128, 0))
        screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
 
    pygame.display.flip()  # Aggiorna la finestra
 
# --- Chiude il gioco ---
pygame.quit()
 
