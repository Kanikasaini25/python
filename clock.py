
from time import strftime
from tkinter import Label,Tk
window= Tk()
window.title("digital clock")
window.resizable(False,False)

clock_label=Label(window,font=("Times",30),background="white",foreground="red")
clock_label.place(x=0,y=40)
def update_label():
    current_time=strftime('%H:%M:%S%p')
    clock_label.configure( text=current_time)
    clock_label.after(1000,update_label)
    

update_label()
window.mainloop()



                    
