'''
i libri sono composti da 2 FILE: svg e png
'''
from seleniumwire import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
from mimetypes import guess_extension
import requests
from PIL import Image
from io import StringIO

nomeLibro=""  #edit here
numeroPagine= #edit here



options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=/home/_____usrdname______/.config/google-chrome/Default")

br = webdriver.Chrome(chrome_options=options)


#start it up

print("Avvio di chrome....")
br.get("")


print("Quando vuoi avviare la sequenza premi invio");
input()

import os
if not os.path.exists('/'+nomeLibro+'/'):
    os.makedirs('/'+nomeLibro+'/')


for x in range(1, numeroPagine+1):
	print(str(x/numeroPagine*100) + "% --> " + str(x))
	try:
		r= str(x).zfill(4)
		
		
		urlImage = "/"+nomeLibro+"/"+str(r)+"_1.jpg?uni="  #change here
		
		br.get(urlImage)
		with open('/'+nomeLibro+'/'+r+'.png', 'wb') as file:
			file.write(br.find_element_by_tag_name('img').screenshot_as_png) #se non uso screenshot ma uso altro ottengo file migliore
		
		urlSvg="/"+nomeLibro+"/"+str(r)+".svg?uni="  #change here
		
		br.get(urlSvg)
		with open('/'+nomeLibro+'/'+r+'.svg', 'wb') as file:
			file.write(br.page_source.encode("utf-8")) #se non uso screenshot ma uso altro ottengo file migliore
		
	
			
			
			
	except Exception as e: 
		print(e)
		print(urlImage)
		print(urlSvg)


print("Finish....")
