import webbrowser
from pytube import YouTube
import ttk
import tkinter as tk
from tkinter import filedialog
import os
import pygame
import random

# Window
window = tk.Tk()
window.geometry("500x300")
window.resizable(0, 0)
window.title("SYD")
window.configure(bg="#282828")
window.iconbitmap('resources/SYDApp.ico')

# Label Title
mp4_title = tk.Label(window, text='Smart YouTube Downloader', font=("YTSans Bold", 14), fg="#FF0000")
mp4_title.place(relx=0.5, y=10, anchor=tk.CENTER)
mp4_title.configure(bg="#282828")

# Enter URL
link = tk.StringVar()

link_label = tk.Label(window, text="Paste link here:", font="YTSans", fg="#FF0000")
link_label.place(relx=0.5, y=60, anchor=tk.CENTER)
link_label.configure(bg="#282828")
entry = tk.Entry(window, width=70, fg="#ffffff", textvariable=link, bg="#202020", highlightthickness=0.5,
                 borderwidth=0.5)
entry.config(highlightbackground="#313131", highlightcolor="#3ea6ff")

entry.place(relx=0.5, y=90, anchor=tk.CENTER)


# Functions
def downloader():
    while 0 < 1:
        global resolution
        path = filedialog.askdirectory(title="Select Directory")
        url = YouTube(str(link.get()))
        if path == "":
            break
        video = url.streams.get_by_resolution(resolution.get())
        video.download(path)

        confirmation = tk.Label(window, text="Download Successful!", font=("YTSans", 16), fg="#FF0000")
        confirmation.place(relx=0.5, y=230, anchor=tk.CENTER)
        confirmation.configure(bg="#282828")
        window.after(2800, confirmation.destroy)
        entry.delete(0, tk.END)

        break


def downloader_mp3():
    while 0 < 1:
        path = filedialog.askdirectory(title="Select Directory")
        url = YouTube(str(link.get()))
        if path == "":
            break
        video = url.streams.filter(only_audio=True).first()
        video.download(path)



        confirmation = tk.Label(window, text="Download Successful!", font=("YTSans", 16,), fg="#FF0000")
        confirmation.place(relx=0.5, y=230, anchor=tk.CENTER)
        confirmation.configure(bg="#282828")
        window.after(3500, confirmation.destroy)

        break


def creator_link(url):
    webbrowser.open_new(url)


# Combobox etc.
ebg = "#282828"
fg = "#d3d3d3"
style = ttk.Style()
style.theme_use('clam')
window.option_add('*TCombobox*Listbox*Background', "#202020")
window.option_add('*TCombobox*Listbox*Foreground', "#ffffff")
window.option_add('*TCombobox*Listbox*selectBackground', "#313131")
window.option_add('*TCombobox*Listbox*selectForeground', "#ffffff")
style.map('TCombobox', fieldbackground=[('readonly', '#202020')])
style.map('TCombobox', selectbackground=[('readonly', '#121212')])
style.map('TCombobox', selectforeground=[('readonly', '#ffffff')])
style.map('TCombobox', background=[('readonly', "#313131")])
style.map('TCombobox', foreground=[('readonly', "#ffffff")])
style.configure("TCombobox", lightcolor="#313131", darkcolor="#313131")
resolution = ttk.Combobox(window, state="readonly", values=["720p", "480p  (Not Working)", "360p"])
resolution.place(relx=0.5, y=200, anchor=tk.CENTER)
creator = tk.Label(window, text="Creator: DRKTRZY", fg="#d3d3d3", cursor="hand2", font=("YTSans 8 underline"))
creator.place(x=400, y=280)
creator.configure(bg="#282828")
creator.bind("<Button-1>", lambda e: creator_link("https://github.com/DRKTRZY"))


# Hover Button
def custom_button(x, y, anchor, text, bcolor, fcolor, downloader):
    def on_enter(e):
        download_button["background"] = bcolor
        download_button["foreground"] = fcolor

    def on_leave(e):
        download_button["background"] = fcolor
        download_button["foreground"] = bcolor

    download_button = tk.Button(window, text=text, font="YTSans", fg=bcolor, bg=fcolor, border=0,
                                activeforeground=fcolor, activebackground=bcolor, padx=2, command=downloader)
    download_button.bind("<Enter>", on_enter)
    download_button.bind("<Leave>", on_leave)
    download_button.place(relx=x, y=y, anchor=anchor)


custom_button(0.5, 120, tk.CENTER, "DOWNLOAD MP4", "#FF0000", "#282828", downloader)
custom_button(0.5, 155, tk.CENTER, "DOWNLOAD MP3", "#FF0000", "#282828", downloader_mp3)
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