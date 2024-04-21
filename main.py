class Colors:
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


class Piece:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


def print_chess_board(chess_board, highlight=None):
    for row in range(8):
        for col in range(8):
            color = Colors.WHITE
            piece = chess_board[row][col]
            if piece.colour == "black" and [row, col] not in highlight:
                color = Colors.GREEN
            elif piece.colour == "white" and [row, col] not in highlight:
                color = Colors.WHITE
            elif highlight and [row, col] in highlight:
                color = Colors.RED
            print(color, piece.name, Colors.RESET, end="")
        print()


def ask_user_input():
    print("Enter move")
    while True:
        try:
            row = int(input("Enter row:")) - 1
            column = int(input("Enter column:")) - 1
            if 0 <= row <= 7 and 0 <= column <= 7:
                return row, column
            else:
                print("Invalid input. Row and column must be between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")


def print_possible_moves(board, x1, x2, turn):
    return_value = []
    piece = board[x1][x2]

    if turn == (piece.colour == 'white'):
        direction = 1 if turn else -1
        initial_row = 1 if turn else 6
        opponent_color = 'black' if turn else 'white'

        if piece.name == 'p':
            if board[x1 + direction][x2].name == '_':
                return_value.append([x1 + direction, x2])
                if x1 == initial_row and board[x1 + 2 * direction][x2].name == '_':
                    return_value.append([x1 + 2 * direction, x2])
            if not return_value:
                print("No moves available")

            for dx in [-1, 1]:
                if 0 <= x2 + dx < 8 and board[x1 + direction][x2 + dx].colour == opponent_color:
                    return_value.append([x1 + direction, x2 + dx])
        elif piece.name == 'N':
            possible_moves = [(x1 + 2, x2 + 1), (x1 + 2, x2 - 1), (x1 + 1, x2 + 2), (x1 + 1, x2 - 2), (x1 - 2, x2 + 1),
                              (x1 - 2, x2 - 1), (x1 - 1, x2 + 2), (x1 - 1, x2 - 2)]
            for move in possible_moves:
                nx, ny = move
                if 0 <= nx < 8 and 0 <= ny < 8 and (
                        board[nx][ny].colour == opponent_color or board[nx][ny].name == '_'):
                    return_value.append([nx, ny])
            if not return_value:
                print("No moves available")

        elif piece.name == 'B':
            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                end = False
                y = 1
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                        else:
                            end = True
                    else:
                        end = True
                    y += 1
            if not return_value:
                print("No moves available")

        elif piece.name == 'R':
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                y = 1
                end = False
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                    else:
                        end = True
                    y += 1

        elif piece.name == 'Q':
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                y = 1
                end = False
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                    else:
                        end = True
                    y += 1

            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                end = False
                y = 1
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                        else:
                            end = True
                    else:
                        end = True
                    y += 1
            if not return_value:
                print("No moves available")

        elif piece.name == 'K':
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx = x1 + dx
                    ny = x2 + dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_' or board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])

    else:
        print("Wrong turn!")

    return return_value


def ask_move(possible_moves):
    input_string = input("Enter move: ")
    move = [int(x) for x in input_string.split()]
    if move in possible_moves:
        print("Good work")
    else:
        print("Not a valid move")


def move_piece(board, ):
    print("hi")


def main():
    end = False
    turn = True

    chess_board = [
        [Piece('R', 'white'), Piece('N', 'white'), Piece('B', 'white'), Piece('K', 'white'), Piece('Q', 'white'),
         Piece('B', 'white'), Piece('N', 'white'), Piece('R', 'white')],
                                                                         [Piece('_', 'white')] * 8,
                                                                         [Piece('_', 'normal')] * 8,
                                                                         [Piece('_', 'normal')] * 8,
                                                                         [Piece('_', 'normal')] * 8,
                                                                         [Piece('_', 'normal')] * 8,
                                                                         [Piece('_', 'black')] * 8,
        [Piece('R', 'black'), Piece('N', 'black'), Piece('B', 'black'), Piece('K', 'black'), Piece('Q', 'black'),
         Piece('B', 'black'), Piece('N', 'black'), Piece('R', 'black')]]

    possible_moves = []
    print_chess_board(chess_board, possible_moves)

    while not end:
        row, column = ask_user_input()
        possible_moves = print_possible_moves(chess_board, row, column, turn)
        print_chess_board(chess_board, possible_moves)
        print(possible_moves)
        ask_move(possible_moves)
        turn = not turn


if __name__ == "__main__":
    main()
