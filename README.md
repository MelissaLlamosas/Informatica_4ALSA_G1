# Informatica_4ALSA_G1
# Breakout Game – Python & Pygame
![gif](../../Images/game.gif) 


Questo progetto è una semplice versione del classico gioco **Breakout**, realizzata in **Python** con la libreria **Pygame**.  
L’obiettivo del gioco è rompere tutti i blocchi colorati con la pallina, controllando il paddle nella parte inferiore dello schermo.  
Quando tutti i blocchi vengono distrutti, il giocatore vince la partita.

## Descrizione del gioco

Il giocatore controlla un **paddle** situato nella parte inferiore dello schermo e deve evitare che la pallina cada.  
Ogni volta che la pallina colpisce un blocco, il blocco viene distrutto e il punteggio aumenta.  
Quando tutti i blocchi vengono eliminati, la partita termina con la vittoria.  

Il gioco include:
- Generazione casuale dei colori dei blocchi  
- Movimento del paddle tramite le frecce direzionali  
- Gestione dei rimbalzi e delle collisioni  
- Sistema di punteggio e messaggio di vittoria  

## Struttura della repository

La repository è organizzata in modo da guidare passo dopo passo nella realizzazione del gioco.  
È composta da una cartella principale chiamata `tutorial`, che contiene **6 lezioni**, due per ogni componente del gruppo.

## Struttura del progetto

Ogni lezione contiene:
- una **cartella `images/`** con le immagini necessarie alla spiegazione;  
- una **cartella `templates/`** con i file di riferimento;  
- un file **`README.md`** che contiene il vero e proprio tutorial con spiegazioni e passaggi di sviluppo;  
- un file **`lessonX-soluzione.py`** con la soluzione funzionante della lezione.  

Se durante la realizzazione sono stati riscontrati o corretti errori nel codice, questi sono stati segnalati e documentati all’interno dei rispettivi tutorial, per rendere il percorso più chiaro e didattico.

## Prerequisiti

- **Python 3.10** o superiore  
- **Pygame** installato

Per installare Pygame:
```bash
pip install pygame
