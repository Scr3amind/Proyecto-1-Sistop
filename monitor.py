import psutil

lstproc = psutil.pids()
for i in lstproc:
    print(psutil.Process(i).name()+"  %d Bytes"%psutil.Process(i).memory_info().rss)
    print(psutil.Process(i).memory_percent("rss"))
    print()