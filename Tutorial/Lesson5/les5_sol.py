# Punteggio iniziale
score = 0

# Collisione con blocchi
for block in blocks[:]:
    if ball.colliderect(block['rect']):
        blocks.remove(block)      # Rimuovi blocco colpito
        ball_dy *= -1             # Rimbalza
        score += 1                # Aumenta punteggio
        break

# Mostra punteggio
score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
screen.blit(score_text, (10, HEIGHT - 30))
