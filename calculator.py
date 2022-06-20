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

#now im going to create a window
window=tk.Tk()
window.geometry("300x300")
field=tk.Text(window,height=2,width=25,font=("Times New Roman",20))
field.grid(row=1,column=1,columnspan=4)
window.mainloop()

