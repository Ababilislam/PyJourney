from urllib.request import Request, urlopen
obj = Request("https://www.tutorialspoint.com/")
resp = urlopen(obj)
data = resp.read()
print (data)