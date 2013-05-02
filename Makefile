all:
	#./scripts/correctnames
	./scripts/gentemplate ./README.md ./template.html
	python ./scripts/mkhtml.py
