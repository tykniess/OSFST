all:
	cat os.lexc > backups/os.lexc.copy
	cat os.twol > backups/os.twol.copy
	hfst-lexc -v os.lexc -o os.lexc.hfst
	hfst-twolc os.twol -o os.twol.hfst
	hfst-compose-intersect -v -o os.gen.hfst os.lexc.hfst os.twol.hfst
	hfst-invert -v os.gen.hfst -o os.mor.hfst	
	hfst-fst2strings os.mor.hfst --xfst obey-flags | sort | gsed s/':'/'\t'/g|gsed s/'<'/' <'/g | gsed s/'>'/'> '/g > forms.txt
	python3 gi-prefix.py
	cat os.lexc | sh visualize_transducer.sh
	cat forms-prefixed.txt > forms.txt
	python3 coverage.py
	cat heliand/clean.txt|while read line; do hfst-lookup os.mor.hfst; done > lookup.txt
	echo 'The top 20 words yet to be included are:'
	cat words_not_covered.txt | sort | uniq -c| sort -rn | head -n 20             
