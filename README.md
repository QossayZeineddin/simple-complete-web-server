# simple-complete-web-server

 Using socket programming, implement a simple but a complete web server in python or java or C that is listening on port 9000. The user types in the browser something like http://localhost:9000/ or http://localhost:9000/index.html or http://localhost:9000/image.png, etc
The program should check 
    1- if the request is / or /index.html (for example localhost:9000/ or localhost:9000/index.html) then the server should send index.html file with Content-Type: text/html. 
The index.html file should contain 
HTML webpage that contains 
    1- “ENCS3320 Simple Webserver” in the title
    2- “Welcome to our course Computer Networks” (part of the phrase is in Green)
    3- Group members names and IDs
    4- Some information about the group members. For instance, projects you have done during different course (programming, electrical, math, etc), skills, hobbies, etc.
    5- Use CSS to make the page looks nice (for example, you can divide the page using CSS)
    6- An image with extention.jpg and an image with extension .png


    2- if the request is /imagename.png then the server should send the png image with Content-Type: image/png. You can use any image.
    3- if the request is /imagename.jpg then the server should send the jpg image with Content-Type: image/jpeg. You can use any image.


    4- Include a text file (or you can use csv file) that contains names and prices of at least 5 smartphones 
    5- if the request is /SortName then the output on the browser should be the names and prices of the smartphones sorted by the name. The server should send text page with Content-Type: text/plain. I you wish, you can use text/html to display the output in a more convenient way.

    6- if the request is /SortPrice then the output on the browser should be name and price of the smartphones sorted by its price. The server should send text page with Content-Type: text/plain. I you wish, you can use text/html to display the output in a more convenient way.

    7- If the request is wrong or the file doesn’t exist the server should return a simple HTML webpage that contains (Content-Type: text/html)
    1-  “HTTP/1.1 404 Not Found” in the response status
    2- “Error” in the title
    3- “Not Found” in the body 
    4- Your names and IDs in Bold
    5- The IP and port number of the client


The program should print the HTTP requests on the terminal window (command line window).
Provide screenshots of the browser to show that your project works as expected. (/index.html /imagename.png,  /SortName, etc.) . Test the project from a browser on the same computer and from a different computer or phone.
Provide also a screenshot of the HTTP request printed on the command line. 

Hint: Have a look on HTTP response in Listing 1 and the HTML code In Listing 2. You may use the minimal header and HTML code. Have a look also on rfc2616 (https://tools.ietf.org/html/rfc2616)
HTTP/1.1 200 OK 
Connection: close
Date: Fri, 03 Mar 2017 06:19:37 GMT
Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.1e-fips PHP/5.4.16
Last-Modified: Fri, 03 Mar 2017 05:28:07 GMT
Content-Length: 6821 
Content-Type: text/html
data data data data data ...

Listing 1: HTTP Response
<!DOCTYPE html>
<html>
<head><title >XYZ Company INC.</ title ></head>
<body><h1>Welcome <b>XYZ</b> Company</h1>
<img src="http:www. xyz.com/ images / logo.gif " ALT="XYZ Logo"><br>
We are so happy that you have chosen to visit our website.
</body>
</html>
Listing 2: Simple HTML Code
[ProjectNetwork.pdf](https://github.com/QossayZeineddin/simple-complete-web-server/files/8430365/ProjectNetwork.pdf)
