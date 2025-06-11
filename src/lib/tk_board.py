from lib.window import *

class Cell:
    def __init__(self, length, height, x, y, child = None):
        self.__length = length
        self.__height = height
        self.__x = x
        self.__y = y
        self.__child = child

    def draw(self, canvas:Canvas, fill):
        canvas.create_rectangle(self.__x, self.__y, self.__x + self.__length, self.__y + self.__height, fill=fill)

class Board:
    def __init__(self, win:Window, width, height, num_rows, num_cols, thickness = 2):
        self.width = width
        self.height = height
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size = num_rows * num_cols
        self.__thickness = thickness
        self.__col_size = width / num_cols
        self.__row_size = height / num_rows
        self.__board = [ [  ] ]
        self.__win = win
        self.__canvas = Canvas(width=width, height=height, background="gray30")
        self.__win.append_canvas(self.__canvas)
        self.__canvas.pack(anchor="nw", expand=True, fill=BOTH)


        self.__reset_board()

    def __reset_board(self):
        self.__board = [
            [ Cell( self.__col_size, self.__row_size, self.__col_size * _, self.__row_size * x ) for _ in range(self.num_cols) ] for x in range (self.num_rows)
        ]

    def draw(self):
        cnt = 0
        for row in self.__board:
            for col in row:
                cnt += 1
                if cnt % 2 == 0:
                    col.draw(self.__canvas, fill="tan4")
                else:
                    col.draw(self.__canvas, fill="wheat")