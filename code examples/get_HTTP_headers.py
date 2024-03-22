# imports here
def process_header(header_line):
    print(header_line.decode('utf-8').strip())

c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/headers')
c.setopt(c.HEADERFUNCTION, process_header)
c.setopt(c.NOBODY, 1)
c.perform()
c.close()
