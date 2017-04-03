import tkinter as tk
from tkinter import ttk
import psutil

class Monitor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.read_percentCPU()
        self.read_percentMEM()

    def create_widgets(self):
        
        self.percentBarCPU = ttk.Progressbar(self,length=400,mode="determinate",orient=tk.HORIZONTAL)
        self.percentBarCPU.pack()
        
        CPUperc = tk.StringVar(self)


        self.CPUlabel = ttk.Label(self,text="Porcentaje de CPU en uso:")
        self.CPUlabel.pack()
        

        self.percentBarMEM = ttk.Progressbar(self,length=400,mode="determinate",orient=tk.HORIZONTAL)
        self.percentBarMEM.pack()

        self.CPUlabel = ttk.Label(self,text="Porcentaje de MEMORIA en uso:",)
        self.CPUlabel.pack()
        

        self.quit = tk.Button(self, text="Salir", fg="black",
                              command=root.destroy)
        self.quit.pack(side="bottom")
        
        xscroll = tk.Scrollbar(self)
        xscroll.pack(side="right", fill="y")


        self.lstbox = tk.Listbox(self,width=80,heigh=20,yscrollcommand=xscroll.set)
        xscroll.config(command=self.lstbox.yview)
       
        lstproc = psutil.pids()
        for i in lstproc:
        	self.lstbox.insert(i,psutil.Process(i).name())
        self.lstbox.pack()


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

    def bytes2human(n):
    #funcion que convierte de Bytes a distintas magnitudes mas legibles para el usuario
    # http://code.activestate.com/recipes/578019
    
	    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
	    prefix = {}
	    for i, s in enumerate(symbols):
	        prefix[s] = 1 << (i + 1) * 10
	    for s in reversed(symbols):
	        if n >= prefix[s]:
	            value = float(n) / prefix[s]
	            return '%.1f%s' % (value, s)
	    return "%sB" % n

root = tk.Tk()
root.title("Monitor Procesos")
app = Monitor(master=root)
app.mainloop()