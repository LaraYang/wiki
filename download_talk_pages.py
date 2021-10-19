from convokit import Corpus, download
for i in range(2018, 2020):
	print("Downloading data for {}... ".format(i))
	_ = Corpus(filename=download("wikiconv-"+str(i)))
