"""
This is a modified version of the tic-tak-toe game.
According to the modification, every player can only have three moves/pieces in the board at any time.
If they have already played their three moves, and thier turn comes, their last move will become invalid after this turn.
They can move anywhere except all the boxex that shows that one have the player has a piece.
"""

from typing import List, Tuple
import json

def load_rules_form_json(filepath="rules.json") -> list[str]:
    with open(filepath, "r") as file:
        data = json.load(file)
        return data["rules"]


def rules() -> None:
    rules = load_rules_form_json()
    print("")
    for rule in rules:
        print(rule)
    print("")


def get_index_array_from_position_number(position) -> list[int]:
    """
    Position number - vs - index in array:
    board = [
             ["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]
            ]
    """
    x, y = [-1, -1]
    if position % 3 == 0:
        x = (position // 3) - 1
        y = 2
    else:
        x = position // 3
        y = (position % 3) - 1
    return [x, y]


def show_current_board(x_moves, y_moves) -> None:
    """
    This function will show the current board
    """

    board = [["*", "*", "*"],
             ["*", "*", "*"],
             ["*", "*", "*"]]
    for move in x_moves:
        index_arr = get_index_array_from_position_number(move)
        board[index_arr[1]][index_arr[0]] = "X"
    for move in y_moves:
        index_arr = get_index_array_from_position_number(move)
        board[index_arr[1]][index_arr[0]] = "O"

    for row in board:
        print(row)


def pre_move_choices(x_moves, y_moves, turn):
    all_available_positions = [(x + 1) for x in range(9)]
    occupied_positions = x_moves + y_moves
    available_moves = [x for x in all_available_positions if x not in occupied_positions]
    show_current_board(x_moves, y_moves)
    print("Current turn: ", "X" if turn == 'x' else "O")
    print("Select one of the positions among ", available_moves)


def check_win(moves):
    if len(moves) != 3:
        return False
    biggest_position = moves[0]
    smallest_position = moves[0]
    sum_positions = 0
    for move in moves:
        if move > biggest_position:
            biggest_position = move
        if move < smallest_position:
            smallest_position = move
        sum_positions += move
    
    # Following method doesn't work because it is valid for any three consecutive numbers.
    # if 2 * sum_positions == 3 * (biggest_position + smallest_position):
    #     return True

    smallest_coordinate = get_index_array_from_position_number(smallest_position)
    biggest_coordinate = get_index_array_from_position_number(biggest_position)
    median_coordinate = get_index_array_from_position_number(sum_positions - smallest_position - biggest_position)
    if ((smallest_coordinate[0] + biggest_coordinate[0]) == 2 * median_coordinate[0]) and ((smallest_coordinate[1] + biggest_coordinate[1]) == 2 * median_coordinate[1]):
        return True
    
    print(smallest_coordinate, median_coordinate, biggest_coordinate)

    return False


def move(x_moves: List[int], y_moves: List[int], turn: str, input_move=0) -> Tuple[List[int], List[int], str]:
    all_available_positions = [(x + 1) for x in range(9)]
    occupied_positions = x_moves + y_moves
    available_moves = [x for x in all_available_positions if x not in occupied_positions]
    if input_move == 0:
        show_current_board(x_moves, y_moves)
        print("Current turn: ", "X" if turn == 'x' else "O")
        print("Select one of the positions among ", available_moves)
    chosen_move = 0
    if input_move == 0:
        chosen_move = int(input())
    else:
        chosen_move = input_move
    if chosen_move not in available_moves:
        print("Invalid Move!")
        return x_moves, y_moves, turn
    if turn == 'x':
        if len(x_moves) >= 3:
            x_moves = x_moves[1:]
        # x_moves[len(x_moves)] = chosen_move       # index out of range
        # x_moves.push_back(chosen_move)            # no function called push_back()
        x_moves = x_moves + [chosen_move]
        turn = 'y'
    elif turn == 'y':
        if len(y_moves) >= 3:
            y_moves = y_moves[1:]
        # y_moves[len(y_moves)] = chosen_move       # index out of range
        # y_moves.push_back(chosen_move)            # no function called push_back()
        y_moves = y_moves + [chosen_move]
        turn = 'x'
    # print(x_moves)
    # print(y_moves)

    if check_win(x_moves):
        print("*****X Won!*****", x_moves)
        if turn == 'x':
            turn = 'y'
        else:
            turn = 'x'
        return x_moves, y_moves, turn
    if check_win(y_moves):
        print("O Won!!!", y_moves)
        if turn == 'x':
            turn = 'y'
        else:
            turn = 'x'
        return x_moves, y_moves, turn

    return x_moves, y_moves, turn 


def main_menu(x_moves, y_moves):
    print("Current Board")
    show_current_board(x_moves, y_moves)
    no_move_made = True if len(x_moves) == 0 and len(y_moves) == 0 else False
    print("")
    print("Select one of the following choices:")
    print("1. " , "Make a Move." if no_move_made else "Continue Game")
    print("2. Print Current Board.")
    print("3. Print Game Rules.")
    print("4. ", "Exit Game." if no_move_made else "Restart Game")
    if not no_move_made:
        print("5. Exit Game")

    chosen_option = int(input())

    if no_move_made and chosen_option == 4:
        chosen_option = 5

    return chosen_option


def main():
    x_moves = []
    y_moves = []
    turn = 'x'
    rules()
    print("First Move: X's turn.")
    while(1):
        choice = main_menu(x_moves, y_moves)
        if choice == 1:
            next_turn = 'x' if turn == 'y' else 'y'
            while True:
                x_moves, y_moves, next_turn = move(x_moves, y_moves, turn)
                if next_turn == turn:
                    break
                else:
                    turn = next_turn
        elif choice == 2:
            show_current_board(x_moves, y_moves)
        elif choice == 3:
            rules()
        elif choice == 4:
            x_moves = []
            y_moves = []
            turn = 'x'
            print("Board Reset.")
            # print(x_moves)
            # print(y_moves)
            show_current_board(x_moves, y_moves)
        elif choice == 5:
            exit(0)
        else: 
            print("Invalid Option!")


if __name__ == "__main__":
    main()
