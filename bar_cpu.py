import tkinter as tk
from tkinter import ttk
import psutil

class PorcentajeCpu(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=300, mode="determinate")
        self.progress.pack()

        self.percent = 0
        
        self.start()

    def start(self):
        self.progress["value"] = 0
        
        self.progress["maximum"] = 100
        self.read_percent()

    def read_percent(self):
        
        self.percent = psutil.cpu_percent(interval=1)
        self.progress["value"] = self.percent
        # Lee el estado de porcentaje en uso de CPU cada 50ms
        self.after(50, self.read_percent)

app = PorcentajeCpu()
app.mainloop()