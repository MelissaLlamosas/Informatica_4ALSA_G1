# Informatica_4ALSA_G1
# Breakout Game – Python & Pygame

Questo progetto è una semplice versione del classico gioco **Breakout**, realizzata in **Python** con la libreria **Pygame**.  
L’obiettivo del gioco è rompere tutti i blocchi colorati con la pallina, controllando il paddle nella parte inferiore dello schermo.  
Quando tutti i blocchi vengono distrutti, il giocatore vince la partita.

## Struttura del progetto

- **breakout.py** → file principale con il codice del gioco  
- Utilizza **Pygame** per la grafica e la gestione degli eventi  
- Include:
  - generazione casuale dei colori dei blocchi  
  - movimento del paddle con le frecce direzionali  
  - gestione dei rimbalzi e delle collisioni  
  - conteggio del punteggio e messaggio di vittoria  

## Prerequisiti

- **Python 3.10** o superiore  
- Libreria **Pygame** installata  

Per installare Pygame:
```bash
pip install pygame
