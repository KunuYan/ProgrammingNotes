import tkinter as tk


def ev_clear():
    lHistory['text'] = eHello.get()
    eHello.delete(0, tk.END)


# create the top level window/frame
top = tk.Tk()
F = tk.Frame(top)  # this is the main frame, so it's child to Top
F.pack(fill="both")  # the main frame will fill the tk window vertically and horizontally

# Now the frame with the text entry
fEntry = tk.Frame(F, border=10, bg="green")  # this frame is child frame of and inside F
# we create a label, define how it looks inside fEntry
lHistory = tk.Label(fEntry, text="Name", foreground="steelblue", bg="white", bd=2)
# we pack the label and tell tk tool where to put it and how much space it takes inside fEntry
lHistory.pack(side="left", fill="x")  # pack is a layout manager(there are other like grid)
eHello = tk.Entry(fEntry)
eHello.pack(side="left")
# we pack fEntry
fEntry.pack(side="top", fill="x")

# Finally the frame with the buttons.
# sink this one for emphasis
fButtons = tk.Frame(F, relief="sunken", border=8)
bClear = tk.Button(fButtons, text="Clear Text", command=ev_clear)
bClear.pack(side="left", padx=5, pady=2)
bQuit = tk.Button(fButtons, text="Quit", command=F.quit)
bQuit.pack(side="left", padx=5, pady=2) # pad is to give space between the ogject
fButtons.pack(side="top", fill="x")

# Now run the event loop
F.mainloop()
