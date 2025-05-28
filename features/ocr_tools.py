import pytesseract
from PIL import Image
import tkinter as tk
import mss
from speech_utils import speak

start_x = start_y = end_x = end_y = 0


def read_screen():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-alpha", 0.3)
    root.attributes("-topmost", True)
    root.lift()
    root.config(bg='black')
    canvas = tk.Canvas(root, cursor="cross", bg='black')
    canvas.pack(fill=tk.BOTH, expand=True)
    def on_mouse_down(event):
        global start_x, start_y
        start_x, start_y = event.x, event.y
        canvas.delete("rect")
    def on_mouse_drag(event):
        canvas.delete("rect")
        canvas.create_rectangle(start_x, start_y, event.x, event.y, outline="red", width=2, tags="rect")
    def on_mouse_up(event):
        global end_x, end_y
        end_x, end_y = event.x, event.y
        root.quit()
    canvas.bind("<Button-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)
    root.mainloop()
    root.destroy()
    x1 = min(start_x, end_x)
    y1 = min(start_y, end_y)
    x2 = max(start_x, end_x)
    y2 = max(start_y, end_y)
    with mss.mss() as sct:
        monitor = {
            "top": y1,
            "left": x1,
            "width": x2 - x1,
            "height": y2 - y1
        }
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
    img.show()
    text = pytesseract.image_to_string(img)
    return text.strip()