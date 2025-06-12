from lib.window import *
from lib.board import *

class X_or_O(Board_Object):
    def __init__(self, x_padding, y_padding, cell:Cell, player):
        self.__x1 = cell.x + x_padding
        self.__y1 = cell.y + y_padding
        self.__x2 = cell.x + cell.length - x_padding
        self.__y2 = cell.y + cell.height - y_padding
        self.__player = player
        

    def draw(self, canvas:Canvas):
        if self.__player == 'O':
            canvas.create_oval(self.__x1, self.__y1, self.__x2, self.__y2, outline="olivedrab4", width=20)

        if self.__player == 'X':
            canvas.create_line(self.__x1, self.__y1, self.__x2, self.__y2, fill="olivedrab4", width=20)
            canvas.create_line(self.__x1, self.__y2, self.__x2, self.__y1, fill="olivedrab4", width=20)

player = 'X'
board_state = [ ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.'] ]
game_won = False

def on_click(board:Board, cell:Cell, x, y):
    global player
    global board_state
    global game_won

    if game_won:
        game_won = False
        board_state = [ ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.'] ]
        board.reset_board()
        board.draw()
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        return 

    print(f"player is {player}  and cell clicked is ({x}, {y})")

    if player == 'X' and board_state[x][y] == '.':
        board.update_cell(x, y, X_or_O(30, 30, cell, 'X'))
        board_state[x][y] = player
        board.draw()
        check_win(board)
        player = 'O'
    elif player == 'O' and board_state[x][y] == '.':
        board.update_cell(x, y, X_or_O(30, 30, cell, 'O'))
        board_state[x][y] = player
        board.draw()
        check_win(board)
        player = 'X'

def check_win(board:Board):
    global game_won
    global board_state
    global player

    ok = False
    for row in board_state:
        for col in row:
            if col == '.':
                ok = True

    if not ok:
        print('tie!')
        game_won = True

    winning_states = [  [(0,0), (0, 1), (0, 2)],
                    [(1,0), (1, 1), (1, 2)],
                    [(2,0), (2, 1), (2, 2)],
                    [(0,0), (1, 0), (2, 0)],
                    [(0,1), (1, 1), (2, 1)],
                    [(0,2), (1, 2), (2, 2)],
                    [(0,0), (1, 1), (2, 2)],
                    [(0,2), (1, 1), (2, 0)] ]

    for win_con in winning_states:
        win = True
        for coords in win_con:
            if board_state[coords[0]][coords[1]] != player:
                win = False

        if win:
            game_won = True
            print(f"{player} won!")
            board.draw_line(win_con[0], win_con[1], "black")
            board.draw_line(win_con[1], win_con[2], "black")

def main():
    win = Window(920, 1080)
    board = Board (win, on_click, 600, 600, 3, 3)

    board.draw()

    win.run_till_close()

main()