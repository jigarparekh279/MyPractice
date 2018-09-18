import requests

def awesome_function():
	print("Do some heavy calculations")
	return 412

def countWords(text):
	return len(text)

def download_text_from_web():
	return "random text"	
	
def download_text_from_web():
	r = requests.get('https://pypi.org/project/mock/')
	return r.text
	
def do_text_analysis():
	text = download_text_from_web()
	word_count = countWords(text)
	return word_count
