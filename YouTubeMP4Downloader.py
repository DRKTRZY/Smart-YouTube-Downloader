import tkinter as tk
import os, pygame, random, ttk, webbrowser, tkinter.messagebox, urllib.request, io, urllib.parse
from pytube import YouTube
from tkinter import filedialog
from PIL import ImageTk,Image

# Window
window = tk.Tk()
window.geometry("595x540")
window.resizable(0,0)
window.title("SYD")   
window.configure(bg="#282828")
window.iconbitmap('resources/SYDApp.ico')

# Enter URL
link = tk.StringVar()

# Functions

# Hover Button
def custom_button(x, y, anchor,text, bcolor, fcolor, downloader):
    def on_enter(e):
        download_button["background"] = bcolor
        download_button["foreground"] = fcolor

    def on_leave(e):
        download_button["background"] = fcolor
        download_button["foreground"] = bcolor

    download_button = tk.Button(set_frame, text=text, font=("YTSans 10"), fg=bcolor, bg=fcolor, border=0,activeforeground=fcolor, activebackground=bcolor, command=downloader)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    download_button.place(relx=x, rely=y, anchor=anchor,relwidth=0.215,relheight=0.5)

def search_url(event):
    clearFrame()
    while 0 < 1:
        global image
        global thumbnail
        global inf_frame
        if link.get() == "Enter URL" or None:
            tkinter.messagebox.showerror("Error", "Please enter a valid link")
            break
        url = YouTube(link.get()).thumbnail_url
        url = url.replace("sddefault.jpg", "maxresdefault.jpg")
        with urllib.request.urlopen(url) as connection:
            raw_data = connection.read()
        im = Image.open(io.BytesIO(raw_data))
        img = im.resize((425,239))
        image = ImageTk.PhotoImage(img)
        widget = tk.Label(thumbnail,image=image)
        widget.pack()
        title_url = YouTube(link.get()).title
        channel_url = YouTube(link.get()).author
        time_url = YouTube(link.get()).length
        print(time_url)
        length_time = len(str(time_url))
        print(length_time)
        if length_time < 2:
            time_url = f"000{time_url}"
        elif length_time < 3 and time_url < 60:
            time_url = f"00{time_url}"
        time = ([str(i) for i in str(time_url)])
        time.insert(2,":")
        time = "".join(time)
        title = tk.Label(inf_frame,text=title_url,font=("YTSans 12 bold"),anchor="sw",fg="#FF0000",bg="#282828")
        title.place(relx=0.,rely=0,width=425,height=25)
        channel = tk.Label(inf_frame,text=channel_url,font=("YTSans 10"),fg="#FF0000",bg="#282828",anchor="sw")
        channel.place(relx=0.,rely=0.5,width=212.5,height=25)
        length = tk.Label(inf_frame,text=time,font=("YTSans 10"),fg="#FF0000",bg="#282828",anchor="sw")
        if time_url > 60:
            print(length_time)
            m, s = divmod(int(time_url), 60)
            h, m = divmod(m, 60)
            hour = f'{h:d}:{m:02d}:{s:02d}'
            length.configure(text=hour)
        length.place(relx=0.52,rely=0.5,width=212.5,height=25)
        format_label = tk.Label(set_frame, text="Format:", font=("YTSans 8"), bg="#282828", fg="white")
        format_label.place(relx=0, rely=0.335,relwidth=0.1099,relheight=0.375)
        format.place(relx=0.17, rely=0.5, anchor=tk.CENTER,relwidth=0.1099,relheight=0.375)
        custom_button(0.4, 0.5, tk.CENTER, "DOWNLOAD", "#FF0000", "#282828", downloader)

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
        if link.get() == "Enter URL":
            tkinter.messagebox.showerror("Error", "Please enter a valid link")
            break

        if format.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter a valid format")
            break

        path = filedialog.askdirectory(title="Select Directory")
        url = YouTube(str(link.get()))
        if path == "":
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
        confirmation.place(relx=0.5, rely=0.87, anchor=tk.CENTER)
        confirmation.configure(bg="#282828")
        window.after(3500, confirmation.destroy)

        break

def clearFrame():
        # destroy all widgets from frame
        global thumbnail
        for widget in thumbnail.winfo_children():
            widget.destroy()


def creator_link(url):
    webbrowser.open_new(url)

# Frames

set_frame = tk.Frame(window, bg="#282828",highlightbackground="green")
set_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER, relwidth=0.715, relheight=0.1)

inf_frame = tk.Frame(window, bg="#282828",highlightthickness=0.01)
inf_frame.place(relx=0.5, rely=0.203, anchor=tk.CENTER,relwidth=0.715,relheight=0.135)

frame = tk.Frame(window,bg="#333333")
frame.place(relx=0, rely=0,relwidth=1,relheight=0.115)

thumbnail = tk.Frame(window, bg="#282828",highlightbackground="red")
thumbnail.place(relx=0.5, rely=0.5, anchor=tk.CENTER,relwidth=0.715,relheight=0.435)

# Combobox
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

format = ttk.Combobox(set_frame, state="readonly", values=["720p", "360p", ".mp3"])

# Entry etc.
creator = tk.Label(window, text="Creator: DRKTRZY", fg="#d3d3d3", cursor="hand2", font=("YTSans 8 underline"),bg="#282828")
creator.place(relx=0.835,rely=0.955)
creator.bind("<Button-1>", lambda e: creator_link("https://github.com/DRKTRZY"))

entry = tk.Entry(frame, width=70,fg = 'grey', textvariable=link, bg="#202020", font=("YTSans 12"))
entry.insert(0, "Enter URL")
entry.bind("<FocusIn>", on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.place(relx=0.43, rely=0.5, anchor=tk.CENTER,relheight=0.775,relwidth=0.85)

search1 = ImageTk.PhotoImage(Image.open("resources/icon.png"))
search = tk.Button(frame,image=search1,bg="#333333",activebackground="#333333",border=0,command=lambda:search_url(search))
search.place(relx=0.89,rely=0.5,anchor=tk.CENTER,relwidth=0.06,relheight=0.6)
# Secret Sound
window.bind("<Return>", (lambda event: search_url(event)))
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