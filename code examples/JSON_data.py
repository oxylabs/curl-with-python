# imports here
data = {'field1': 'value1', 'field2': 'value2'}
post_data = json.dumps(data)
headers = ['Content-Type: application/json']
buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/post')
c.setopt(c.POSTFIELDS, post_data)
c.setopt(c.HTTPHEADER, headers)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

response = buffer.getvalue()

print(response.decode('utf-8'))
