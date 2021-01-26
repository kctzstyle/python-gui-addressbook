
import tkinter as tk
import tkinter.ttk as ttk

from .db import AddressBookDAO


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.dao = AddressBookDAO()

        self.create_widgets()
        self.grid_widgets()
        self.setting_widgets()

    def create_widgets(self):
        self.trvTable = ttk.Treeview()
        self.trvScroll = ttk.Scrollbar()
        self.btnAdd = ttk.Button()
        self.btnRemove = ttk.Button()

    def grid_widgets(self):
        self.trvTable.pack(side='left')
        self.trvScroll.pack(side='right', fill='y')
        # self.lblText.pack()

    def setting_widgets(self):
        columns = self.dao.table_columns()
        self.trvTable['columns'] = [col[0]+1 for col in columns]
        self.trvTable['height'] = 5
        self.trvTable['show'] = 'headings'

        for col in columns:
            self.trvTable.heading(col[0]+1, text=col[1])
            self.trvTable.column(col[0]+1, width=100)

        self.trvScroll['orient'] = 'vertical'
        self.trvScroll['command'] = self.trvTable.yview

        self.trvTable.configure(yscrollcommand=self.trvScroll.set)

        data = self.dao.view_all()
        for v in data:
            self.trvTable.insert('', 'end', values=tuple(v))

        self.trvTable.bind('<ButtonRelease-1>', self.click_item)

    def click_item(self, event):
        selectedItem = self.trvTable.focus()
        value = self.trvTable.item(selectedItem).get('values')
        # self.lblText.configure(text=value)


# TODO: ADD 버튼 누르면 주소록 입력창 띄우도록 하기
class AddressBookApplication(tk.Frame):

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
