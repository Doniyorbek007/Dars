import http.client

h1 =  http.client.HTTPConnection("www.python.org", 80,timeout=10)

print(h1)