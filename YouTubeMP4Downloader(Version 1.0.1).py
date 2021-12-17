import webbrowser
from pytube import YouTube
import tkinter.messagebox
import ttk
import tkinter as tk
import os
import pygame
import random

# Path
path = r"C:\DownloadsMP4"
if not os.path.exists(path):
    os.makedirs(path)
path_mp3 = r"C:\DownloadsMP3"
if not os.path.exists(path):
    os.makedirs(path)
mp3_path = "C:\DownloadsMP3"
mp4_path = "C:\DownloadsMP4"

# Window
window = tk.Tk()
window.geometry("500x300")
window.resizable(0, 0)
window.title("Youtube MP4 and MP3 Downloader")
window.configure(bg="#3f3f3f")
window.iconbitmap('C:\YouTube MP4 Downloader\images/icon1.ico')

# Label Title
mp4_title = tk.Label(window, text='YouTube MP4 and MP3 Downloader', font="Bahnschrift", fg="#d3d3d3")
mp4_title.place(x=116, y=10)
mp4_title.configure(bg="#3f3f3f")

# Enter URL
link = tk.StringVar()
link_label = tk.Label(window, text="Paste link here:", font="Bahnschrift", fg="#d3d3d3")
link_label.place(x=185, y=60)
link_label.configure(bg="#3f3f3f")
link_error = tk.Entry(window, width=70, fg="#2a2a2a", textvariable=link)
link_error.place(x=32, y=90)
link_error.configure(bg="#fbfbfb")

# Functions
def downloader():
    global resolution
    url = YouTube(str(link.get()))
    video = url.streams.get_by_resolution(resolution.get())
    video.download(path)
    bestätigung = tk.Label(window, text="Download Successful!", font=("Bahnschrift", 16, "bold"), fg="orange")
    bestätigung.place(x=155, y=230)
    bestätigung.configure(bg="#3f3f3f")
    window.after(2800, bestätigung.destroy)
    msg_box = tk.messagebox.askquestion("YouTube Mp4 and MP3 Downloader", "The file is located in the folder C:\DownloadsMP4                      Do you want to open this folder")
    if msg_box == 'yes':
        webbrowser.open(os.path.realpath(mp4_path))

def downloader_mp3():
    url = YouTube(str(link.get()))
    video = url.streams.filter(only_audio=True).first()
    downloaded_file = video.download(path_mp3)
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + ".mp3"
    os.rename(downloaded_file, new_file)
    bestätigung_mp3 = tk.Label(window, text="Download Successful!", font=("Bahnschrift", 16, "bold"), fg="orange")
    bestätigung_mp3.place(x=155, y=230)
    bestätigung_mp3.configure(bg="#3f3f3f")
    window.after(2800, bestätigung_mp3.destroy)
    msg_box = tk.messagebox.askquestion("YouTube Mp4 and MP3 Downloader", "The file is located in the folder C:\DownloadsMP3                      Do you want to open this folder")
    if msg_box == 'yes':
        webbrowser.open(os.path.realpath(mp3_path))

def creator_link(url):
    webbrowser.open_new(url)

# Combobox etc.
ebg = "#3f3f3f"
fg = "#d3d3d3"
style = ttk.Style()
style.theme_use('alt')
window.option_add('*TCombobox*Listbox*Background', "#bebebe")
window.option_add('*TCombobox*Listbox*Foreground', "#2a2a2a")
window.option_add('*TCombobox*Listbox*selectBackground', fg)
window.option_add('*TCombobox*Listbox*selectForeground', ebg)
style.map('TCombobox', fieldbackground=[('readonly', '#d3d3d3')])
style.map('TCombobox', selectbackground=[('readonly', '#d3d3d3')])
style.map('TCombobox', selectforeground=[('readonly', '#2a2a2a')])
style.map('TCombobox', background=[('readonly', "#d3d3d3")])
style.map('TCombobox', foreground=[('readonly', "#d3d3d3")])
resolution_label = tk.Label(window, text="Resolution:", font="Bahnschrift", fg="#d3d3d3")
resolution_label.place(x=100, y=198)
resolution_label.configure(bg="#3f3f3f")
resolution = ttk.Combobox(window, state="readonly", values=["720p", "480p  (Not Working)", "360p"], )
resolution.place(x=190, y=200)
creator = tk.Label(window, text="Creator: DRKTRZY", fg="#d3d3d3", cursor="hand2", font=("Bahnschrift 8 underline"))
creator.place(x=400, y=280)
creator.configure(bg="#3f3f3f")
creator.bind("<Button-1>", lambda e: creator_link("https://github.com/DRKTRZY"))

# Hover Button
def custom_button(x, y, text, bcolor, fcolor, downloader):
    def on_enter(e):
        download_button["background"] = bcolor
        download_button["foreground"] = fcolor

    def on_leave(e):
        download_button["background"] = fcolor
        download_button["foreground"] = bcolor

    download_button = tk.Button(window, text=text, font="Bahnschrift", fg=bcolor, bg=fcolor, border=0,
                                activeforeground=fcolor, activebackground=bcolor, padx=2, command=downloader)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    download_button.place(x=x, y=y)

custom_button(185, 120, "DOWNLOAD MP4", "orange", "#3f3f3f", downloader)
custom_button(185, 155, "DOWNLOAD MP3", "orange", "#3f3f3f", downloader_mp3)

# Secret Sound
pygame.mixer.init()

def jukebox(event):
    music = ["C:\YouTube MP4 Downloader\Sound/Flamewall.mp3","C:\YouTube MP4 Downloader\Sound/pvrnormal.mp3"]
    random_music = random.choice(music)
    pygame.mixer.music.load(random_music)
    pygame.mixer.music.play()

def stop_music(event):
    pygame.mixer.music.stop()

window.bind("<Control-f>", jukebox)
window.bind("<Control-s>", stop_music)

window.mainloop()