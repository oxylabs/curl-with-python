# imports here
headers = ["User-Agent: Python-PycURL", "Accept: application/json"]
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, "https://httpbin.org/headers")
c.setopt(c.HTTPHEADER, headers)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
response = buffer.getvalue()
print(response.decode("utf-8"))
