# Mitchell Scott
# Cyber Security Bootcamp - ProjectB

from time import time
from datetime import datetime
import socket

file = open('portLog.txt', 'w')
userInput = input("Enter the host you want to scan: ")
hostIP = socket.gethostbyname(userInput)  # This also works if I input an IPV4 address

try:
    startTime = time()

    startDT = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    file.write("Starting Date and Time: {}\n".format(startDT))

    print("The IP address for {} is: {}".format(hostIP, hostIP))
    print("Scanning {} for open ports...".format(hostIP))

    for port in range(0, 1026):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = sock.connect_ex((hostIP, port))
        socket.setdefaulttimeout(0.025)  # made this number small to increase speed
        # print("Error code: {}".format(connection))
        # print(connection)
        if connection == 0:
            portString = "Port: {} is open\n".format(port)
            file.write(portString)
            print(portString)
            sock.close()

        else:
            print("Port: {} is closed".format(port))
            sock.close()

    endTime = datetime.now()

    totalTime = "{:.2f}".format(time() - startTime)
    print("Scanning time: {} seconds".format(totalTime))
    file.write("Scanning time: {} seconds\n".format(totalTime))
    endDT = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    file.write("Ending Date and Time: {}\n".format(endDT))

except socket.error:
    print("Host does not exist ")
    file.write("{} not available ".format(hostIP))
except KeyboardInterrupt:
    print("Program exited")
    file.write("Scan unable to complete, stopped by user")
except TypeError:
    print("Host does not exist")
    file.write("Host does not exist")

#
file.close()
#
#
