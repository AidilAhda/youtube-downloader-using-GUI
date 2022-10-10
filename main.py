import tkinter as tk
from tkinter import ttk
from pytube import YouTube


def Take_input():
    # get value
    getLink = txt1.get()
    video = YouTube(getLink)
    stream = video.streams.get_highest_resolution()
    stream.download()

# Creating tkinter window
window = tk.Tk()
window.title('Temperature Converter')
window.geometry('500x250')
window.resizable(False, False)

# label text for title
title = ttk.Label(
    window, text="Download Video Youtube",
    background='white', foreground="green",
    font=("Times New Roman", 15)).grid(row=0, column=3)

label1 = ttk.Label(
    window,text="Insert Your Link = ",
    background='white',foreground='black',
    font=("Times New Roman", 11)
).grid(row=1,column=2)

# editteks 1
txt1 = tk.StringVar()
textField1 = tk.Entry(window, textvariable=txt1,width=45).grid(row=1,column=3)



Display = tk.Button(window, height=1,
                    width=20,
                    text="Download",
                    background="green",
                    foreground="white",
                    command=lambda: Take_input()).grid(row=2,column=3)


window.mainloop()
