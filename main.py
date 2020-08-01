import os
import time
import tkinter
from tkinter import *
from tkinter import font
import threading
import pyperclip
from datetime import datetime

#Mainroot
root_main = Tk()
stop_thread = FALSE
def GUI():

    root_main.title("CopyPasteTracker")
    root_main.geometry("300x300")
    root_main.resizable(False,False)
    #root_main.iconbitmap("images\")

    b_start = Button(root_main, command = lambda: threading.Thread(target= cliptrack, args=[b_start, b_stop]).start(),
                     height =5, width=10, bg = "green",text="START\n TRACKING" )
    # b_start.place(x = 150 , y =150, anchor="center" )
    b_start.pack(pady = 30,padx=30,side=LEFT)

    b_stop = Button(root_main, command = lambda: kill_thread(b_start, b_stop), height = 5, width=10, bg="red", text="STOP\n TRACKING")
    b_stop.config(state="disabled")
    b_stop.pack(pady = 30,padx=30,side=RIGHT)

    root_main.mainloop()


def cliptrack(b,s):
    b.config(state="disabled")
    s.config(state="normal")
    global stop_thread
    stop_thread = FALSE
    tmp = ""
    if os.path.exists("Zwischenablage.txt")== True:
            f = open("Zwischenablage.txt","r+")
            f.truncate(0)

    while  stop_thread == FALSE:
        data = pyperclip.paste()
        if data != None and data !=tmp:


            track_list = open("Zwischenablage.txt", "a+")
            now = datetime.now()
            tmp = data
            track_list.write(now.strftime("%H:%M:%S")+ " ::: " + data+"\n")
            track_list.close()

def kill_thread(b, s):
    b.config(state="normal")
    s.config(state="disabled")
    global stop_thread
    stop_thread = TRUE
def file_write():

    f = open("text.txt","a+" )
    f.write("This is new text\n")
    f.close()


if __name__ == '__main__':
    t = threading.Thread(target= cliptrack, args=[True])
    GUI()

