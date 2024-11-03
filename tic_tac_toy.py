from random import choice


def print_board(board):
    
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
        
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return board[0][col]
        
        if board[0][0] == board[1][1] ==board[2][2] != ' ':
            return board[0][0]
        
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        
        return None
            

def make_move(board, player, row, col):
    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def get_computer_move(board, is_center):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))
    return choice(available_moves)


def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    current_player = choice(players)
    print('Вы играете за:', current_player)

    while True:
        print_board(board)
        if current_player == 'X':
            row = int(input('Введите строку (0-2):'))
            col = int(input('Введите столбец (0-2):'))
            if not make_move(board, current_player, row, col):
                print('Неверный ход, попробуйте еще раз.')
                continue
        
        else:
            row, col = get_computer_move(board)
            make_move(board, current_player, row, col)

        if check_winner(board):
            print_board(board)
            print('Игрок', current_player, 'выйграл!')
            break
        if all(all(cell != ' ' for cell in row) for row in board):
            print_board(board)
            print('Ничья!')
            break

        current_player = players[1 - players.index(current_player)]


main()
