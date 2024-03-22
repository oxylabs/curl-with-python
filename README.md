# How to Use cURL With Python

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/eWsVUJrnG5)

Follow this guide to learn how to use cURL in Python to easily send HTTP requests to websites. We'll overview how to send GET and POST requests, custom HTTP headers, handle redirects, and how to fix common PycURL issues.

See the [full article](https://oxylabs.io/blog/curl-with-python) in our blog.

- [Install Python cUrl Library](#install-python-curl-library)
- [GET Requests with PycURL](#get-requests-with-pycurl)
- [POST Requests with PycURL](#post-requests-with-pycurl)
- [Sending Custom HTTP Headers](#sending-custom-http-headers)
- [Sending JSON Data with PycURL](#sending-json-data-with-pycurl)
- [Handling Redirects](#handling-redirects)
  * [Get only HTTP headers](#get-only-http-headers)
- [PycURL vs. Requests: pros and cons](#pycurl-vs-requests-pros-and-cons)
- [Web Scraping with PycURL](#web-scraping-with-pycurl)
- [Common errors and resolutions](#common-errors-and-resolutions)
  * [1. ImportError for pycurl and openssl](#1-importerror-for-pycurl-and-openssl)
- [Conclusion](#conclusion)

## Install Python cUrl Library

You can install PycURL using `pip`, the package installer for Python:

```bash
pip install pycurl
```

## GET Requests with PycURL

For this tutorial, we’ll be using this website – [https://httpbin.org](https://httpbin.org), which returns data in JSON with all the headers, data, form, and files found within the request. Moreover, this website accepts only POST request methods, while [https://httpbin.org/get](https://httpbin.org/get) accepts `GET` requests. 

Executing a `GET` request with PycURL is a rather straightforward process. If you use the cURL command and don’t provide the `-X` option, a `GET` request is sent by default.

```bash
$ curl https://httpbin.org/get
```

You can do the same thing using the PycURL library: 

```python
import pycurl
from io import BytesIO

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/get')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
print(body.decode('utf-8'))
```

In this example, we’re creating a PycURL object, setting the URL option, and providing a buffer to store the response data. For comparison, see [how GET requests can be sent via cURL](https://oxylabs.io/blog/curl-get-requests) in the terminal.

## POST Requests with PycURL

POST requests send data to a server, typically to create or update a resource. To send a `POST` request with PycURL, use the following code:

```python
# imports here
data = {"field1": "value1", "field2": "value2"}
post_data = "&".join([f"{k}={v}" for k, v in data.items()])
buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, "https://httpbin.org/post")
c.setopt(c.POSTFIELDS, post_data)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

response = buffer.getvalue()
print(response.decode("utf-8"))
```

Here, we’re creating a dictionary with the data we want to send, convert to a query string format, and setting the `POSTFIELDS` option to the prepared data. If you're interested in running cURL via your terminal, see this post on [how to send POST requests with cURL](https://oxylabs.io/blog/curl-post-requests).

## Sending Custom HTTP Headers

HTTP headers are used to provide additional information about a request or a response. Custom headers can also be included in `GET` requests, depending on your requirements.

To send custom HTTP headers with a PycURL `GET` request, use the following code:

```python
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
```

In this example, we’re creating a list of custom headers and setting the `HTTP HEADER` option to this list. After executing the request, we close the PycURL object and print the response. The process of [sending HTTP headers with cURL ](https://oxylabs.io/blog/curl-send-headers)via the terminal doesn't differ too much.

## Sending JSON Data with PycURL

JSON is a popular data format for exchanging data between clients and servers. To send data in a `POST` request using PycURL, see the following example:

```python
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
```

In this example, we’re converting the data dictionary to a JSON-formatted string and setting the `POSTFIELDS` option to the JSON string. We’re also setting the content-type header with the intention of informing the server that we’re sending JSON data.

## Handling Redirects

PycURL can automatically follow HTTP redirects by setting the `FOLLOWLOCATION` option:

```python
# imports here
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, "http://httpbin.org")
c.setopt(c.FOLLOWLOCATION, 1)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
response = buffer.getvalue()
print(response.decode("utf-8"))
```

This example demonstrates how to follow redirects by setting the `FOLLOWLOCATION` option to 1 (True).

### Get only HTTP headers

To get only the HTTP headers, you can set the `HEADERFUNCTION` option to a custom function, which will process the received headers:

```python
# imports here
def process_header(header_line):
    print(header_line.decode('utf-8').strip())

c = pycurl.Curl()
c.setopt(c.URL, 'https://httpbin.org/headers')
c.setopt(c.HEADERFUNCTION, process_header)
c.setopt(c.NOBODY, 1)
c.perform()
c.close()
```

## PycURL vs. Requests: pros and cons

When it comes to choosing between PycURL and Requests, each library has its own strengths and weaknesses. Let’s take a closer look at both:

|          | PycURL                                                                   | Requests                                                              |
|----------|--------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Pros     | Faster than Requests, powerful, flexible, supports multiple protocols.   | Easier to learn and use, more readable syntax, better suited for simple tasks. |
| Cons     | Steeper learning curve, more verbose syntax.                             | Slower than PycURL, supports only the HTTP and HTTPS protocols.       |

If you prioritize performance and flexibility, PycURL might be a better choice. However, if you’re looking for a simpler and more user-friendly library, you should probably go with Requests.

## Web Scraping with PycURL
Web scraping is a technique for extracting information from websites by parsing the HTML content. To perform web scraping tasks, you’ll need additional libraries like BeautifulSoup or lxml. Also, PycURL is particularly useful for web scraping tasks that require handling redirects, cookies, or custom headers.

Typically, web scraping begins with a `GET` request for retrieving the HTML content of the target webpage. Here's an example of web scraping with PycURL and BeautifulSoup:

```python
import pycurl
from io import BytesIO
from bs4 import BeautifulSoup

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, "https://books.toscrape.com")
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
html = buffer.getvalue().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# Extract data from the parsed HTML
title = soup.find("title")
print(title.text)
```

In this example, we’re using PycURL to fetch the HTML content. Then, we parse it with BeautifulSoup to extract the desired data. 

## Common errors and resolutions

### 1. ImportError for pycurl and openssl

In some cases, you may have an error in running the code with the libcurl library. It would look something like this:

```bash
mportError: pycurl: libcurl link-time ssl backends (secure-transport, openssl) do not include compile-time ssl backend (none/other)
```

This error means that the OpenSSL headers are missing from your system. To fix this, use the following commands depending on your operating system.

**On macOS**, install OpenSSL 1.1 with Homebrew:

```bash
brew install openssl@1.1
export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
```

Afterwards, reinstall PycURL: 

```bash
pip uninstall pycurl
pip install pycurl --no-cache-dir
```

**On Windows**, [download](https://slproweb.com/products/Win32OpenSSL.html) and install the OpenSSL 1.1.x binaries. After that, add the following environment variables:

- `PYCURL_SSL_LIBRARY` with the value / `openssl`
- `LIB` with the value `C:\OpenSSL-Win64\lib` (replace `C:\OpenSSL-Win64` with the actual installation path if different)
- `INCLUDE` with the value `C:\OpenSSL-Win64\include`

Reinstall the Python library PycURL, and your code should now work.

2. UnicodeEncodeError when sending non-ASCII data

This error occurs when you try to send non-ASCII characters in a PycURL request without properly encoding the data. 

To resolve this issue, make sure to encode the data using the appropriate character encoding (usually `'utf-8'`) before sending it with PycURL:

```python
# imports here

data = {"field1": "value1", "field2": "valüe2"}
post_data = "&".join([f"{k}={v}" for k, v in data.items()]).encode('utf-8')
buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, "https://httpbin.org/post")
c.setopt(c.POSTFIELDS, post_data)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

response = buffer.getvalue()
print(response.decode("utf-8"))
```

## Conclusion

Using cURL with Python through the PycURL library offers a range of powerful features for interacting with web resources and APIs. Following the examples in this guide, you can perform tasks such as GET and POST requests, handling HTTP requests, headers and form data, and even web scraping.

We hope that you found this guide helpful. If you have any questions related to the matter, feel free to contact us at support@oxylabs.io, and our professionals will get back to you within a day. If you're curious to learn more about the topic, check out our articles on [How to Use cURL With Proxy?](https://oxylabs.io/blog/curl-with-proxy), [cURL with Python](https://oxylabs.io/blog/curl-with-python), and [cURL with APIs](https://oxylabs.io/blog/curl-with-api).


