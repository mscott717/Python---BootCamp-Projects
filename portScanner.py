import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifies IPV4 connection and a UDP conenction (sock stream)
s.settimeout(5)


host = input("Please enter the IP you want to scan: ")#need to put an IP address to scan
port = int(input("Please enter the port you want to scan: "))




def portScanner(port): #define the functin portScanner
    if s.connect_ex((host,port))
    print("The port is closed") 

    else: 
        print ('The port is open!')

portScanner(port)        