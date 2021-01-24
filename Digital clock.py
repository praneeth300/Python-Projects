#Digital clock with python

from tkinter import Label,Tk
import time

app_window=Tk()
app_window.title('Digital clock')
app_window.geometry('420x150')
app_window.resizable(1,1)

#Now i define the font of the time, color and its border

text_font=('Boulder',55,'bold')
background="#f2e750"
foreground="#363529"
border_width=25

#Now here i will combine the all elements to define the label of the clock

label=Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)

#Now let's define the main function

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock)

#Now let's run to see our digital clock
digital_clock()
app_window.mainloop()
