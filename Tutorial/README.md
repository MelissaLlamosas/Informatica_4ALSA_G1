# Lezione 6: Vittoria, sconfitta e miglioramenti

### Obiettivi della lezione

* Imparare a gestire la **vittoria** e la **sconfitta** nel gioco.
* Aggiungere un **messaggio di vittoria** quando tutti i blocchi sono distrutti.
* **Resettare la pallina** quando cade fuori dallo schermo.
* Introdurre **effetti grafici e sonori** per migliorare l’esperienza di gioco.
* **Challenge**: Blocchi che si muovono lentamente o non si cancellano.

---

## 1. Gestire la sconfitta: quando la pallina cade

Nel nostro gioco, se la pallina cade sotto il bordo inferiore della finestra, dobbiamo fermare il gioco e resettare la pallina sopra il paddle. Questo avviene nel codice con la seguente logica:

```python
if ball.bottom >= HEIGHT:
    ball_active = False  # La pallina non è più attiva
    ball.x = paddle.centerx - BALL_RADIUS  # Reset posizione
    ball.y = paddle.top - BALL_RADIUS*2  # Reset sopra il paddle
```

* Se la pallina supera il bordo inferiore della finestra (`ball.bottom >= HEIGHT`), viene fermata e riportata sopra il paddle.
* La variabile `ball_active` è impostata su `False` per indicare che la pallina non è attiva finché non premiamo di nuovo **spazio**.

---

## 2. Messaggio di vittoria

Quando tutti i blocchi sono distrutti, è il momento di dichiarare la vittoria! Per farlo, possiamo mostrare un testo al centro della finestra. Questo avviene quando la lista `blocks` è vuota:

```python
if not blocks:
    win_text = font.render("Hai Vinto!", True, (0, 128, 0))
    screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2))  # Posiziona il messaggio al centro
    pygame.display.flip()
    pygame.time.wait(2000)  # Mostra il messaggio per 2 secondi
    running = False  # Ferma il gioco
```

* Quando non ci sono più blocchi (`if not blocks`), mostriamo il messaggio "Hai Vinto!" al centro dello schermo.
* Il messaggio rimane visibile per 2 secondi grazie a `pygame.time.wait(2000)`.

---

## 3. Aggiungere effetti grafici (es. suoni, animazioni)

Per rendere il gioco più interessante, possiamo aggiungere effetti grafici o sonori. Ad esempio, quando la pallina colpisce un blocco, possiamo cambiare il colore del blocco o riprodurre un suono.

### Esempio di suono:

Per aggiungere un suono quando un blocco viene distrutto, carica il suono all'inizio del gioco e riproducilo al momento giusto.

```python
# Carica suono di collisione
collision_sound = pygame.mixer.Sound('collisione.wav')

# Riproduci suono quando colpisci un blocco
collision_sound.play()
```

* Usa `pygame.mixer.Sound()` per caricare il file audio.
* Poi chiama `play()` quando si verifica la collisione con un blocco.

---

## 4. Challenge: Blocchi che si muovono lentamente

Un'idea per rendere il gioco più interessante potrebbe essere quella di far muovere alcuni blocchi lentamente. Per farlo, possiamo aggiungere una velocità di movimento ai blocchi, e spostarli ogni ciclo di gioco.

### Codice per far muovere i blocchi:

```python
# Aggiungi una velocità di movimento ai blocchi
block_speed = 1  # Velocità di movimento

for block in blocks:
    block['rect'].y += block_speed  # Muovi i blocchi verso il basso
```

In questo caso, ogni blocco si sposterà di 1 pixel verso il basso ad ogni aggiornamento. Puoi anche aggiungere un'animazione che fa muovere i blocchi da sinistra a destra per creare un effetto più dinamico.

---

## 5. Codice completo con gli aggiornamenti

```python
import pygame
import random

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

# --- Carica suono di collisione ---
collision_sound = pygame.mixer.Sound('collisione.wav')

# --- Crea blocchi colorati ---
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128)]
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        color = random.choice(colors)
        blocks.append({'rect': rect, 'color': color})

# --- Crea paddle e pallina ---
paddle = pygame.Rect((WIDTH - PADDLE_WIDTH) // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 6
ball = pygame.Rect(paddle.centerx, paddle.top - BALL_RADIUS*2, BALL_RADIUS*2, BALL_RADIUS*2)
ball_dx = 4
ball_dy = -4
ball_active = False
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
    
    # --- Gestione eventi ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not ball_active:
                ball_active = True
    
    # --- Movimento del paddle ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
        if not ball_active:
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
            ball_active = False
            ball.x = paddle.centerx - BALL_RADIUS
            ball.y = paddle.top - BALL_RADIUS*2

        # Collisione con paddle
        if ball.colliderect(paddle):
            ball_dy *= -1
            offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH / 2)
            ball_dx = BALL_RADIUS * offset * 1.5

        # Collisione con blocchi
        for block in blocks[:]:
            if ball.colliderect(block['rect']):
                blocks.remove(block)
                collision_sound.play()  # Suono di collisione
                ball_dy *= -1
                score += 1
                break

    # --- Disegna tutto ---
    draw_blocks()
    pygame.draw.rect(screen, (0, 0, 0), paddle)
    pygame.draw.circle(screen, PINK, ball.center, BALL_RADIUS)
    
    # --- Mostra punteggio ---
    score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, HEIGHT - 30))

    # --- Vittoria ---
    if not blocks:
        win_text = font.render("Hai Vinto!", True, (0, 128,
```

