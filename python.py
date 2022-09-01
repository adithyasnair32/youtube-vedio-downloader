from cgitb import text
from distutils.cmd import Command
from os import link
from sqlite3 import Row
from sre_constants import SUCCESS
import  tkinter as tk
from  tkinter import *
from pytube import YouTube
from tkinter import filedialog,messagebox

def createWidgets():
    link_label =Label(root,text="Youtube URL:" , bg="#F5F5F5") 
    link_label.grid(row=1 ,column=0, pady= 5 , padx=5)


    root.link_text = Entry(root,width=50,textvariable=vedio_link)
    root.link_text.grid(row=1 ,column=1 , pady=5, padx =5)


    destinaion_label = Label(root,text="Destiantion:" , bg="#F5F5F5")
    destinaion_label.grid(row=2, column=0, pady=5 , padx=5)

    root.destination_text = Entry(root ,width= 35 , textvariable=download_path)
    root.destination_text.grid(row=2, column=1 , pady=3 , padx=3 )


    browse_button =Button(root,text="Browse", command=browse,width=10 , bg= "#CCEEDF")
    browse_button.grid(row=2,column=2,pady=1,padx=1)
    

    download_button = Button(root, text="Download vedio",command=download_vedio, width=25, bg= "#CCEEDF")
    download_button.grid(row=3 ,column=1,pady=3, padx=3)


def browse():
    download_dir = filedialog.askdirectory(initialdir="your directory")

    download_path.set(download_dir)

def download_vedio():
    
    url= vedio_link.get()
    folder =download_path.get()

    vedio=YouTube(url)
    streams=vedio.streams.first()
    streams.download(folder)

    messagebox.showinfo("sucsuss","Download is sucsussfull!Thankyou for using this application , you will find your vedio at\n"+folder)
    


root= tk.Tk()

root.geometry("600x120")
root.resizable(False,False)
root.title("YOUTUBE VEDIO DOWNLOADER")
root.config(bg = "#25265E")


vedio_link =StringVar()
download_path = StringVar()


createWidgets()


root.mainloop()


