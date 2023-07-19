from time import strftime
from tkinter import Label, Tk

#Configuring window
window = Tk()
window.title("Digital Clock using Python")
window.geometry("350x150")
 #Background of the clock
window.configure(bg="black") 
#setting a fixed window size 
window.resizable(True, True)  

clock_label = Label(
    window, bg="black", fg="green", font=("Arial", 40, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)
def update_label():
    """
    This function will update the clock every 80 milliseconds
    """
    current_time = strftime("%H: %M: %S %p\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")
update_label()
window.mainloop()