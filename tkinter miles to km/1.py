import tkinter
window = tkinter.Tk()
window.title("TKINTER")
window.minsize()

def calculate():
    km = int(entry.get()) * 1.609
    my_label2.config(text=f"{entry.get()} miles equal to {round(km,2)} kilometers")


my_label1 = tkinter.Label(text="MILES TO KILOMETER CALCULATOR", font=(24))
my_label1.grid(row = 0,column = 0, columnspan=2)

entry = tkinter.Entry()
entry.grid(row = 1,column = 0)

button = tkinter.Button(text="button", command=calculate)
button.grid(row = 2,column = 0)

my_label2=tkinter.Label()
my_label2.grid(row=3,column=0)

window.mainloop()

