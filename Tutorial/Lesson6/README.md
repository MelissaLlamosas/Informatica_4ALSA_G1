
# Lezione 6: Vittoria, sconfitta e miglioramenti

### Obiettivi della lezione

* Gestire la **fine del gioco** (quando la pallina cade).
* Mostrare un **messaggio di vittoria** quando tutti i blocchi sono distrutti.
* **Resettare la pallina** per far ripartire il gioco.
* Aggiungere **punteggio** e semplici **effetti visivi o sonori**.
* Proporre una **challenge**: blocchi che si rompono solo dopo due colpi.

---

## 1. Game over: quando la pallina cade 

Controlliamo se la pallina **cade oltre il bordo inferiore** dello schermo.
In quel caso, la partita si interrompe e la pallina viene rimessa sopra il paddle:

```python
if ball.bottom >= HEIGHT:
    ball_active = False  # La pallina si ferma
    # Rimetti la pallina sopra il paddle
    ball.x = paddle.centerx - BALL_RADIUS
    ball.y = paddle.top - BALL_RADIUS*2
```

**Spiegazione:**

* `ball.bottom` indica la posizione verticale del bordo inferiore della pallina.
* Quando supera `HEIGHT`, vuol dire che è uscita dallo schermo.
* `ball_active = False` blocca il movimento, e la pallina torna al punto di partenza.

 Questo comportamento simula una **sconfitta temporanea** (non chiude il gioco).

---

## 2. Mostrare la vittoria 

La vittoria avviene quando **tutti i blocchi sono stati distrutti**:

```python
if not blocks:
    win_text = font.render("Hai Vinto!", True, (0, 128, 0))
    screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    running = False
```

**Cosa succede:**

* `if not blocks:` controlla se la lista `blocks` è vuota.
* Se sì, mostra “Hai Vinto!” al centro dello schermo per 2 secondi.
* Poi il gioco termina (`running = False`).

In un’estensione futura, potresti **ricominciare automaticamente** il gioco invece di chiuderlo.

---

## 3. Aggiungere un punteggio 

Nel codice, ogni volta che un blocco viene distrutto, il punteggio aumenta:

```python
score += 1
```

E viene mostrato in basso allo schermo:

```python
score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
screen.blit(score_text, (10, HEIGHT - 30))
```

Il punteggio aiuta il giocatore a monitorare i propri progressi e la precisione dei colpi.

---

## 4. Effetti visivi e sonori 

### Effetti sonori

Puoi aggiungere effetti con `pygame.mixer.Sound`:

```python
hit_sound = pygame.mixer.Sound("hit.wav")
win_sound = pygame.mixer.Sound("win.wav")

# Quando colpisci un blocco
hit_sound.play()

# Quando vinci
win_sound.play()
```

### Effetti visivi

```python
if not blocks:
    screen.fill((200, 255, 200))  # Colore verde chiaro per la vittoria
```

 Questi dettagli rendono il gioco più vivo e divertente.

---

## 5. Challenge: blocchi che si rompono solo al secondo colpo 

In questa variante, i blocchi **non si distruggono subito**, ma solo **dopo essere stati colpiti due volte**.
Per farlo, assegniamo ad ogni blocco una **vita iniziale** di 2 colpi (`'hits': 2`).

### Creazione dei blocchi con punti vita

```python
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        color = random.choice(colors)
        blocks.append({'rect': rect, 'color': color, 'hits': 2})
```

### Gestione della collisione

```python
for block in blocks[:]:
    if ball.colliderect(block['rect']):
        block['hits'] -= 1  # Il blocco perde una “vita”
        ball_dy *= -1       # La pallina rimbalza

        if block['hits'] == 1:
            block['color'] = (150, 150, 150)  # Cambia colore per mostrare il danno
        elif block['hits'] <= 0:
            blocks.remove(block)              # Si rompe al secondo colpo
            score += 1
        break
```

**Spiegazione:**

* Ogni blocco parte con `hits = 2`.
* Dopo il primo colpo → `hits` diventa `1` → cambia colore per segnalare che è danneggiato.
* Dopo il secondo colpo → `hits = 0` → viene rimosso dalla lista (`blocks.remove`).

Questo introduce una **meccanica di resistenza**, rendendo il gioco più interessante.

---

## 6. Challenge per la classe 

1. Mostra un **messaggio di “Game Over”** quando la pallina cade.
2. Crea blocchi con **resistenza diversa** (alcuni con 1, altri con 3 colpi).

---

## 7. Domande per riflettere 

* Come potresti indicare visivamente quanti colpi restano a un blocco?
* Quale strategia rende più divertente il gioco: blocchi forti o tanti blocchi deboli?
* Come potresti salvare il punteggio più alto?
* Cosa succederebbe se la pallina colpisse due blocchi nello stesso frame?




