#CHALLENGE: aggiungi palline
###aggiungendo queste righe al codice il gioco sarà in grado di aggiungere una pallina ogni volta che si preme il tasto "X"

# --- Lista per palline multiple ---
balls = [ball.copy()]  # Inizia con la pallina originale

# --- All'interno del loop eventi ---
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            ball_active = True  # Lancia la prima pallina
        if event.key == pygame.K_x:
            # Crea una nuova pallina sopra il paddle
            new_ball = pygame.Rect(paddle.centerx - BALL_RADIUS, paddle.top - BALL_RADIUS*2, BALL_RADIUS*2, BALL_RADIUS*2)
            balls.append(new_ball)  # Aggiungi alla lista

# --- Movimento e disegno delle palline ---
for b in balls:
    if ball_active:
        b.x += ball_dx
        b.y += ball_dy
    pygame.draw.circle(screen, PINK, b.center, BALL_RADIUS)  # Disegna pallina
