from tkinter import *

def calc():
    print("Calculating")
    miles = input.get()
    km = int(miles) * 1.609
    answer.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)


#Label

my_label = Label(text="is equal to", font=("Arial", 14),)
my_label.grid(column=0, row=1)
my_label.config(padx=10,pady=10)


#Label2

Miles_label = Label(text="Miles")
Miles_label.grid(column=2, row=0)



#Label3

Km_label = Label(text="Km")
Km_label.grid(column=2, row=1)

#Label4 (answer)

answer = Label(text="0")
answer.grid(column=1, row=1)


# Button 1

button = Button(text="calculate", command=calc)
button.grid(column=1, row=3)




# Entry

input = Entry(width=10)
input.grid(column=1, row=0)









window.mainloop()