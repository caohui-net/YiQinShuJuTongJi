import requests 
print("downloading with requests")
url = 'http://www.gutenberg.org/cache/epub/1112/pg1112.txt' 
r = requests.get(url) 
with open("test.txt", "wb") as code:
     code.write(r.content)