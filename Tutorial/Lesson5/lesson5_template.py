# Punteggio iniziale 
score = 0

# Collisione con blocchi
for block in blocks[:]:
    if # TODO: controlla se la pallina collide con il blocco
        # TODO: rimuovi il blocco
        # TODO: cambia direzione verticale
        # TODO: aumenta il punteggio
        break

# Mostra punteggio
score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
screen.blit(score_text, (# TODO: posizione testo))
