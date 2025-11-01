# Lezione 1 - Creare la finestra e impostare Pygame

In questa prima lezione impareremo a creare la finestra di gioco, impostare Pygame e mostrare uno sfondo bianco.  
Questo è il punto di partenza per qualsiasi videogioco 2D.

# 🧱 Lezione 1 — Creare la finestra e impostare Pygame

## 🎯 Obiettivo dell’esercizio
> In questa prima lezione creeremo la base del nostro gioco **Breakout**, imparando a:
> - Inizializzare Pygame  
> - Creare la finestra di gioco  
> - Impostare titolo, colori, FPS e clock  
> - Mostrare uno sfondo bianco  
>
> Alla fine, il programma aprirà una finestra bianca vuota — il punto di partenza per costruire tutto il resto del gioco!

---

## 🧩 Concetti chiave

---

### 🔹 1. Inizializzare Pygame
> Prima di poter usare qualsiasi funzione di Pygame, bisogna **inizializzarlo** con:
>
> ```python
> import pygame
> pygame.init()
> ```
>
> Questo comando prepara tutte le sue componenti (grafica, suoni, input da tastiera, ecc.) per essere usate.  
> È sempre il **primo passo** in qualsiasi progetto Pygame.

---

### 🔹 2. Creare la finestra di gioco
> La finestra principale si crea con `pygame.display.set_mode()` specificando **larghezza** e **altezza**:
>
> ```python
> WIDTH, HEIGHT = 480, 640
> screen = pygame.display.set_mode((WIDTH, HEIGHT))
> ```
>
> Puoi pensare a `screen` come a un foglio bianco su cui disegnare tutti gli oggetti del gioco.  
> È l’area visiva in cui appariranno paddle, pallina, blocchi e punteggi.

---

### 🔹 3. Impostare titolo, FPS e clock
> Il titolo è il testo che appare in alto sulla finestra:
>
> ```python
> pygame.display.set_caption("Breakout Pygame")
> ```
>
> Gli **FPS (Frame Per Second)** controllano la velocità di aggiornamento del gioco:
>
> ```python
> FPS = 60
> clock = pygame.time.Clock()
> ```
>
> Con `clock.tick(FPS)` diremo al gioco di non superare i 60 aggiornamenti al secondo.  
> Questo rende il movimento **fluido e costante** su qualsiasi computer.

---

### 🔹 4. Definire i colori
> In Pygame i colori sono tuple RGB, cioè tre numeri tra 0 e 255 che rappresentano **Rosso, Verde e Blu**.
>
> ```python
> WHITE = (255, 255, 255)
> BLACK = (0, 0, 0)
> PINK = (255, 105, 180)
> ```
>
> Li useremo per colorare sfondo, blocchi, paddle e pallina.

---

### 🔹 5. Mostrare uno sfondo bianco
> Il metodo `screen.fill()` riempie la finestra con un colore:
>
> ```python
> screen.fill(WHITE)
> pygame.display.flip()
> ```
>
> `pygame.display.flip()` serve per **aggiornare la finestra**, mostrando tutto ciò che è stato disegnato.  
> È necessario ogni volta che modifichiamo qualcosa sullo schermo.

---

### 🔹 6. Loop principale del gioco
> Per mantenere aperta la finestra e gestire gli eventi (come chiudere con la “X”), serve un **game loop**:
>
> ```python
> running = True
> while running:
>     for event in pygame.event.get():
>         if event.type == pygame.QUIT:
>             running = False
>
>     screen.fill(WHITE)
>     pygame.display.flip()
> ```
>
> Questo ciclo viene eseguito **continuamente** finché il giocatore non chiude la finestra.  
> È il cuore del gioco, dove in futuro gestiremo i movimenti, le collisioni e i punteggi.

---

## 🚀 Codice completo della Lezione 1

```python
import pygame

# Inizializza Pygame
pygame.init()

# --- Costanti ---
WIDTH, HEIGHT = 480, 640
FPS = 60
WHITE = (255, 255, 255)

# --- Imposta finestra ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Pygame")
clock = pygame.time.Clock()

# --- Loop principale ---
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Riempi la finestra di bianco
    screen.fill(WHITE)

    # Aggiorna la finestra
    pygame.display.flip()

# Chiudi il gioco
pygame.quit()
