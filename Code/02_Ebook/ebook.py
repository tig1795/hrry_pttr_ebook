import tkinter as tk
from glob import glob


class Notepad:
    fullscreen = False

    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("My notepad")
        self.root['bg'] = "coral"
        self.frame1 = tk.Frame(self.root)
        self.frame1['bg'] = "coral"
        self.frame1.pack(side="left", fill=tk.Y)
        self.lb = tk.Listbox(self.frame1, width=50)
        self.lb.pack(fill=tk.Y, expand=1)
        for file in glob("*.txt"):
            self.lb.insert(tk.END, file)
        self.text = tk.Text(self.root, width=70)
        self.text.pack(fill=tk.BOTH, expand=1)
        self.root.bind("<F11>", lambda x: self.toggle_fullscreen())
        self.lb.bind("<Double-Button>", lambda x: self.show_text())

    def show_text(self):
        num_item = self.lb.curselection()  # the index of item selected
        fname = self.lb.get(num_item)  # the file name selected
        with open(fname) as file:
            self.text.delete("1.0", tk.END)
            file = file.read()
            self.text.insert(tk.END, file)

    def toggle_fullscreen(self):
        if Notepad.fullscreen == False:
            self.root.attributes("-fullscreen", True)
            Notepad.fullscreen = True
        else:
            self.root.attributes("-fullscreen", False)
            Notepad.fullscreen = False


root = tk.Tk()  # creates a window
app = Notepad(root)
root.mainloop()