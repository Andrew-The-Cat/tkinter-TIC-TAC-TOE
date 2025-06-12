from lib.window import *
from lib.board_obj import Board_Object
from lib.draw import Line, Point

class Cell:
    def __init__(self, length, height, x, y, child = None):
        self.length = length
        self.height = height
        self.x = x
        self.y = y
        self.__child = child

    def draw(self, canvas:Canvas, fill):
        canvas.create_rectangle(self.x, self.y, self.x + self.length, self.y + self.height, fill=fill)
        if self.__child != None:
            self.__child.draw(canvas)

    def assign_child(self, child:Board_Object):
        self.__child = child

class Board:
    def __init__(self, win:Window, on_click, width, height, num_rows, num_cols, thickness = 2):
        self.width = width
        self.height = height
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size = num_rows * num_cols
        self.__thickness = thickness
        self.col_size = width / num_cols
        self.row_size = height / num_rows
        self.__board = [ [  ] ]

        def click_wrapper(event):
            cell_x = int(event.y // self.col_size)
            cell_y = int(event.x // self.row_size)

            on_click(self, self.__board[cell_x][cell_y], int(cell_x), int(cell_y))

        self.__win = win
        self.__canvas = Canvas(width=width, height=height, background="gray30")
        self.__canvas.bind('<Button-1>', click_wrapper)
        self.__win.append_canvas(self.__canvas)
        self.__canvas.pack(anchor="nw", expand=False)
        
        self.reset_board()

    def reset_board(self):
        self.__board = [
            [ Cell( self.col_size, self.row_size, self.col_size * _, self.row_size * x ) for _ in range(self.num_cols) ] for x in range (self.num_rows)
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

    def draw_cell(self, i, j):
        cnt = i + j
        cell:Cell = self.__board[i][j]

        if cnt % 2 == 0:
            cell.draw(self.__canvas, fill="tan4")
        else:
            cell.draw(self.__canvas, fill="wheat")

    def draw_line(self, x1, y1, x2, y2, fill="black"):
        cell1:Cell = self.__board[x1][y1]
        cell2:Cell = self.__board[x2][y2]

        real_x1 = cell1.x + cell1.height // 2
        real_y1 = cell1.y + cell1.length // 2

        real_x2 = cell2.x + cell2.height // 2
        real_y2 = cell2.y + cell2.length // 2

        self.__canvas.create_line(real_x1, real_y1, real_x2, real_y2, fill=fill)

    def draw_line(self, tup1:tuple, tup2:tuple, fill="black"):
        cell1:Cell = self.__board[tup1[0]][tup1[1]]
        cell2:Cell = self.__board[tup2[0]][tup2[1]]

        real_x1 = cell1.x + cell1.height // 2
        real_y1 = cell1.y + cell1.length // 2

        real_x2 = cell2.x + cell2.height // 2
        real_y2 = cell2.y + cell2.length // 2

        self.__canvas.create_line(real_x1, real_y1, real_x2, real_y2, fill=fill, width=20)

    def update_cell(self, i, j, child:Board_Object):
        cell:Cell = self.__board[i][j]

        if child != None:
            cell.assign_child(child)
