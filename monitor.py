import psutil

lstproc = psutil.pids()
for i in lstproc:
    print(psutil.Process(i).name()+"  %d Bytes"%psutil.Process(i).memory_info().rss)
    print("Porcentaje de uso de memoria: %f"%psutil.Process(i).memory_percent(memtype="rss"))
    print("numero de hilos : %d"%psutil.Process(i).num_threads())
    print()
