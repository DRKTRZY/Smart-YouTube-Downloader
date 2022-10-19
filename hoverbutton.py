import tkinter as tk

def custom_button(window,x, y, anchor,text, bcolor, fcolor, function):
    def on_enter(e):
        download_button["background"] = bcolor
        download_button["foreground"] = fcolor

    def on_leave(e):
        download_button["background"] = fcolor
        download_button["foreground"] = bcolor

    download_button = tk.Button(window, text=text, font=("YTSans 10"), fg=bcolor, bg=fcolor, border=0,activeforeground=fcolor, activebackground=bcolor, command=function)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    download_button.place(relx=x, rely=y, anchor=anchor,relwidth=0.215,relheight=0.5)