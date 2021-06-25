





replacements = {'594.453':'2972.265', '814.208':'4071.04'}


for x in range(1, 529):
	try: 
		r= str(x).zfill(4)
		

		with open(r+".svg") as infile, open(r+"-resize.svg", 'w') as outfile:
			for line in infile:
				for src, target in replacements.items():
					line = line.replace(src, target, 1)
				outfile.write(line)
		
		
		
	except Exception as e: print(e)

'''

for x in range(1, 529):
	try: 
		r= str(x).zfill(4)
		
		#input file
		fin = open(r+".svg", "rt")
		#output file to write the result to
		fout = open(r+"-resize.svg", "wt")
		#for each line in the input file
		for line in fin:
			#read replace the string and write to output file
			fout.write(line.replace('594.453', '2972.265'))
			
			fout.write(line.replace('814.208', '4071.04'))
		#close input and output files
		fin.close()
		fout.close()
		

		
		
		
		
	except Exception as e: print(e)
'''