# Lezione 6: Vittoria, sconfitta e miglioramenti

### Obiettivi della lezione

* Gestire la **fine del gioco** (quando la pallina cade).
* Mostrare un **messaggio di vittoria** quando tutti i blocchi sono distrutti.
* **Resettare la pallina** per far ripartire il gioco.
* Aggiungere **punteggio** e semplici **effetti visivi o sonori**.
* Proporre una **challenge**: blocchi che si rompono solo dopo due colpi.

---

## 1. Game over: quando la pallina cade 

Controlliamo se la pallina **cade oltre il bordo inferiore** dello schermo.
In quel caso, la partita si interrompe e la pallina viene rimessa sopra il paddle:

```python
if ball.bottom >= HEIGHT:
    ball_active = False  # La pallina si ferma
    # Rimetti la pallina sopra il paddle
    ball.x = paddle.centerx - BALL_RADIUS
    ball.y = paddle.top - BALL_RADIUS*2
```

**Spiegazione:**

* `ball.bottom` indica la posizione verticale del bordo inferiore della pallina.
* Quando supera `HEIGHT`, vuol dire che è uscita dallo schermo.
* `ball_active = False` blocca il movimento, e la pallina torna al punto di partenza.

 Questo comportamento simula una **sconfitta temporanea** (non chiude il gioco).

---

## 2. Mostrare la vittoria 

La vittoria avviene quando **tutti i blocchi sono stati distrutti**:

```python
if not blocks:
    win_text = font.render("Hai Vinto!", True, (0, 128, 0))
    screen.blit(win_text, (WIDTH // 2 - 60, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    running = False
```

**Cosa succede:**

* `if not blocks:` controlla se la lista `blocks` è vuota.
* Se sì, mostra “Hai Vinto!” al centro dello schermo per 2 secondi.
* Poi il gioco termina (`running = False`).

In un’estensione futura, potresti **ricominciare automaticamente** il gioco invece di chiuderlo.

---

## 3. Aggiungere un punteggio 

Nel codice, ogni volta che un blocco viene distrutto, il punteggio aumenta:

```python
score += 1
```

E viene mostrato in basso allo schermo:

```python
score_text = font.render(f"Punteggio: {score}", True, (0, 0, 0))
screen.blit(score_text, (10, HEIGHT - 30))
```

Il punteggio aiuta il giocatore a monitorare i propri progressi e la precisione dei colpi.

---

## 4. Effetti visivi e sonori 

### Effetti sonori

Puoi aggiungere effetti con `pygame.mixer.Sound`:

```python
hit_sound = pygame.mixer.Sound("hit.wav")
win_sound = pygame.mixer.Sound("win.wav")

# Quando colpisci un blocco
hit_sound.play()

# Quando vinci
win_sound.play()
```

### Effetti visivi

```python
if not blocks:
    screen.fill((200, 255, 200))  # Colore verde chiaro per la vittoria
```

 Questi dettagli rendono il gioco più vivo e divertente.

---

## 5. Challenge: blocchi che si rompono solo al secondo colpo 

In questa variante, i blocchi **non si distruggono subito**, ma solo **dopo essere stati colpiti due volte**.
Per farlo, assegniamo ad ogni blocco una **vita iniziale** di 2 colpi (`'hits': 2`).

### Creazione dei blocchi con punti vita

```python
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        color = random.choice(colors)
        blocks.append({'rect': rect, 'color': color, 'hits': 2})
```

### Gestione della collisione

```python
for block in blocks[:]:
    if ball.colliderect(block['rect']):
        block['hits'] -= 1  # Il blocco perde una “vita”
        ball_dy *= -1       # La pallina rimbalza

        if block['hits'] == 1:
            block['color'] = (150, 150, 150)  # Cambia colore per mostrare il danno
        elif block['hits'] <= 0:
            blocks.remove(block)              # Si rompe al secondo colpo
            score += 1
        break
```

**Spiegazione:**

* Ogni blocco parte con `hits = 2`.
* Dopo il primo colpo → `hits` diventa `1` → cambia colore per segnalare che è danneggiato.
* Dopo il secondo colpo → `hits = 0` → viene rimosso dalla lista (`blocks.remove`).

Questo introduce una **meccanica di resistenza**, rendendo il gioco più interessante.

---

## 6. Challenge per la classe 

1. Mostra un **messaggio di “Game Over”** quando la pallina cade.
2. Crea blocchi con **resistenza diversa** (alcuni con 1, altri con 3 colpi).

---

## 7. Domande per riflettere 

* Come potresti indicare visivamente quanti colpi restano a un blocco?
* Quale strategia rende più divertente il gioco: blocchi forti o tanti blocchi deboli?
* Come potresti salvare il punteggio più alto?
* Cosa succederebbe se la pallina colpisse due blocchi nello stesso frame?



