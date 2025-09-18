import os
import pygame

pygame.init()

# Obtém a lista de monitores
display_info = pygame.display.get_desktop_sizes()
print("Monitores detectados:", display_info)

# Supondo que o projetor seja o segundo monitor (índice 1)
monitor_index = 1
screen_width, screen_height = display_info[monitor_index]

# Posição do segundo monitor (x, y)
# Para a maioria dos setups, o segundo monitor começa na largura do primeiro
x_offset = display_info[0][0]  # largura do primeiro monitor
y_offset = 0

# Define a posição da janela antes de criar
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x_offset},{y_offset}"

# Cria a janela fullscreen no segundo monitor
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # fundo preto
    # Desenho de exemplo
    pygame.draw.circle(screen, (255, 0, 0), (screen_width//2, screen_height//2), 100)


pygame.quit()
