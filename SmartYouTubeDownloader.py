import tkinter as tk
import os, ttk, webbrowser, tkinter.messagebox, urllib.request, io, urllib.parse,snd
from pytube import YouTube
from tkinter import filedialog
from PIL import ImageTk,Image
import hoverbutton as hvb
import clearframe as cr

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
def search_url(event):
    cr.clear(thumbnail)
    while True:
        global image
        if link.get() == "Enter URL" or not link.get():
            tkinter.messagebox.showerror("Error", "Please enter a valid link")
            break
            # For the Thumbnail image
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
        length_time = len(str(time_url))

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
            m, s = divmod(int(time_url), 60)
            h, m = divmod(m, 60)
            hour = f'{h:d}:{m:02d}:{s:02d}'
            length.configure(text=hour)

        length.place(relx=0.52,rely=0.5,width=212.5,height=25)
        format_label = tk.Label(set_frame, text="Format:", font=("YTSans 8"), bg="#282828", fg="white")
        format_label.place(relx=0, rely=0.335,relwidth=0.1099,relheight=0.375)
        format.place(relx=0.17, rely=0.5, anchor=tk.CENTER,relwidth=0.1099,relheight=0.375)
        hvb.custom_button(set_frame,0.4, 0.5, tk.CENTER, "DOWNLOAD", "#FF0000", "#282828", downloader)

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
    while True:
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
            digit = 1
            if os.path.exists(path):
                while True:
                    try:
                        new_file = base + "(" + str(digit) + ")" + ".mp3"
                        os.rename(downloaded_file, new_file)
                        if os.path.exists(path) == False:
                            break
                    except:
                        digit += 1
                        continue
                    else:
                        break

        elif format.get() == "720p" or "360p":
            video = url.streams.get_by_resolution(format.get())
            video.download(path)

        confirmation = tk.Label(window, text="Download Successful!", font=("YTSans", 16), fg="#FF0000")
        confirmation.place(relx=0.5, rely=0.87, anchor=tk.CENTER)
        confirmation.configure(bg="#282828")
        window.after(3500, confirmation.destroy)

        break

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
entry = tk.Entry(frame, width=70,fg = 'grey', textvariable=link, bg="#202020", font=("YTSans 12"))
entry.insert(0, "Enter URL")
entry.place(relx=0.43, rely=0.5, anchor=tk.CENTER,relheight=0.775,relwidth=0.85)

search1 = ImageTk.PhotoImage(Image.open("resources/icon.png"))
search = tk.Button(frame,image=search1,bg="#333333",activebackground="#333333",border=0,command=lambda:search_url(search))
search.place(relx=0.89,rely=0.5,anchor=tk.CENTER,relwidth=0.06,relheight=0.6)

# Binds
window.bind("<Return>", (lambda event: search_url(event)))

entry.bind("<FocusIn>", on_entry_click)
entry.bind('<FocusOut>', on_focusout)

window.bind("<Control-f>", snd.jukebox)
window.bind("<Control-s>", snd.stop_music)

window.mainloop()