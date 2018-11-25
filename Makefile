ZIPFILE = gnugo.zip

$(ZIPFILE): handler.py
	zip -r $@ $< gnugo

clean:
	rm $(ZIPFILE) 