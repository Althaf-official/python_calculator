import tkinter as tk
#for the display
feild_text=""

#when we click the function it will show the numbers .so we will define now
def add_to_field(sth):
    global feild_text
    #so now we will make the  sth as a string and we will update the feild text
    feild_text=feild_text+str(sth)