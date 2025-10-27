# Max Martin - Y10CSC
# Python Tic Tac Toe Using Tkinter

#region Imports
import tkinter as tk
from time import sleep

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

BUTTON_BG = "white"       # background for normal cells
BUTTON_BG_WON = "green"   # background for winning cells
#endregion

#region Globals

# store the current players icon
player_to_move = PLAYER_1

winning_cells = [] # list will store the cells that are 3 in a row

#endregion

# when game ends, reset the game
def reset_game():
    global player_to_move
    player_to_move = PLAYER_1 # reset player

    for cell in cell_objects:
        cell_objects[cell].config(state=tk.NORMAL) # enable all buttons
        cell_objects[cell].config(text = "") # reset text on all buttons
        cell_objects[cell].config(bg = BUTTON_BG) # change colour back to default

def cell_clicked(cell_number):
    cell_objects[cell_number].config(state=tk.DISABLED) # make it not clickable
    cell_objects[cell_number].config(text=player_to_move)

    if game_won_check(): # has someone won?
        for cell in cell_objects:
            # stop interaction with the buttons until the game is reset
            cell_objects[cell].config(state = tk.DISABLED)
        game_won_logic()  # do win logic

    elif game_drawn_check(): # is it a draw
        print("DRAW")
        reset_game() # reset game state

    else: # continue as normal
        next_player_turn()  # after making a move, the next player can move

def game_won_logic():
    for cell in winning_cells: # loop all winning cells
        cell.config(bg = BUTTON_BG_WON) # change color

    # when using tkinter i found "sleep(1)" dosent work because it freezes the GUI

    # root.after schedules the function "reset_game" to run after some milliseconds
    # this dosnt freeze the UI :)
    root.after(1000, reset_game)

def game_won_check():
    global winning_cells
    # check if there are 3 in a row that are THE SAME and NOT blank
    # .cget gets the config data
    # if won, set the winning cells

    # ROWS
    if cell_objects[1].cget("text") == cell_objects[2].cget("text") == cell_objects[3].cget("text") != "":
        winning_cells = [cell_objects[1], cell_objects[2], cell_objects[3]]
        return True
    if cell_objects[4].cget("text") == cell_objects[5].cget("text") == cell_objects[6].cget("text") != "":
        winning_cells = [cell_objects[4], cell_objects[5], cell_objects[6]]
        return True
    if cell_objects[7].cget("text") == cell_objects[8].cget("text") == cell_objects[9].cget("text") != "":
        winning_cells = [cell_objects[7], cell_objects[8], cell_objects[9]]
        return True

    # COLUMNS
    if cell_objects[1].cget("text") == cell_objects[4].cget("text") == cell_objects[7].cget("text") != "":
        winning_cells = [cell_objects[1], cell_objects[4], cell_objects[7]]
        return True
    if cell_objects[2].cget("text") == cell_objects[5].cget("text") == cell_objects[8].cget("text") != "":
        winning_cells = [cell_objects[2], cell_objects[5], cell_objects[8]]
        return True
    if cell_objects[3].cget("text") == cell_objects[6].cget("text") == cell_objects[9].cget("text") != "":
        winning_cells = [cell_objects[3], cell_objects[6], cell_objects[9]]
        return True

    # DIAGONALS
    if cell_objects[1].cget("text") == cell_objects[5].cget("text") == cell_objects[9].cget("text") != "":
        winning_cells = [cell_objects[1], cell_objects[5], cell_objects[9]]
        return True
    if cell_objects[3].cget("text") == cell_objects[5].cget("text") == cell_objects[7].cget("text") != "":
        winning_cells = [cell_objects[3], cell_objects[5], cell_objects[7]]
        return True

    return False

def game_drawn_check():
    # loop through all cells
    for cell in cell_objects:
        # if here is a blank cell, the game can continue
        if cell_objects[cell].cget("text") == "":
            return False
    # if all cells are full, it is a draw, ensure to run AFTER win_check
    return True

def next_player_turn():
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

# make empty dict to keep a reference to all the buttons
# do this so the config of buttons can be modified
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
        bg = BUTTON_BG,
        # need to use c in parameters, or it won't be correct
        # I think its called "late binding" or somthing
        command=lambda c=cell: cell_clicked(c)  # will call this function when clicked
    )
    # place on the grid (will be aligned together inside the frame)
    cell_button.grid(row=row, column=collum, sticky=tk.NSEW)
    cell_objects[cell] = cell_button # save the reference (starts at 1)
#endregion

tk.mainloop()