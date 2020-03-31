for filename in *.txt; do
	../youtube-dl -o "${filename%.*}/%(autonumber)s-%(playlist_title)s.mp4" --cookie ../cookies.txt -a ${filename} --ignore-errors
done
