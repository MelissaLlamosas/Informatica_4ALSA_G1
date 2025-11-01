import pygame

# --- Inizializzazione di Pygame ---
pygame.init()

# --- Costanti di gioco ---
LARGHEZZA, ALTEZZA = 800, 600
COLORE_SFONDO = (0, 0, 0)
COLORE_PADDLE = (255, 255, 255)
COLORE_PALLINA = (255, 0, 0)

# --- Creazione della finestra ---
schermo = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption("Lezione 4 - Rimbalzo della pallina")

# --- Paddle ---
paddle = pygame.Rect(LARGHEZZA // 2 - 60, ALTEZZA - 40, 120, 15)
velocità_paddle = 8

# --- Pallina ---
pallina = pygame.Rect(LARGHEZZA // 2 - 10, ALTEZZA // 2 - 10, 20, 20)
velocità_pallina = [5, -5]

# --- Ciclo principale ---
clock = pygame.time.Clock()
running = True

while running:
    # --- Gestione eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movimento paddle ---
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_LEFT]:
        paddle.x -= velocità_paddle
    if tasti[pygame.K_RIGHT]:
        paddle.x += velocità_paddle

    # --- Limiti schermo paddle ---
    # TODO: limita il movimento del paddle ai bordi della finestra

    # --- Movimento pallina ---
    pallina.x += velocità_pallina[0]
    pallina.y += velocità_pallina[1]

    # --- Rimbalzi sui bordi ---
    # TODO: fai rimbalzare la pallina quando tocca i bordi

    # --- Collisione pallina-paddle ---
    # TODO: verifica collisione e inverti la direzione verticale

    # --- Disegno sulla finestra ---
    schermo.fill(COLORE_SFONDO)
    pygame.draw.rect(schermo, COLORE_PADDLE, paddle)
    pygame.draw.ellipse(schermo, COLORE_PALLINA, pallina)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
