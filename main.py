import os
import time
import tkinter
import webbrowser
from tkinter import *
from tkinter import font
import threading
import pyperclip
from datetime import datetime

#Mainroot
root_main = Tk()
stop_thread = FALSE
#Main GUI function
def GUI():

    #Window Config
    root_main.title("CopyPasteTracker")
    root_main.geometry("285x500")
    root_main.resizable(False,False)
    root_main.config(background="#BDEBD4")
    #root_main.iconbitmap("images\")

    #START Button
    b_start = Button(root_main, command = lambda: threading.Thread(target= cliptrack, args=[b_start, b_stop, track_listbox]).start(),
                     height =5, width=10, bg = "green",text="START\n TRACKING",
                     activebackground = "#9BFA92", activeforeground="white", borderwidth=4 )
    b_start.grid(row=1, column=1,padx = 30,pady = 30)


    #STOP button
    b_stop = Button(root_main, command = lambda: kill_thread(b_start, b_stop), height = 5, width=10, bg="#FC7B7B",
                    text="STOP\n TRACKING", relief="sunken",borderwidth=4)
    b_stop.config(state="disabled")
    b_stop.grid(row=1, column=2,padx = 30,pady = 30)

    # Create Frame
    my_frame = Frame(root_main)
    #Dispaly Frame
    my_frame.grid(row=2, column=1, columnspan=2)

    #Create Scrollbar
    scrollbar = Scrollbar(my_frame, orient=HORIZONTAL)
    scrollbar.pack(side=BOTTOM, fill=X)

    #Create Listbox
    track_listbox = Listbox(my_frame, width=40, xscrollcommand= scrollbar.set)
    track_listbox.pack()




    track_listbox.config(yscrollcommand=scrollbar.set)
    #Configure scrollbar
    scrollbar.config(command = track_listbox.xview)
    #Create Exit button
    b_exit = Button(root_main, command=lambda: exit(b_start, b_stop), height=1, width=10, bg="gray",
                    text="EXIT", activebackground="#DADCDB", activeforeground="white")
    b_exit.grid(row=3, column=1, columnspan=2, pady=20)

    # Creator Textlabel with Hyperlink to Github of Creator
    creator = Label(root_main, text="Created by RibelH", fg="blue", bg="#BDEBD4")
    f = font.Font(creator, creator.cget("font"))
    f.configure(underline=True)
    creator.configure(font=f)
    creator.bind("<Button-1>", open_github)
    creator.grid(row=4, column=1,  columnspan=2)


    root_main.mainloop()

#Function tracks clipboard and writes txt file
def cliptrack(b,s,l):
    l.delete(0,"end")
    b.config (state="disabled", bg="#9BFA92", fg="white", relief="sunken")
    s.config (state="normal", bg= "red", fg="black", relief ="raised")
    global stop_thread
    stop_thread = FALSE
    tmp = ""
    # if os.path.exists("Zwischenablage.txt")== True:
    #         f = open("Zwischenablage.txt","r+")
    #         f.truncate(0)
    i = 0
    while  stop_thread == FALSE:

        data = pyperclip.paste()
        if data != None and data !=tmp:
            i = i +1


            # track_list = open("Zwischenablage.txt", "a+")
            now = datetime.now()
            tmp = data
            l.insert(i,now.strftime("%H:%M:%S")+ " ::: " + data+"\n" )
            # track_list.write(now.strftime("%H:%M:%S")+ " ::: " + data+"\n")
            # track_list.close()

def kill_thread(b, s):
    b.config(state="normal", bg = "green", fg="black", relief="raised")
    s.config(state="disabled", bg="#FC7B7B", fg ="white", relief ="sunken")
    global stop_thread
    stop_thread = TRUE
def exit(b,s):
    kill_thread(b,s)
    sys.exit()


# def file_write():
#
#     f = open("text.txt","a+" )
#     f.write("This is new text\n")
#     f.close()

#Open GIT-Hub of creator
def open_github(event):
    webbrowser.open("https://github.com/RibelH/CopyPasteTracker")

#START PROGRAM
if __name__ == '__main__':
    t = threading.Thread(target= cliptrack, args=[True])
    GUI()

