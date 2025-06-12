from lib.board import Canvas

class Board_Object:
    def __init__(self, x_padding, y_padding, cell):
        self.__x1 = cell.__x + x_padding
        self.__y1 = cell.__y + y_padding
        self.__x2 = cell.__x + cell.length - x_padding
        self.__y2 = cell.__y + cell.height - y_padding

    def draw(self, canvas:Canvas):
        raise Exception("method must be overriden on child classes of this class")