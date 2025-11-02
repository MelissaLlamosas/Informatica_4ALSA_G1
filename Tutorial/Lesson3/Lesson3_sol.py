import pygame
import random

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

# --- Crea il paddle (barra controllata dal giocatore) ---
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 6

# --- Crea la pallina sopra il paddle ---
ball = pygame.Rect(paddle.centerx, paddle.top - BALL_RADIUS * 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx = 4
ball_dy = -4
ball_active = False

# --- Loop principale del gioco ---
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # --- Gestione eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movimento del paddle con frecce sinistra e destra ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
        if not ball_active:
            ball.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed
        if not ball_active:
            ball.x += paddle_speed

    # --- Challenge (facoltativo): cambia velocità con tasti A e D ---
    if keys[pygame.K_a]:
        paddle_speed = max(1, pad_
