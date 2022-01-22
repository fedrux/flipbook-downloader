
from xml.dom import minidom

nomeLibro=""
numeroPagine=



cartella = '/'+nomeLibro+'/'


for x in range(1, numeroPagine+1):
	print(str(x/numeroPagine*100) + "% --> " + str(x))
	try: 
		r= str(x).zfill(4)
		

		with open(cartella+r+".svg") as infile, open(cartella+r+"-resize.svg", 'w') as outfile:
			for line in infile:
				
				width = minidom.parseString(line).getElementsByTagName("svg:svg")[0].getAttribute("width")[:-2] # elimina px
				height = minidom.parseString(line).getElementsByTagName("svg:svg")[0].getAttribute("height")[:-2]
				
				replacements = {width:str(float(width)*4), height:str(float(height)*4)}#fare in scala 4 a 1, deve cambiare di libro in libro
				
				
				
				for src, target in replacements.items():
					line = line.replace(src, target, 1)#lasciare sempre 1, non deve cambiare la viewbox
				outfile.write(line)
		
		
		
	except Exception as e: print(e)
