import threading
import time
import os
import subprocess
import re
import socket
import time
import Buffer

packet = [0] * 992
udp_thread = None

barrierLock = threading.Lock()
barrier = False
packetList = []

def listReduce(a):
    b= [0] * (len(a) / 2)
    for i in range (len(a) / 2) :
        #b[i] = int(ord(a[2*i])* 256 + ord(a[2*i + 1]))
        b[i] = int(ord(a[2*i]))
    return b

def swap(a):
    b = [0] * 992
    for i in range(31) :
        l = i * 32
        for j in range (16) :
            b[l + j] = a [l + 2*j]
        for k in range (16) :
            b[l + k + 16] = a [l + 2*k + 1]
    return b

class udp (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        global barrier

        print "Starting " + self.name
        #Init the packet
        UDP_IP_RX = "192.168.240.3"
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

        data = []
        buffer = []
        i = 0
        while True:
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

                    buffer = swap(listReduce(buffer))

                    Buffer.setBuffer(buffer)

                    print "Grid", len(buffer)
                    print buffer[0]

                    barrierLock.acquire()
                    barrier = True
                    barrierLock.release()

                elif len(data) < 1000 :
                    print "received message len:", len(data)
                    print "received message :", data
            else :
                if i < len(MSG):
                    print "Sending  message:", MSG[i]
                    sock.sendto(MSG[i], (UDP_IP_TX, UDP_PORT))
                    i = i + 1
                    time.sleep(1)

def init():
    global udp_thread
    global barrier

    udp_thread = udp(1, "UDP Thread")
    udp_thread.start()
    flag = False

    while flag is False:
        barrierLock.acquire()
        flag = barrier
        barrierLock.release()

if __name__ == '__main__':
    init()

