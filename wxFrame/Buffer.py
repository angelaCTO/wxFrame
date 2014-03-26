import threading

bufferLock = threading.Lock()
globalBuffer = None

def initBuffer(size):
    global globalBuffer
    global bufferLock

    bufferLock.acquire()
    globalBuffer = [0] * size
    bufferLock.release()

def getBuffer():
    global globalBuffer
    global bufferLock

    bufferLock.acquire()
    tempBuffer = list(globalBuffer)
    bufferLock.release()

    return tempBuffer

def setBuffer(buffer):
    global globalBuffer
    global bufferLock

    bufferLock.acquire()
    globalBuffer = list(buffer)
    bufferLock.release()



