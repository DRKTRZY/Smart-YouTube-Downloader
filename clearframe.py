
def clear(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()