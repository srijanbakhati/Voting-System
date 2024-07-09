import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "UML\n\nKP Sharma Oli", variable = vote, value = "uml", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"uml",client_socket)).grid(row = 2,column = 1)
    umlLogo = ImageTk.PhotoImage((Image.open("img/uml.png")).resize((35,35),Image.LANCZOS))
    umlImg = Label(frame1, image=umlLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Congress\n\nSher Bahadur Deuba", variable = vote, value = "cong", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"cong",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/nCongress.png")).resize((25,35),Image.LANCZOS))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Maoist\n\nPuspa kamal Dahal", variable = vote, value = "maoist", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"maoist",client_socket) ).grid(row = 4,column = 1)
    maoistLogo = ImageTk.PhotoImage((Image.open("img/maoist.png")).resize((25,30),Image.LANCZOS))
    maoistImg = Label(frame1, image=maoistLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "RSP\n\nRavi lamachine", variable = vote, value = "rsp", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"rsp",client_socket)).grid(row = 5,column = 1)
    rspLogo = ImageTk.PhotoImage((Image.open("img/rsp.png")).resize((35,35),Image.LANCZOS))
    rspImg = Label(frame1, image=rspLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nRaprapa    \n  ", variable = vote, value = "raprapa", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"raprapa",client_socket)).grid(row = 6,column = 1)
    raprapaLogo = ImageTk.PhotoImage((Image.open("img/raprapa.png")).resize((35,35),Image.LANCZOS))
    raprapaImg = Label(frame1, image=raprapaLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
