# Import socket module
from socket import *
# Assign a port number
serverPort = 9000
#Create a TCP server socket
# #(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to server address and server port
serverSocket.bind(('',serverPort))

#serverSocket.bind(('192.168.53.110', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)
print("The server is ready to receive")
# Server should be up and running and listening to the incoming connections

while True:
    # Set up a new connection from the client
    connectionSocket, addr= serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(addr)
    print(sentence)
    ip = addr[0]
    # list=sentence.split('/')
    request= sentence.split('/')
    R=request[1]
    port = addr[1]

    # Send the content of the requested 1 file to the client
    # when enter http://localhost:7000/1

    ss = R.split(' ')
    print ("*******************")
    rec = ss[0]
    print ("The Request")
    print (rec)
    print ("*******************")
    # to get index without HTTP
    if rec=='index.html'or rec=='':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        htmlFile = open('index.html','rb')
        connectionSocket.send(htmlFile.read())

    elif rec=='imagename.png':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s=open("network.png","rb")
        # Close the client connection socket
        connectionSocket.send(s.read())


    # Send the content of the requested 3 file to the client
    # when enter http://localhost:7000/3
    elif rec=='imagename.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s=open("dough.jpg","rb")
        # Close the client connection socket
        connectionSocket.send(s.read())




    elif rec == 'SortName':
        import pandas as pd
        df = pd.read_csv("list.csv")
        sorted_df = df.sort_values(by=["name"], ascending=True)
        # to save data in a file after sorting
        sorted_df.to_csv('nameSort.csv', index=False)

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        my_file = open("nameSort.csv", "r")
        content_list = my_file.readlines()
        html = " <html><head><title> sorted Name </title> <body> <h1><br><font color=\"red\"> Smart phone sorted name <br>  <font color=\"black\"> </h1> <h3><ol> <li> "+ content_list.__getitem__(0)  + "    <li>"+ content_list.__getitem__(1)  + " " \
            "   <li> "+ content_list.__getitem__(2)  + "   <li>  "+ content_list.__getitem__(3)  + "   <li> "+ content_list.__getitem__(4)  + "   <li> "+ content_list.__getitem__(5)  + " <li> "\
               + content_list.__getitem__(6)  + "  <li> "+ content_list.__getitem__(7)  + "  <li> "+ content_list.__getitem__(8)  + "  <li> "+ content_list.__getitem__(9)  + "  </ol>  </h3>"
        connectionSocket.send(html)


    elif rec == 'SortPrice':
        import pandas as pd

        df = pd.read_csv("list.csv")
        sorted_df = df.sort_values(by=["price"], ascending=True)
        # to save data in a file after sorting
        sorted_df.to_csv('priceSort.csv', index=False)

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())

        my_file = open("priceSort.csv", "r")
        content_list = my_file.readlines()
        html = " <html><head><title> sorted Price </title> <body> <h1><br><font color=\"red\"> Smart phone sorted Price <br>  <font color=\"black\"> </h1> <h3><ol> <li> " + content_list.__getitem__(0) + "" \
               "    <li>" + content_list.__getitem__(1) + "  <li> " + content_list.__getitem__(2) + "   <li>  " + content_list.__getitem__(3) + "   <li> " + content_list.__getitem__(4) + "" \
              "   <li> " + content_list.__getitem__(5) + " <li> " + content_list.__getitem__(6) + "  <li> " + content_list.__getitem__(7) + "  <li> " + content_list.__getitem__(8) + " " \
            " <li> " + content_list.__getitem__(9) + "  </ol>  </h3>"
        connectionSocket.send(html)

    elif rec == 'dough.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("dough.jpg", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())

    elif rec == 'screen.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("screen.jpg", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())


    elif rec == 'amr.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("amr.jpg", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())

    elif rec == 'qossay.png':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("qossay.png", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())
    elif rec == 'ameena.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("ameena.jpg", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())


    elif rec != 'SortPrice' and rec != 'SortName' and rec != 'imagename.jpg' and rec != 'magename.pnf' and rec != 'index.html' and rec !='' :
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html; charset=ISO-8859-1\r\n\r\n".encode())
        connectionSocket.send("<html><head><title> ERROR </title></head><body><h1><br><font color=\"red\"> Error request  not found<br>  <font color=\"black\"> </h1><h1>qossay zeinelddin 1180235</h1><h1>ameena jadallah 1171018"
                              "</h1><h1>Amr Shayeb 1171042</h1><h3>The IP {"+str(ip)+"}</h3><h3>The Port Number:{"+str(port)+"}</h3></body></html>")

        connectionSocket.close()

