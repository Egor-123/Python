from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Крестики-нолики')
root.minsize(200, 200)


class TicTacToe:
    X = 1
    O = 2

    PLAYER_1 = 'X'
    PLAYER_2 = 'O'

    current_player = PLAYER_1
    cells_data = [0, 0, 0,
                  0, 0, 0,
                  0, 0, 0]

    def clear_data(self, btns):
        self.cells_data = [0, 0, 0,
                           0, 0, 0,
                           0, 0, 0]
        self.current_player = self.PLAYER_1

        for button in btns:
            button.config(text='')

    def is_win(self):
        d = self.cells_data

        if d[0] == d[1] == d[2] != 0:
            return True
        elif d[3] == d[4] == d[5] != 0:
            return True
        elif d[6] == d[7] == d[8] != 0:
            return True
        elif d[0] == d[3] == d[6] != 0:
            return True
        elif d[1] == d[4] == d[7] != 0:
            return True
        elif d[2] == d[5] == d[8] != 0:
            return True
        elif d[0] == d[4] == d[8] != 0:
            return True
        elif d[2] == d[4] == d[6] != 0:
            return True
        else:
            return False

    def change_player(self):
        if self.current_player == self.PLAYER_1:
            self.current_player = self.PLAYER_2
            return self.PLAYER_1
        else:
            self.current_player = self.PLAYER_1
            return self.PLAYER_2

    def set_cells_data(self, num):
        cell_value = self.get_cell_value()

        if num >= 0 or num <= 8:
            if self.cells_data[num] != 0:
                return False

            self.cells_data[num] = cell_value
            return True

        return False

    def get_cell_value(self):
        if self.current_player == self.PLAYER_1:
            return self.X
        else:
            return self.O


def click(btn, num):
    is_set_cells_data = tic_tac_toe.set_cells_data(num)

    if not is_set_cells_data:
        return

    text = tic_tac_toe.change_player()
    btn.config(text=text)

    is_win = tic_tac_toe.is_win()

    if is_win:
        is_new_game = messagebox.askyesno(title='Играть еще раз?', message='Победили ' + text)

        if is_new_game:
            tic_tac_toe.clear_data(buttons)
        else:
            root.destroy()


btn_w = 10
btn_h = 5

tic_tac_toe = TicTacToe()

button_1 = Button(width=btn_w, height=btn_h, command=lambda: click(button_1, 0))
button_2 = Button(width=btn_w, height=btn_h, command=lambda: click(button_2, 1))
button_3 = Button(width=btn_w, height=btn_h, command=lambda: click(button_3, 2))
button_4 = Button(width=btn_w, height=btn_h, command=lambda: click(button_4, 3))
button_5 = Button(width=btn_w, height=btn_h, command=lambda: click(button_5, 4))
button_6 = Button(width=btn_w, height=btn_h, command=lambda: click(button_6, 5))
button_7 = Button(width=btn_w, height=btn_h, command=lambda: click(button_7, 6))
button_8 = Button(width=btn_w, height=btn_h, command=lambda: click(button_8, 7))
button_9 = Button(width=btn_w, height=btn_h, command=lambda: click(button_9, 8))

buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

root.mainloop()
