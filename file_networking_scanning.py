import re


#fake url
phishing_log = "Suspicious Log:http://fakebank.com/transfer?amt=1000"

#creating regex pattern for url matching
url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[^\s]*'


urls = re.findall(url_pattern,phishing_log)

print(urls)