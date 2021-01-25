
import tkinter as tk

from addressbook.app import Application


if __name__ == '__main__':
    root = tk.Tk()
    root.title('주소록')

    app = Application(master=root)
    app.mainloop()
