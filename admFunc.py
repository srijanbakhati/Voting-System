import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    umlLogo = ImageTk.PhotoImage((Image.open("img/uml.png")).resize((35,35),Image.LANCZOS))
    umlImg = Label(frame1, image=umlLogo).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/nCongress.png")).resize((25,35),Image.LANCZOS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    maoistLogo = ImageTk.PhotoImage((Image.open("img/maoist.png")).resize((25,30),Image.LANCZOS))
    maoistImg = Label(frame1, image=maoistLogo).grid(row = 4,column = 0)

    rspLogo = ImageTk.PhotoImage((Image.open("img/rsp.png")).resize((35,35),Image.LANCZOS))
    rspImg = Label(frame1, image=rspLogo).grid(row = 5,column = 0)

    raprapaLogo = ImageTk.PhotoImage((Image.open("img/raprapa.png")).resize((35,35),Image.LANCZOS))
    raprapaImg = Label(frame1, image=raprapaLogo).grid(row = 6,column = 0)


    Label(frame1, text="UML             :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['uml'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" MAOIST               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['maoist'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text=" RSP    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['rsp'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text=" Raprapa            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['raprapa'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
