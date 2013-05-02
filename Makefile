all:
	#./scripts/correctnames
	./scripts/gentemplate ./README.md ./template.html
	python mkhtml.py
