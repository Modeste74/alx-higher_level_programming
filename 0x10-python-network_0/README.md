What a URL is:
A URL (Uniform Resource Locator) is a reference or address used to locate resources on the internet. It's a formatted string that specifies the protocol, domain name, and specific path to a resource, such as a webpage, image, or file.

What HTTP is:
HTTP (Hypertext Transfer Protocol) is a protocol used for communication between web browsers (clients) and web servers. It defines the rules for how requests from clients are made to servers and how servers respond with the requested data.

How to read a URL:
A URL consists of several components:

=> Scheme: Specifies the protocol used (e.g., "http" or "https").
=> Domain/Subdomain: The address of the server hosting the resource.
=> Port: Optional, specifies the network port for the server.
=> Path: The specific location of the resource on the server.
=> Query String: Optional, contains parameters for the resource.
=> Fragment: Optional, refers to a specific part of the resource.

The scheme for an HTTP URL:
The scheme for an HTTP URL is typically "http" or "https" (for secure connections).

What a domain name is:
A domain name is a human-readable address that corresponds to a specific IP address on the internet. It's used to identify resources hosted on servers.

What a sub-domain is:
A sub-domain is a subset of a larger domain, allowing further categorization of resources. For example, in "sub.example.com," "sub" is the sub-domain of "example.com."

How to define a port number in a URL:
A port number can be specified in a URL by adding a colon followed by the port number after the domain. For example, "http://example.com:8080" specifies port 8080.

What a query string is:
A query string is a part of a URL that follows the path and is used to pass parameters to a resource. It starts with a question mark and includes key-value pairs, typically separated by "&" symbols.

What an HTTP request is:
An HTTP request is a message sent by a client (e.g., a web browser) to a server, requesting a specific resource. It includes information like the request method, headers, and potentially a message body.

What an HTTP response is:
An HTTP response is the server's reply to an HTTP request. It contains the requested data, along with status information, headers, and sometimes a message body.

What HTTP headers are:
HTTP headers are additional pieces of information sent with an HTTP request or response. They provide metadata about the message, such as content type, length, and caching directives.

What the HTTP message body is:
The HTTP message body is the optional data sent with an HTTP request or response. For example, when submitting a form, the form data is typically included in the message body.

What an HTTP request method is:
An HTTP request method specifies the action to be performed on the resource. Common methods include GET (retrieve data), POST (send data), PUT (update data), and DELETE (remove data).

What an HTTP response status code is:
An HTTP response status code is a numeric code included in the server's response to indicate the outcome of the request. For example, 200 indicates success, while 404 indicates that the requested resource was not found.

What an HTTP Cookie is:
An HTTP Cookie is a small piece of data that a web server sends to a user's browser. The browser stores this data and includes it in subsequent requests, allowing the server to maintain stateful interactions with the client.

How to make a request with cURL:
cURL is a command-line tool for making HTTP requests. To use it, open a terminal and type: curl [options] [URL]. For example, curl https://www.example.com.

What happens when you type google.com in your browser (Application level):

1. Your browser checks its local cache for a previously visited version of google.com to load it faster.
2. If not found, your browser sends a DNS (Domain Name System) request to resolve "google.com" to an IP address.
3. Once the IP address is obtained, your browser opens a TCP connection to the server.
4. It sends an HTTP GET request to the server for the "/" path of the resource.
5. The server processes the request, generates an HTTP response, and sends it back.
6. Your browser receives the response, which includes HTML, CSS, JavaScript, and possibly more resources.
7. The browser renders the page, executing JavaScript and making additional requests for resources referenced in the page.
8. The webpage is displayed on your screen, and further interactions lead to more HTTP requests and responses.
