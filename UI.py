import pygame
import sys
from main import *

pygame.init()

screen = pygame.display.set_mode((300, 325))

pygame.display.set_caption("Tic-Tac-Toe: Modified")

x_moves = []
y_moves = []
turn = 'x'

def draw_board_and_pieces():
    global x_moves, y_moves, turn
    # Drawing the board
    # pygame.draw.line(surface, color(r, g, b), start_point, end_point, thickness)
    pygame.draw.line(screen, (0,0,0), (100, 0), (100, 300), 5)
    pygame.draw.line(screen, (0,0,0), (200, 0), (200, 300), 5)
    pygame.draw.line(screen, (0,0,0), (0, 100), (300, 100), 5)
    pygame.draw.line(screen, (0,0,0), (0, 200), (300, 200), 5)
    pygame.draw.line(screen, (0,0,0), (0, 300), (300, 300), 5)

    # Drawing pieces
    for x_piece in x_moves:
        # Drawing X in center of square x_piece
        x, y = get_index_array_from_position_number(x_piece)
        x_center = (100 * x) + 50
        y_center = (100 * y) + 50
        pygame.draw.line(screen, (0,0,0), ((x_center - 25), (y_center - 25)), ((x_center + 25), (y_center + 25)), 3)
        pygame.draw.line(screen, (0,0,0), ((x_center - 25), (y_center + 25)), ((x_center + 25), (y_center - 25)), 3)
    
    for y_piece in y_moves:
        # Drawing O in center of square y_piece
        x, y = get_index_array_from_position_number(y_piece)
        x_center = (100 * x) + 50
        y_center = (100 * y) + 50
        pygame.draw.circle(screen, (0, 0, 0), (x_center, y_center), 25, 3)

    # Rendering the turn text
    font = pygame.font.Font(None, 25)
    text_surface = font.render("Turn: ?", True, (0, 0, 0))
    if turn == 'x':
        text_surface = font.render("Turn: X", True, (0, 0, 0))
    else:
        text_surface = font.render("Turn: O", True, (0, 0, 0))
    
    text_area = text_surface.get_rect(center=(150, 314))
    screen.blit(text_surface, text_area)
    
    return

"""
def get_chosen_move_position_from_mouse_location(mouse_location):
    position = 0
    if mouse_location[0] > 205 and mouse_location[0] < 295:
        # pos 7, 8, 9
        position = 6
    elif mouse_location[0] > 105 and mouse_location[0] < 195:
        # pos 4, 5, 6
        position = 3
    elif mouse_location[0] > 5 and mouse_location[0] < 95:
        # pos 1, 2, 3
        pass
    else:
        # Invalid position
        return -1
    
    if mouse_location[1] > 205 and mouse_location[1] < 295:
        position += 3
    elif mouse_location[1] > 105 and mouse_location[1] < 195:
        position += 2
    elif mouse_location[1] > 5 and mouse_location[1] < 95:
        position += 1
    else:
        # Invalid position
        return -1
    
    return position
"""

def get_chosen_move_position_from_mouse_location(mouse_location):
    if mouse_location[0] >= 300 or mouse_location[1] >= 300:
        return -1
    
    return ((mouse_location[0] // 100) * 3) + ((mouse_location[1] // 100) + 1)

def try_to_move(mouse_location):
    global x_moves, y_moves, turn
    position = get_chosen_move_position_from_mouse_location(mouse_location)
    x_moves, y_moves, turn = move(x_moves, y_moves, turn, position)

    # Check win

    pre_move_choices(x_moves, y_moves, turn)

def game_loop():
    while True:
        screen.fill((150, 150, 150))
        draw_board_and_pieces()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                try_to_move(pygame.mouse.get_pos())
        
        pygame.display.flip()

def draw_text_centered(text, y, color=(0, 0, 0), size=30):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(150, y))
    screen.blit(text_surface, rect)
    return rect

def menu_loop():
    while True:
        screen.fill((160, 160, 160))
        # draw menu and menu-items

        title_rect = draw_text_centered("Tic-Tac-Toe", 60, size=36)
        play_rect = draw_text_centered("1. Play Game", 120)
        rules_rect = draw_text_centered("2. View Rules", 170)
        exit_rect = draw_text_centered("3. Exit Game", 220)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    return "play"
                elif rules_rect.collidepoint(event.pos):
                    return "rules"
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    choice = menu_loop()
    if choice == "play":
        game_loop()
    elif choice == "rules":
        pass
