import pygame
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
    pygame.draw.line(screen, (0,0,0), (100, 0), (100, 300), 5)
    pygame.draw.line(screen, (0,0,0), (200, 0), (200, 300), 5)
    pygame.draw.line(screen, (0,0,0), (0, 100), (300, 100), 5)
    pygame.draw.line(screen, (0,0,0), (0, 200), (300, 200), 5)
    pygame.draw.line(screen, (0,0,0), (0, 300), (300, 300), 5)

    # Rendering the turn
    font = pygame.font.Font(None, 25)
    text_surface = font.render("Turn: ?", True, (0, 0, 0))
    if turn == 'x':
        text_surface = font.render("Turn: X", True, (0, 0, 0))
    else:
        text_surface = font.render("Turn: O", True, (0, 0, 0))
    
    text_area = text_surface.get_rect(center=(150, 314))
    screen.blit(text_surface, text_area)


    # Drawing pieces
    for x_piece in x_moves:
        # Drawing x in center of square x_piece
        x, y = get_index_array_from_position_number(x_piece)
        x_center = (100 * x) + 50
        y_center = (100 * y) + 50
        pygame.draw.line(screen, (0,0,0), ((x_center - 25), (y_center - 25)), ((x_center + 25), (y_center + 25)), 3)
        pygame.draw.line(screen, (0,0,0), ((x_center - 25), (y_center + 25)), ((x_center + 25), (y_center - 25)), 3)
    
    for y_piece in y_moves:
        # Drawing x in center of square x_piece
        x, y = get_index_array_from_position_number(y_piece)
        x_center = (100 * x) + 50
        y_center = (100 * y) + 50
        pygame.draw.circle(screen, (0, 0, 0), (x_center, y_center), 25, 3)

def get_position_from_mouse_location(mouse_location):
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

def try_to_move(mouse_location):
    global x_moves, y_moves, turn
    position = get_position_from_mouse_location(mouse_location)
    x_moves, y_moves, turn = move(x_moves, y_moves, turn, position)

    # Check win

    pre_move_choices(x_moves, y_moves, turn)

game_loop = True
while game_loop:
    screen.fill((150, 150, 150))
    draw_board_and_pieces()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_location = pygame.mouse.get_pos()
            try_to_move(mouse_location)
    
    pygame.display.flip()
