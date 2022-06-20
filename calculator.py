import tkinter as tk
#for the display
feild_text=""

#when we click the function it will show the numbers .so we will define now
def add_to_field(sth):
    global feild_text
    #so now we will make the  sth as a string and we will update the feild text
    feild_text=feild_text+str(sth)
    field.delete("1.0","end")
    field.insert("1.0",feild_text)
def calculate():#when we click the "=" button should calculate the result
    global feild_text
    result=str(eval(feild_text))
    field.delete("1.0", "end")
    field.insert("1.0",result)
def clear():
    global feild_text
    feild_text=""
    field.delete("1.0","end")




#now im going to create a window
window=tk.Tk()
window.geometry("300x300")
field=tk.Text(window,height=2,width=20,font=("Times New Roman",20))
field.grid(row=1,column=1,columnspan=4)
#number button
btn_1=tk.Button(window,text="1",command=lambda: add_to_field(1),width=5,font=("Times New Roman",14))
btn_1.grid(row=4,column=1)

btn_2=tk.Button(window,text="2",command=lambda: add_to_field(2),width=5,font=("Times New Roman",14))
btn_2.grid(row=4,column=2)

btn_3=tk.Button(window,text="3",command=lambda: add_to_field(3),width=5,font=("Times New Roman",14))
btn_3.grid(row=4,column=3)

btn_4=tk.Button(window,text="4",command=lambda: add_to_field(4),width=5,font=("Times New Roman",14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(window,text="5",command=lambda: add_to_field(5),width=5,font=("Times New Roman",14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(window,text="6",command=lambda: add_to_field(6),width=5,font=("Times New Roman",14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(window,text="7",command=lambda: add_to_field(7),width=5,font=("Times New Roman",14))
btn_7.grid(row=2,column=1)

btn_8=tk.Button(window,text="8",command=lambda: add_to_field(8),width=5,font=("Times New Roman",14))
btn_8.grid(row=2,column=2)

btn_9=tk.Button(window,text="9",command=lambda: add_to_field(9),width=5,font=("Times New Roman",14))
btn_9.grid(row=2,column=3)

btn_0=tk.Button(window,text="0",command=lambda: add_to_field(0),width=5,font=("Times New Roman",14))
btn_0.grid(row=5,column=1)

window.mainloop()

