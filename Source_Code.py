import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage


# --------------------------------------------------


# Ensure High DPI awareness on Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# --------------------------------------------------


class Stopwatch:
    def __init__(self, master):
        self.master = master
        self.master.title("StopWatch")
        self.master.geometry("500x250")

        self.time = 0
        self.running = False

        self.label = ttk.Label(self.master, text="00:00:00", font=("Arial", 30))
        self.label.pack(pady=40)

        self.start_button = ttk.Button(self.master, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=40)

        self.stop_button = ttk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=30)

        self.reset_button = ttk.Button(self.master, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=40)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

    def update(self):
        if self.running:
            self.time += 0.1
            minutes, seconds = divmod(int(self.time), 60)
            hours, minutes = divmod(minutes, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_str)
            self.master.after(100, self.update)


if __name__ == "__main__":
    root = tk.Tk()
    logo = PhotoImage(file='logo.png')
    root.iconphoto(False, logo)
    stopwatch = Stopwatch(root)
    root.mainloop()