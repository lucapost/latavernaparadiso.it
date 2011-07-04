compile:
	./minimalsite.py -t default

zip:
	7z a -tzip ~/tmp/tavpar.zip -xr@exclude.list
	@echo creating ~/tmp/tavpar.zip
