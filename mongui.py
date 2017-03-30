import tkinter as tk
from tkinter import ttk
import psutil

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.read_percentCPU()
        self.read_percentMEM()

    def create_widgets(self):
        
        self.percentBarCPU = ttk.Progressbar(self,length=200,mode="determinate",orient=tk.HORIZONTAL)
        self.percentBarCPU.pack()

        self.CPUlabel = ttk.Label(self,text="Porcentaje de CPU en uso")
        self.CPUlabel.pack()

        

        self.percentBarMEM = ttk.Progressbar(self,length=200,mode="determinate",orient=tk.HORIZONTAL)
        self.percentBarMEM.pack()

        self.CPUlabel = ttk.Label(self,text="Porcentaje de MEMORIA en uso",)
        self.CPUlabel.pack()
        

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def read_percentCPU(self):
        
        self.CPUpercent = psutil.cpu_percent(interval=1)
        self.percentBarCPU["value"] = self.CPUpercent
        # Lee el estado de porcentaje en uso de CPU cada 50ms
        self.after(50, self.read_percentCPU)

    def read_percentMEM(self):
        self.MEMpercent = psutil.virtual_memory().percent

        self.percentBarMEM["value"] = self.MEMpercent
        # Lee el estado de porcentaje en uso de MEM cada 50ms
        self.after(50, self.read_percentMEM)

root = tk.Tk()
root.title("Monitor Procesos")
app = Application(master=root)
app.mainloop()