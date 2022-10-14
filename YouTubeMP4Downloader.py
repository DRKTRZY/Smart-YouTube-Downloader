import tkinter as tk
import os, pygame, random, ttk, webbrowser, tkinter.messagebox, urllib.request, io
from pytube import YouTube
from tkinter import filedialog
from PIL import ImageTk,Image

# Window
window = tk.Tk()
window.geometry("595x540")
window.resizable(0, 0)
window.title("SYD")
window.configure(bg="#282828")
window.iconbitmap('resources/SYDApp.ico')

# Enter URL
link = tk.StringVar()

# Functions

def test():
    while 0 < 1:
        global image
        global thumbnail
        global inf_frame
        clearFrame()
        if link.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid link")
            break
        url = YouTube(link.get()).thumbnail_url
        with urllib.request.urlopen(url) as connection:
            raw_data = connection.read()
        im = Image.open(io.BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        widget = tk.Label(thumbnail,image=image)
        widget.pack()
        title_url = YouTube(link.get()).title
        channel_url = YouTube(link.get()).author
        print(channel_url)
        print(title_url)
        title = tk.Label(inf_frame,text=title_url,font=("YTSans 12 bold"),fg="red",bg="#282828")
        title.place(relx=0.,rely=0.1,width=118,height=35)
        channel = tk.Label(inf_frame,text=title_url,font=("YTSans 12 bold"),fg="red",bg="#282828")


        return image
    
def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if entry.get() == 'Enter URL':
       entry.delete(0, "end") # delete all the text in the entry
       entry.insert(0, '') #Insert blank for user input
       entry.config(fg = "#ffffff")

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter URL')
        entry.config(fg = 'grey')

def downloader():
    while 0 < 1:
        global resolution
        if link.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid link")
            break
        path = filedialog.askdirectory(title="Select Directory")
        url = YouTube(str(link.get()))
        if path == "":
            break

        if format.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid format")
            break

        elif format.get() == ".mp3":
            video = url.streams.filter(only_audio=True).first()
            downloaded_file = video.download(path)
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + ".mp3"
            os.rename(downloaded_file, new_file)

        elif format.get() == "720p" or "360p":
            print("test")
            print(format.get())
            video = url.streams.get_by_resolution(format.get())
            video.download(path)

        confirmation = tk.Label(window, text="Download Successful!", font=("YTSans", 16), fg="#FF0000")
        confirmation.place(relx=0.5, y=230, anchor=tk.CENTER)
        confirmation.configure(bg="#282828")
        window.after(2800, confirmation.destroy)
        entry.delete(0, tk.END)

        break

def clearFrame():
        # destroy all widgets from frame
        global thumbnail
        for widget in thumbnail.winfo_children():
            widget.destroy()

def creator_link(url):
    webbrowser.open_new(url)

# Combobox etc.
style = ttk.Style()
style.theme_use('clam')
window.option_add('*TCombobox*Listbox*Background', "#202020")
window.option_add('*TCombobox*Listbox*Foreground', "#ffffff")
window.option_add('*TCombobox*Listbox*selectBackground', "#313131")
window.option_add('*TCombobox*Listbox*selectForeground', "#ffffff")
style.map('TCombobox', fieldbackground=[('readonly', '#202020')])
style.map('TCombobox', selectbackground=[('readonly', '#202020')])
style.map('TCombobox', selectforeground=[('readonly', '#ffffff')])
style.map('TCombobox', background=[('readonly', "#313131")])
style.map('TCombobox', foreground=[('readonly', "#ffffff")])
style.configure("TCombobox", lightcolor="#313131", darkcolor="#313131")

set_frame = tk.Frame(window, bg="blue",highlightbackground="green")
set_frame.place(relx=0.9, rely=0.5, anchor=tk.CENTER,width=65,height=250)

inf_frame = tk.Frame(window, bg="green",highlightthickness=0.01)
inf_frame.place(relx=0.5, rely=0.203, anchor=tk.CENTER,width=400,height=65)

format = ttk.Combobox(window, state="readonly", values=["720p", "360p", ".mp3"],width=5)
format.place(relx=0.9, rely=0.4, anchor=tk.CENTER)

creator = tk.Label(window, text="Creator: DRKTRZY", fg="#d3d3d3", cursor="hand2", font=("YTSans 8 underline"),bg="#282828")
creator.place(relx=0.835,rely=0.955)
creator.bind("<Button-1>", lambda e: creator_link("https://github.com/DRKTRZY"))

frame = tk.Canvas(window,bg="#333333",width=600,height=60,highlightbackground="#333333",highlightcolor="#333333")
frame.place(relx=0,rely=0)

thumbnail = tk.Frame(window, bg="red",highlightbackground="red")
thumbnail.place(relx=0.5, rely=0.5, anchor=tk.CENTER,width=400,height=250)

entry = tk.Entry(frame, width=70,fg = 'grey', textvariable=link, bg="#202020", font=("YTSans 12"))
entry.insert(0, "Enter URL")
entry.bind("<FocusIn>", on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.place(relx=0.42, rely=0.5, anchor=tk.CENTER,height=42,width=500)



# Hover Button
def custom_button(x, y,anchor,downloader):
    image_a = ImageTk.PhotoImage(Image.open("resources/btn1.png"))
    image_b = ImageTk.PhotoImage(Image.open("resources/btn2.png"))
    def on_enter(e):
        download_button["image"]=image_b

    def on_leave(e):
        download_button["image"]=image_a

    download_button = tk.Button(window,image=image_a,border=0,background="#282828", cursor="hand2", command=downloader,relief=tk.SUNKEN)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    download_button.place(relx=x, rely=y, anchor=anchor)

custom_button(0.9, 0.4, tk.CENTER, downloader)
custom_button(0.9, 0.5, tk.CENTER, test)
# Secret Sound
pygame.mixer.init()

def jukebox(event):
    music = ["resources/sound/Flamewall.mp3", "resources/sound/pvrnormal.mp3", "resources/sound/Aa.mp3"]
    random_music = random.choice(music)
    pygame.mixer.music.load(random_music)
    pygame.mixer.music.play()

def stop_music(event):
    pygame.mixer.music.stop()


window.bind("<Control-f>", jukebox)
window.bind("<Control-s>", stop_music)

window.mainloop()