from lib.window import *
from lib.tk_board import *
def main():
    win = Window(920, 1080)
    board = Board (win, 720, 480, 3, 3)
    board.draw()

    win.run_till_close()

main()