'''
books are made of 2 FILE: svg e png
'''
from seleniumwire import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
from mimetypes import guess_extension
import requests
from PIL import Image
from io import StringIO

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=/home/<user>/.config/google-chrome/Default")
prefs = {'download.default_directory' : '/Downloads'}
options.add_experimental_option('prefs', prefs)

br = webdriver.Chrome(chrome_options=options)

#start it up
print("Avvio di chrome....")
br.get("url link to book")

##wait time to access the book if the access is behind registration

print("Press Enter to start");
input()

for x in range(1, 689):
	try:
		r= str(x).zfill(4)
		 #pages ar form 0001.svg or .png to 0689.svg
		
		br.get("pngURL/'+r+'.png', 'wb') as file:
			file.write(br.find_element_by_tag_name('img').screenshot_as_png) #se non uso screenshot ma uso altro ottengo file migliore
		
			
		br.get("svgURL/"+str(r)+".svg")
		br.find_element_by_tag_name('svg').screenshot('/svg-'+r+'.png', 'wb') as file:
			file.write(br.find_element_by_tag_name('svg'))
	except Exception as e: print(e)
print("Finish....")
