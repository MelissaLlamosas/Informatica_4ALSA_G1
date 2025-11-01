Perfetto! Ecco la **Lezione 6: Vittoria, sconfitta e miglioramenti** scritta **nello stesso stile e formato** della tua “Lezione 3”, passo per passo e pensata per studenti che usano **Pygame** 👇

---

# 🏁 Lezione 6: Vittoria, sconfitta e miglioramenti

### Obiettivi della lezione

* Far terminare il gioco quando la pallina cade → **Game Over**
* Mostrare un **messaggio di vittoria** quando tutti i blocchi sono distrutti
* Resettare la pallina e il gioco dopo la vittoria o la sconfitta
* Aggiungere **effetti grafici o sonori** per rendere il gioco più interessante
* Proporre una **sfida avanzata**: blocchi che si muovono o non si distruggono

---

## 1. Game Over: la pallina cade sotto il bordo

Quando la pallina supera il bordo inferiore della finestra, il gioco deve terminare.

```python
if ball.bottom >= HEIGHT:
    game_over = True
```

Se la condizione è vera, disegniamo un messaggio e blocchiamo il gioco.

```python
if game_over:
    draw_text("GAME OVER! Premi SPAZIO per riprovare", font, RED, screen, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    waiting_restart = True
```

📘 **Spiegazione:**

* `ball.bottom` è la coordinata inferiore del rettangolo della pallina.
* Quando `ball.bottom` è uguale o maggiore dell’altezza della finestra (`HEIGHT`), significa che la pallina è “caduta”.
* `game_over = True` ferma la logica di gioco (non aggiorniamo più la pallina o i blocchi).
* `draw_text()` è una piccola funzione di utilità per scrivere messaggi sullo schermo (puoi crearla tu).

Esempio di funzione per scrivere testo:

```python
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)
```

---

## 2. Mostrare un messaggio di vittoria

Quando tutti i blocchi sono stati distrutti, vogliamo mostrare un messaggio di vittoria.

All’interno del ciclo di gioco, aggiungiamo:

```python
if all(brick["active"] == False for brick in bricks):
    victory = True
```

E poi disegniamo il messaggio:

```python
if victory:
    draw_text("HAI VINTO! Premi SPAZIO per continuare", font, GREEN, screen, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    waiting_restart = True
```

📘 **Spiegazione:**

* `all()` controlla che **tutti i blocchi** abbiano `active == False` → significa che sono stati distrutti.
* `victory = True` indica che il giocatore ha vinto.
* Come nel “Game Over”, il messaggio appare e il gioco si ferma finché il giocatore non preme **spazio**.

---

## 3. Resettare la pallina e il gioco

Quando il giocatore preme **spazio**, possiamo resettare la posizione della pallina e ricominciare.

```python
if waiting_restart:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_over = False
        victory = False
        waiting_restart = False
        reset_ball()
        reset_bricks()
```

Definiamo ora la funzione per resettare la pallina:

```python
def reset_ball():
    ball.x = paddle.centerx
    ball.y = paddle.top - BALL_RADIUS * 2
    ball_dx = 4
    ball_dy = -4
    return ball_dx, ball_dy
```

📘 **Spiegazione:**

* La pallina torna sopra il paddle, come all’inizio del gioco.
* Le velocità orizzontale (`ball_dx`) e verticale (`ball_dy`) vengono reimpostate ai valori di partenza.

---

## 4. Aggiungere effetti (grafica e suoni)

Per rendere il gioco più interessante, aggiungiamo effetti visivi o sonori.

### 🔊 Suoni

Usiamo `pygame.mixer.Sound()` per caricare i suoni.

```python
hit_sound = pygame.mixer.Sound("hit.wav")
win_sound = pygame.mixer.Sound("win.wav")
lose_sound = pygame.mixer.Sound("lose.wav")
```

Poi nei momenti giusti:

```python
if collision_with_brick:
    hit_sound.play()

if victory:
    win_sound.play()

if game_over:
    lose_sound.play()
```

### 🌈 Grafica

Puoi far lampeggiare lo sfondo o cambiare il colore della pallina:

```python
if victory:
    screen.fill((0, 255, 0))
elif game_over:
    screen.fill((255, 0, 0))
```

---

## 5. Challenge 💪

### Challenge 1: Blocchi che si muovono lentamente

```python
for brick in bricks:
    if brick["active"]:
        brick["rect"].x += math.sin(pygame.time.get_ticks() / 1000) * 0.5
```

📘 Così i blocchi oscillano lentamente a destra e sinistra!

---

### Challenge 2: Blocchi indistruttibili

Aggiungi un tipo speciale di blocco:

```python
brick = {"rect": rect, "active": True, "unbreakable": random.choice([True, False])}
```

E quando controlli la collisione:

```python
if brick["active"] and not brick["unbreakable"]:
    brick["active"] = False
```

📘 I blocchi “unbreakable” rimarranno anche dopo il colpo!

---

## 6. Riassunto del codice principale

```python
# Controllo sconfitta
if ball.bottom >= HEIGHT:
    game_over = True

# Controllo vittoria
if all(not b["active"] for b in bricks):
    victory = True

# Mostra messaggi
if game_over:
    draw_text("GAME OVER! Premi SPAZIO per riprovare", font, RED, screen, WIDTH // 2, HEIGHT // 2)
elif victory:
    draw_text("HAI VINTO! Premi SPAZIO per continuare", font, GREEN, screen, WIDTH // 2, HEIGHT // 2)

# Reset
if waiting_restart:
    if keys[pygame.K_SPACE]:
        game_over = False
        victory = False
        waiting_restart = False
        ball_dx, ball_dy = reset_ball()
        reset_bricks()
```

---

## 7. Domande per riflettere 🤔

* Come capisce il gioco quando tutti i blocchi sono stati distrutti?
* Cosa succede se non resetti le velocità della pallina dopo la sconfitta?
* Come potresti mostrare il punteggio sullo schermo?

---

## 🧠 Approfondimenti consigliati

* Aggiungi un contatore di **vite**: il gioco finisce solo dopo 3 cadute.
* Crea **livelli multipli**: ogni volta che vinci, carica nuovi blocchi.
* Implementa una **classifica dei punteggi** con `pygame.font` e file di testo.

---

Vuoi che ti scriva anche la versione del codice completo della **Lezione 6** in un unico file `.py` pronto da eseguire?
Posso includere anche i suoni e i messaggi già implementati.

