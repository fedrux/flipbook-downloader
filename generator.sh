#!/bin/bash

cd "./"


#non mettere spazi tra definizione variabile e uguale e valore


nomeLibro=""
numeroPagine=


mkdir -p $nomeLibro/out


for i in $(seq 1 $numeroPagine); do #inserire da 1 al numero di page

    page=`printf "%04d" $i`;
    
	wkhtmltoimage --transparent  $nomeLibro/${page}-resize.svg $nomeLibro/SVG_${page}.png
	
    convert -flatten -geometry 2972x4071 -fuzz 10% -transparent white  -density 400   $nomeLibro/${page}.png $nomeLibro/SVG_${page}.png $nomeLibro/out/$page.pdf
    
    rm $nomeLibro/SVG_${page}.png
	
	echo ${page} 
    
    
    
done;
cd $nomeLibro/out
pdfunite * $nomeLibro.pdf
