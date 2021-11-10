import numpy as np

game_matrix = np.array([[' ', ' ', ' '],
                        [' ', ' ', ' '],
                        [' ', ' ', ' ']])
X = 'X'
O = 'O'


def print_matrix(m):
    print("---------\n"
          f"| {m[0, 0]} {m[0, 1]} {m[0, 2]} |\n"
          f"| {m[1, 0]} {m[1, 1]} {m[1, 2]} |\n"
          f"| {m[2, 0]} {m[2, 1]} {m[2, 2]} |\n"
          "---------")


def print_occ():
    print("This cell is occupied! Choose another one!")


def print_game():
    print_matrix(game_matrix)
    print("Enter the coordinates:")


def x_move():
    print_game()
    c = input()
    c1 = int(c[0]) - 1
    c2 = int(c[2]) - 1
    if c1 < 3 and c2 < 3:
        if game_matrix[c1, c2] == X or game_matrix[c1, c2] == O:
            print_occ()
            x_move()
        else:
            game_matrix[c1, c2] = X
            if check(game_matrix) == 0:
                o_move()
            else:
                print_matrix(game_matrix)
                print(check(game_matrix))
    else:
        print_occ()
        x_move()


def o_move():
    print_game()
    c = input()
    c1 = int(c[0]) - 1
    c2 = int(c[2]) - 1
    if c1 < 3 and c2 < 3:
        if game_matrix[c1, c2] == X or game_matrix[c1, c2] == O:
            print_occ()
            o_move()
        else:
            game_matrix[c1, c2] = O
            if check(game_matrix) == 0:
                x_move()
            else:
                print_matrix(game_matrix)
                print(check(game_matrix))
    else:
        print_occ()
        o_move()


def check(m):
    game_check = True
    if game_check is False or ((m[0, 0] == X and m[0, 1] == X and m[0, 2] == X) or
                               (m[1, 0] == X and m[1, 1] == X and m[1, 2] == X) or
                               (m[2, 0] == X and m[2, 1] == X and m[2, 2] == X) or
                               (m[0, 0] == X and m[1, 0] == X and m[2, 0] == X) or
                               (m[0, 1] == X and m[1, 1] == X and m[2, 1] == X) or
                               (m[0, 2] == X and m[1, 2] == X and m[2, 2] == X) or
                               (m[0, 0] == X and m[1, 1] == X and m[2, 2] == X) or
                               (m[0, 2] == X and m[1, 1] == X and m[2, 0] == X)):
        return "X wins"
    elif ((m[0, 0] == O and m[0, 1] == O and m[0, 2] == O) or
          (m[1, 0] == O and m[1, 1] == O and m[1, 2] == O) or
          (m[2, 0] == O and m[2, 1] == O and m[2, 2] == O) or
          (m[0, 0] == O and m[1, 0] == O and m[2, 0] == O) or
          (m[0, 1] == O and m[1, 1] == O and m[2, 1] == O) or
          (m[0, 2] == O and m[1, 2] == O and m[2, 2] == O) or
          (m[0, 0] == O and m[1, 1] == O and m[2, 2] == O) or
          (m[0, 2] == O and m[1, 1] == O and m[2, 0] == O)):
        return "O wins"
    elif ' ' in game_matrix:
        return 0

    else:
        return "Draw"


x_move()
