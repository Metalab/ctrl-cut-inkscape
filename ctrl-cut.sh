eval svgfile=\${$#}
mv $svgfile $svgfile.svg
ctrl-cut $svgfile.svg 2> /dev/null
rm $svgfile.svg
