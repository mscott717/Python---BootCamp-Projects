import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port))) 
    s.settimeout(5) #sets the timeout to 5 seconds 
    print(str(s.recv(1024)))

def main():
    ip = input("Pleae enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip,port)


main()
