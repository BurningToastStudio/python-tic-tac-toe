# Max Martin - Y10CSC
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
PLAYER_1 = "X"
PLAYER_2 = "O"

CELL_FONT = "Arial", 50
CELL_WIDTH = 3
CELL_HEIGHT = 1
#endregion

#region Globals

# store the current players icon
player_to_move = PLAYER_1
#endregion

def cell_clicked(cell_number):
    cell_objects[cell_number].config(state=tk.DISABLED) # make it not clickable
    cell_objects[cell_number].config(text = player_to_move) # replace text with the players icon
    if not win_check(): # check if no one has won yet
        next_player() # after making a move, the next player moves
    else: # someone has won
        print("GAME OVER")


def win_check():
    # 1 2 3
    # 4 5 6
    # 7 8 9

    # check if there are 3 in a row that are THE SAME and NOT blank
    # .cget gets the config data

    # ROWS
    if cell_objects[1].cget("text") == cell_objects[2].cget("text") == cell_objects[3].cget("text") != "":
        return True
    if cell_objects[4].cget("text") == cell_objects[5].cget("text") == cell_objects[6].cget("text") != "":
        return True
    if cell_objects[7].cget("text") == cell_objects[8].cget("text") == cell_objects[9].cget("text") != "":
        return True

    # COLUMNS
    if cell_objects[1].cget("text") == cell_objects[4].cget("text") == cell_objects[7].cget("text") != "":
        return True
    if cell_objects[2].cget("text") == cell_objects[5].cget("text") == cell_objects[8].cget("text") != "":
        return True
    if cell_objects[3].cget("text") == cell_objects[6].cget("text") == cell_objects[9].cget("text") != "":
        return True

    # DIAGONALS
    if cell_objects[1].cget("text") == cell_objects[5].cget("text") == cell_objects[9].cget("text") != "":
        return True
    if cell_objects[3].cget("text") == cell_objects[5].cget("text") == cell_objects[7].cget("text") != "":
        return True

    return False


def next_player():
    global player_to_move
    if player_to_move == PLAYER_1:
        player_to_move = PLAYER_2
    else:
        player_to_move = PLAYER_1


#region Setup UI


# create frame to store the buttons
board_frame = tk.Frame(root)
# relx / rely is relative x and relative y (relative to window size)
# 0 - 1 is from edge to edge
# using 0.5 makes it centered
board_frame.place(relx=0.5, rely=0.5, anchor="center")  # center the frame

# dictionary of cell for init position on the grid
# tuple contains text, row, collum
cells_button_initialization = {
    1: ("", 0, 0), 2: ("", 0, 1), 3: ("", 0, 2),
    4: ("", 1, 0), 5: ("", 1, 1), 6: ("", 1, 2),
    7: ("", 2, 0), 8: ("", 2, 1), 9: ("", 2, 2),
}

# make empty dict to store a reference to the cells
cell_objects = {}

# loop through all cells in dictionary
# .items lets you iterate the key and values
for cell, (text, row, collum) in cells_button_initialization.items():
    cell_button = tk.Button (
        board_frame, # put inside frame so it can then be centered
        text=text,
        font=CELL_FONT,
        width=CELL_WIDTH,
        height=CELL_HEIGHT,
        # need to use c in parameters, or it won't be correct
        # I think its called "late binding"
        command=lambda c=cell: cell_clicked(c)  # will call this function when clicked
    )
    # place on the grid (will be aligned together inside the frame)
    cell_button.grid(row=row, column=collum, sticky=tk.NSEW)
    cell_objects[cell] = cell_button # save the reference (starts at 1)
#endregion

tk.mainloop()