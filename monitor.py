import psutil


    
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

def main():
	porcent = psutil.virtual_memory().percent
	total = bytes2human(psutil.virtual_memory().total)
	usada = bytes2human(psutil.virtual_memory().used)
	
	print('MEMORIA\n------')
	print('%-12s : %7s' % ("Porcentaje:", porcent))
	print('%-12s : %7s' % ("Total:", total))
	print('%-12s : %7s' % ("En Uso:", usada))
	print('------\n')
	
	print('CPU\n------')
	print('%-10s : %7s' % ("Porcentaje:", psutil.cpu_percent(interval=1)))
	print('------\n')

	print('%-30s  %7s' % ('PROCESO:','USO MEMORIA:' ))
	print('---------------------------------------------------\n')
	lstproc = psutil.pids()
	for i in lstproc:
		
		print('%-30s : %7s ' % (psutil.Process(i).name(), bytes2human(psutil.Process(i).memory_info().rss)))
	


main()

