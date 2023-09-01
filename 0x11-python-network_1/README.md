0x11-python-network_1:
These are the objective to be handled in the following directory

Certainly! Here are answers to your objectives:
1. How to fetch internet resources with the Python package urllib:
You can use the urllib package in Python to fetch internet resources by creating a request and then opening the URL. Here's a basic example of how to use it for making an HTTP GET request:

----------------------------------------------
import urllib.request

url = 'https://example.com'
response = urllib.request.urlopen(url)
html = response.read()

print(html)
-----------------------------------------------

2. How to decode urllib body response:
You can decode the response body using the decode() method with the appropriate encoding. For example, to decode a response as UTF-8:

---------------------------------------------
html_decoded = html.decode('utf-8')
print(html_decoded)
----------------------------------------------

3. How to use the Python package requests #requestsiswaysimplerthanurllib:
The requests package is indeed a more user-friendly alternative to urllib. To use it, you need to install it first (if not already installed) and then make HTTP requests. Here's an example:

---------------------------------------------
import requests

url = 'https://example.com'
response = requests.get(url)

print(response.text)
------------------------------------------------

4. How to make an HTTP GET request:
Using the requests library, as shown above, you can make an HTTP GET request using the requests.get(url) method.

5. How to make HTTP POST/PUT/etc. requests:
You can use the requests library to make various HTTP requests. For example, to make a POST request:

----------------------------------------------------
import requests

url = 'https://example.com'
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, data=data)

print(response.text)
--------------------------------------------------
Similarly, you can use requests.put(), requests.delete(), etc., for other HTTP methods.

6. How to fetch JSON resources:
To fetch JSON resources, you can make an HTTP GET request using requests and then parse the JSON response. Here's an example:

--------------------------------------
import requests

url = 'https://example.com/api/data.json'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    print(json_data)
-------------------------------------

7. How to manipulate data from an external service:

Once you've fetched data from an external service, you can manipulate it using Python's built-in data structures and libraries, depending on your specific requirements. For example, you can use dictionaries, lists, and various Python libraries like Pandas or NumPy for data manipulation, analysis, and visualization.

Here's a basic example of manipulating JSON data:

-----------------------------------------------
import requests

url = 'https://example.com/api/data.json'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()
    # Manipulate the JSON data as needed
    print(json_data)
----------------------------------------------
