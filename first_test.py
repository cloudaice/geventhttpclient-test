# -*- coding: utf-8 -*-
from geventhttpclient import HTTPClient
from geventhttpclient import URL

url = URL("http://gevent.org/")

print url.request_uri
print url.path
http = HTTPClient(url.host)

response = http.get(url.path)

print response.status_code

print response.get('url')

print response.headers
#print response.read()


http.close()
