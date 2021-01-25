
import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.grid_widgets()
        self.setting_widgets()

    def create_widgets(self):
        self.lblName = tk.Label()
        self.lblAddr = tk.Label()
        self.lblPNo = tk.Label()
        self.lblEmail = tk.Label()

        self.txtName = tk.Entry()
        self.txtAddr = tk.Entry()
        self.txtPNo = tk.Entry()
        self.txtEmail = tk.Entry()

        self.vName = tk.StringVar()
        self.vAddr = tk.StringVar()
        self.vPNo = tk.StringVar()
        self.vEmail = tk.StringVar()

        self.btnOK = tk.Button()
        self.btnCancel = tk.Button()
        self.btnView = tk.Button()

    def grid_widgets(self):
        self.lblName.grid(row=0, column=0)
        self.txtName.grid(row=0, column=1)

        self.lblAddr.grid(row=1, column=0)
        self.txtAddr.grid(row=1, column=1)

        self.lblPNo.grid(row=2, column=0)
        self.txtPNo.grid(row=2, column=1)

        self.lblEmail.grid(row=3, column=0)
        self.txtEmail.grid(row=3, column=1)

        self.btnOK.grid(row=4, column=0)
        self.btnCancel.grid(row=4, column=1)

    def setting_widgets(self):
        self.lblName['text'] = '성명: '
        self.lblAddr['text'] = '주소: '
        self.lblPNo['text'] = '휴대전화: '
        self.lblEmail['text'] = '이메일: '

        self.txtName['textvariable'] = self.vName
        self.txtAddr['textvariable'] = self.vAddr
        self.txtPNo['textvariable'] = self.vPNo
        self.txtEmail['textvariable'] = self.vEmail

        self.btnOK['text'] = 'OK'
        self.btnCancel['text'] = 'Cancel'
