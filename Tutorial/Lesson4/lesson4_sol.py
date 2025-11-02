# --- Aggiungi la pallina sopra il paddle ---
BALL_RADIUS = 8
PINK = (255, 105, 180)

ball = pygame.Rect(paddle.centerx - BALL_RADIUS, paddle.top - BALL_RADIUS*2, BALL_RADIUS*2, BALL_RADIUS*2)
ball_dx = 4
ball_dy = -4
ball_active = False

# --- lancio della pallina ---
if ball_active:
    ball.x += ball_dx
    ball.y += ball_dy

    # Rimbalzo sui bordi
    if ball.left <= 0 or ball.right >= LARGHEZZA:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
    if ball.bottom >= ALTEZZA:
        ball_active = False
        ball.x = paddle.centerx - BALL_RADIUS
        ball.y = paddle.top - BALL_RADIUS*2

    # Rimbalzo sul paddle
    if ball.colliderect(paddle):
        ball_dy *= -1
        offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH / 2)
        ball_dx = BALL_RADIUS * offset * 1.5

# --- Disegno della pallina ---
pygame.draw.circle(schermo, PINK, ball.center, BALL_RADIUS)
