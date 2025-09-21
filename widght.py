from tinker import*
from date import date

window = Tk()
window.title('getting strated Widgets')
window.gometry('400x300')

lbl = Label(text="Hey There!", fg="white", bg="#07F5F", height=1, width=300)
name_lbl = Label(text= "Full Name", bg="3895D3")
name_entry = Entry()

def display():

    

    global message
    message = "Welcome to the Application! \n todays date is: "

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)
    btn = Button(text="Begin", comand=display, height=1, bg="#1261A0", fg='white')

