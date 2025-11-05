# Lezione 6: Vittoria, sconfitta e miglioramenti

### Obiettivi della lezione

* Imparare a gestire la **vittoria** e la **sconfitta** nel gioco.
* Aggiungere un **messaggio di vittoria** quando tutti i blocchi sono distrutti.
* **Resettare la pallina** quando cade fuori dallo schermo.
* Introdurre **effetti grafici / sonori** per migliorare l’esperienza di gioco.
* **Challenge**: Blocchi che si muovono lentamente.

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


