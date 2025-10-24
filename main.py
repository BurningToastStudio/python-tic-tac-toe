# Max Martin
# Python Tic Tac Toe Using Tkinter

#region Imports
import tkinter as tk
#endregion

#region Window Setup
root = tk.Tk()
root.geometry("400x400")
root.title("Tic Tac Toe")
root.resizable(False, False)
#endregion

#region Constants
PLAYER_ICON_1 = "X"
PLAYER_ICON_2 = "O"

CELL_FONT = "Arial", 50
CELL_WIDTH = 3
CELL_HEIGHT = 1
#endregion

#dictionary of cells
#tuple contains text, row, collum
cells = {
    0: ("", 0, 0), 1: ("", 0, 1), 2: ("", 0, 2),
    3: ("", 1, 0), 4: ("", 1, 1), 5: ("", 1, 2),
    6: ("", 2, 0), 7: ("", 2, 1), 8: ("", 2, 2),
}

def cell_clicked(cell):
    pass

#region Setup UI

# create frame to store the buttons
board_frame = tk.Frame(root)
# relx / rely is relative x and relative y (relative to window size)
# 0 - 1 is from edge to edge
# using 0.5 makes it centered
board_frame.place(relx=0.5, rely=0.5, anchor="center")  # center the frame

# loop through all cells in cells dictionary
# .items lets you iterate the key and values
for cell, (text, row, collum) in cells.items():
    cell_button = tk.Button (
        board_frame,
        text=text,
        font=CELL_FONT,
        width=CELL_WIDTH,
        height=CELL_HEIGHT,
        command=lambda: cell_clicked(cell)
    )
    cell_button.grid(row=row, column=collum, sticky=tk.NSEW)
#endregion

tk.mainloop()