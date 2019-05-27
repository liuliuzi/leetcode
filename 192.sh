 sed -E 's/[[:space:]]+/\n/g' words.txt|sort| uniq -c| sort -n -r -k1 | awk '{print $2 " "$1}'
