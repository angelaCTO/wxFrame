import socket
import time
UDP_IP_RX = "192.168.240.2"
UDP_IP_TX = "192.168.240.1"
UDP_PORT = 30444

MESSAGE1 = "Calling HTPA series devices"
MESSAGE2 = "Bind HTPA series device"
MESSAGE3 = "M"
MESSAGE4 = "k"
MESSAGE5 = "t"

MSG = [MESSAGE1,MESSAGE2,MESSAGE3,MESSAGE4,MESSAGE5]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_RX, UDP_PORT))
sock.settimeout(0.25)

i = 0
data = []
buffer = []        
stop = False
while stop is False:
    try:
        data = sock.recv(2048) # buffer size is 1024 bytes
    except:
        data = [] 
    if len(data) != 0 :
        #print "received message len:", len(data)
        if len(data) == 1058 :
            buffer = data
        elif len(data) == 1054:
            buffer = buffer + data
            print "received message len:", len(buffer)
#            stop = True
        elif len(data) < 1000 :
            print "received message len:", len(data)
            print "received message :", data
    else :
        if i < len(MSG):
            print "Sending  message:", MSG[i]
            sock.sendto(MSG[i], (UDP_IP_TX, UDP_PORT))
            i = i + 1
            time.sleep(1)
