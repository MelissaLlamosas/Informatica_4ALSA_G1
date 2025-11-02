# Crea blocchi colorati
colors = [# TODO: aggiungi una lista di colori RGB]

blocks = []  # lista per salvare tutti i blocchi
for row in range(# TODO: numero di righe):
    for col in range(# TODO: numero di colonne):
        # TODO: crea un rettangolo pygame.Rect con posizione e dimensioni corrette
        color = # TODO: scegli un colore casuale dalla lista
        blocks.append({'rect': rect, 'color': color})  # salva blocco

# Funzione per disegnare i blocchi
def draw_blocks():
    for block in blocks:
        # TODO: disegna il blocco colorato
        # TODO: disegna il bordo nero intorno
