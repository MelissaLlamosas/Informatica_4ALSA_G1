import pygame          # Importa la libreria Pygame per creare giochi
import random          # Serve per scegliere colori casuali per i blocchi
 
# Inizializza Pygame
pygame.init()
 
# --- Costanti di gioco ---
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
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Breakout Pygame")      
clock = pygame.time.Clock()                        
font = pygame.font.SysFont("Arial", 24)            
 
# --- Crea blocchi colorati ---
colors = [(192, 222, 234), (252, 186, 205), (208, 193, 251), (249, 181, 99), (196, 242, 240), (207, 252, 170)]
 
blocks = []  
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        color = random.choice(colors)
        blocks.append({'rect': rect, 'color': color, 'hits': 2})  # TODO: i blocchi ora richiedono 2 colpi per rompersi
 
# --- Crea paddle ---
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 6
 
# --- Crea pallina ---
ball = pygame.Rect(paddle.centerx, paddle.top - BALL_RADIUS*2, BALL_RADIUS*2, BALL_RADIUS*2)
ball_dx = 4      
ball_dy = -4     
ball_active = False  
 
# --- Punteggio ---
score = 0
 
# --- Funzione per disegnare i blocchi ---
def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, block['color'], block['rect'])       
        pygame.draw.rect(screen, (0, 0, 0), block['rect'], 1)          

 
# --- Loop principale ---
running = True
while running:
    clock.tick(FPS)                        
    screen.fill(WHITE)                     
 
    # --- Eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False               
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not ball_active:           
                ball_active = True
 
    # --- Movimento paddle ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
        if not ball_active:
            ball.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed
        if not ball_active:
            ball.x += paddle_speed
 
    # --- Movimento pallina ---
    if ball_active:
        ball.x += ball_dx
        ball.y += ball_dy
 
        # --- Rimbalzi ---
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_dx *= -1
        if ball.top <= 0:
            ball_dy *= -1

        # --- TODO: GAME OVER se la pallina cade ---
        if ball.bottom >= HEIGHT:
            # TODO: mostra messaggio "GAME OVER"
            pass
 
        # --- Collisione con paddle ---
        if ball.colliderect(paddle):
            ball_dy *= -1
            offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH / 2)
            ball_dx = BALL_RADIUS * offset * 1.5

 
    # --- Disegna ---
    draw_blocks()                                
    pygame.draw.rect(screen, (0, 0, 0), paddle)   
    pygame.draw.circle(screen, PINK, ball.center, BALL_RADIUS)  
 
    # --- Mostra punteggio ---
    score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, HEIGHT - 30))
 
    # --- TODO: Vittoria ---
    if not blocks:
        # TODO: mostra messaggio "Hai Vinto!"
        pass
 
    pygame.display.flip()
 
# --- Chiude il gioco ---
pygame.quit()
