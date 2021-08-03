import tkinter as tk
import glob


class Ebook:
    fullscreen = False

    def __init__(self, root):
        """Define window for the app"""
        self.root = root
        self.root.geometry("600x400")
        self.root['bg'] = "white"
        self.left_menu()
        self.editor()
        self.root.bind("<F11>", lambda x: self.toggle_fullscreen())

    # Widgets on the left =====================|
    def left_menu(self):
        """List of files in the folder"""
        self.frame1 = tk.Frame(self.root)
        self.frame1["bg"] = "black"
        self.frame1.pack(side='left', fill=tk.Y)
        self.button = tk.Button(self.frame1, text="Save", command=self.save)
        self.lstb = tk.Listbox(self.frame1, width=50)
        self.button.pack()
        self.lstb['bg'] = "black"
        self.lstb['fg'] = "gold"
        self.lstb.pack(fill=tk.Y, expand=1)
        self.insert_files()
        self.lstb.bind("<<ListboxSelect>>", lambda x: self.show_text())

    def show_text(self):
        """Shows text of selected file"""
        if not self.lstb.curselection() == ():  #when you have selected an item
            noi = self.lstb.curselection()[0]
            self.filename = self.lstb.get(noi)
            fn = self.opentext(self.filename)
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, fn)

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(self.text.get("1.0", tk.END))

    def editor(self):
        self.text = tk.Text(self.root)
        self.text['bg'] = "white"
        self.text['fg'] = "black"
        self.text['font'] = "Arial 12"
        self.text.pack(fill=tk.BOTH, expand=1)

    def insert_files(self):
        """Insert file names in the list on the left"""
        files = glob.glob("*.txt")
        for file in files:
            self.lstb.insert(tk.END, file)

    def opentext(self, fname):
        with open(fname) as file:
            file = file.read()
        return file

    def toggle_fullscreen(self):
        if Ebook.fullscreen == False:
            self.root.attributes("-fullscreen", True)
            Ebook.fullscreen = True
        else:
            self.root.attributes("-fullscreen", False)
            Ebook.fullscreen = False


root = tk.Tk()  # creates a window
app = Ebook(root)
app.root.title("Ebook maker")
root.mainloop()