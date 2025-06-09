from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Tic-Tac-Toe"
        self.__running = False
        self.__canvas = Canvas(self.__root, width=width, height=height)