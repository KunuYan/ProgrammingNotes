import tkinter as tk
import tkinter.messagebox as mb
import ttc_logic

top = tk.Tk()
top.title("Tic-Tac-Toe")


# tk menus are built like
def build_menu(parent):
    menus = (
        ("File", (("New", ev_new),
                  ("Resume", ev_resume),
                  ("Save", ev_save),
                  ("Exit", ev_exit))),
        ("Help", (("Help", ev_help),
                  ("About", ev_about)))
    )
    # you first define the menubar
    menubar = tk.Menu(parent)
    for menu in menus:
        #  add a menu and it's command (we can add more submenus also)
        m = tk.Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
        # add a menu name and it's submenu's
        menubar.add_cascade(label=menu[0], menu=m)
    return menubar


def ev_new():
    status['text'] = "Playing game"
    game2cells(ttc_logic.newGame())


def ev_resume():
    status['text'] = "Playing game"
    game = ttc_logic.restoreGame()
    game2cells(game)


def ev_save():
    game = cells2game()
    ttc_logic.saveGame(game)


def ev_exit():
    if status['text'] == "Playing game":
        if mb.askyesno("Quitting",
                       "Do you want to save the game before quitting?"):
            ev_save()
    top.quit()


def ev_help():
    mb.showinfo("Help", '''
    File‐>New: starts a new game of tic‐tac‐toe
    File‐>Resume: restores the last saved game and commences play
    File‐>Save: Saves current game.
    File‐>Exit: quits, prompts to save active game
    Help‐>Help: shows this page
    Help‐>About: Shows information about the program and author''')


def ev_about():
    mb.showinfo("About", "Tic‐tac‐toe game GUI")


def ev_click(row, col):
    mb.showinfo("Cell clicked", "row:{}, col:{}".format(row, col))


# ----- Building the board -----------
def build_board(parent):
    outer = tk.Frame(parent, border=2, relief="sunken")
    inner = tk.Frame(outer)
    inner.pack()

    for row in range(3):
        for col in range(3):
            cell = tk.Button(inner, text=" ", width="5", height="2",
                             command=lambda r=row, c=col: ev_click(r, c))
            cell.grid(row=row, column=col)
    return outer


# ----- game mechanics -----
def ev_click(row, col):
    if status['text'] == "Game over":
        mb.showerror("Game over", "Game over!")
        return
    game = cells2game()
    index = (3*row) + col
    result = ttc_logic.userMove(game, index)
    game2cells(game)

    if not result:
        result = ttc_logic.computerMove(game)
        game2cells(game)

    if result == "D":
        mb.showinfo("Result", "It's a Draw!")
        status['text'] = "Game over"

    else:
        if result == "X" or result == "O":
            mb.showinfo("Result", "The winner is: {}".format(result))
            status['text'] = "Game over"


def game2cells(game):
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            table.grid_slaves(row=row, column=col)[0]['text'] = game[3*row+col]


def cells2game():
    values = []
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            values.append(table.grid_slaves(row=row, column=col)[0]['text'])
    return values


mbar = build_menu(top)
top["menu"] = mbar

board = build_board(top)
board.pack()
status = tk.Label(top, text="testing", border=0,
                  background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

top.mainloop()
