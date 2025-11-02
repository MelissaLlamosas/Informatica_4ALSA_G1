# Crea blocchi colorati
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0),
          (0, 255, 0), (0, 0, 255), (128, 0, 128)]  # Colori possibili

blocks = []  # Lista per salvare tutti i blocchi
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        rect = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
        color = random.choice(colors)
        blocks.append({'rect': rect, 'color': color})

# Funzione per disegnare tutti i blocchi
def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, block['color'], block['rect'])       # Disegna blocco colorato
        pygame.draw.rect(screen, (0, 0, 0), block['rect'], 1)         # Bordo nero
