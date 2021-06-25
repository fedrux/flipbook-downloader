replacements = {'594.453':'2972.265', '814.208':'4071.04'}
for x in range(1, 689):
	try: 
		r= str(x).zfill(4)

		with open(r+".svg") as infile, open(r+"-resize.svg", 'w') as outfile:
			for line in infile:
				for src, target in replacements.items():
					line = line.replace(src, target, 1)
				outfile.write(line)
		
	except Exception as e: print(e)
