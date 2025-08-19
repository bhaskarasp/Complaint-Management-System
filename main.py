from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from db import DBConnect
from listComp import ListComp

# Config
conn = DBConnect()
root = Tk()
root.geometry('700x500')
root.title('Complaint Management System')

# Set background color
root.configure(background='#F0F0F0')

# Style
style = Style()
style.theme_use('clam')
style.configure('TFrame', background='#F0F0F0')
style.configure('TLabel', background='#F0F0F0', font=('Helvetica', 14))
style.configure('TButton', background='#4CAF50', foreground='white', font=('Helvetica', 12), padding=10)
style.map('TButton', background=[('active', '#45A049')])
style.configure('TText', font=('Helvetica', 12))

# Header
header = Label(root, text='Complaint Management System', font=('Helvetica', 20, 'bold'), background='#F0F0F0')
header.pack(pady=20)

# Frame for input fields
input_frame = Frame(root, padding=10, relief='groove', borderwidth=2)
input_frame.pack(pady=10)

# Labels and Entries
labels = ['Full Name:', 'Gender:', 'Comment:']
for i in range(3):
    Label(input_frame, text=labels[i]).grid(row=i, column=0, padx=10, pady=10, sticky=W)

fullname = Entry(input_frame, width=40, font=('Helvetica', 14))
fullname.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

SpanGender = StringVar()
Radiobutton(input_frame, text='Male', value='male', variable=SpanGender).grid(row=1, column=1, padx=5)
Radiobutton(input_frame, text='Female', value='female', variable=SpanGender).grid(row=1, column=2, padx=5)

# Text area for comments with scrollbar
comment_frame = Frame(input_frame)
comment_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

comment = Text(comment_frame, width=40, height=5, font=('Helvetica', 12))
comment.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(comment_frame, command=comment.yview)
scrollbar.pack(side=RIGHT, fill=Y)
comment.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

BuList = Button(button_frame, text='List Complaints')
BuList.grid(row=0, column=1, padx=10)

BuSubmit = Button(button_frame, text='Submit Now')
BuSubmit.grid(row=0, column=2, padx=10)

# Functionality
def SaveData():
    msg = conn.Add(fullname.get(), SpanGender.get(), comment.get(1.0, 'end'))
    fullname.delete(0, 'end')
    comment.delete(1.0, 'end')
    showinfo(title='Add Info', message=msg)

def ShowList():
    listrequest = ListComp()

BuSubmit.config(command=SaveData)
BuList.config(command=ShowList)


root.mainloop()
