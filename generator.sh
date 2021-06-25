#!/bin/bash
mkdir -p out

for i in $(seq 1 689); do 

    page=`printf "%04d" $i`;
    
	wkhtmltoimage --transparent  pages1/${page}-resize.svg pages1/py-svg/${page}.png
	
    convert -flatten -geometry 2972x4071 -fuzz 10% -transparent white  -density 400   pages1/${page}.png pages1/py-svg/${page}.png out/$page.pdf
    
	echo ${page} 
    
    
    
done;
cd out
pdfunite * out.pdf
