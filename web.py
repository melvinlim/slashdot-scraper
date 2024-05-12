import requests
from bs4 import BeautifulSoup
import re

def textWWW(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	return soup.get_text()

def textSlashdot():
	x=textWWW("https://www.slashdot.org")
	x=re.sub('[\n\t]+','\n',x)
	s=re.search('[1-2][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',x)
	x=x[(s.span(0)[1]+1):]

	#s=x.find('«')		#reads all articles.
	#x=x[:s]

	s=re.search('[1-2][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',x)			#reads only latest article.
	x=x[:s.span(0)[0]]
	return x

def main():
	x=textSlashdot()
	y=open('asdf.txt','w')
	y.write(x)
	y.close()

#main()

print(textSlashdot())
