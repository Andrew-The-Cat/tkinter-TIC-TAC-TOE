from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk(className="Tic-Tac-Toe")
        self.__root.wm_title("Tic-Tac-Toe")
        self.__root.resizable(False, False)
        self.__running = False
        #self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def append_canvas(self, canvas:Canvas) -> Canvas:
        canvas.master = self.__root
        return canvas
    
    def update(self):
        self.__root.update()
        self.__root.update_idletasks()

    def run_till_close(self):
        print(self.__root.title)
        self.__root.mainloop()
        '''
        self.__running = True
        while self.__running:
            self.update()
            '''

    def close(self):
        self.__running = False