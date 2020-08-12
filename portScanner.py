#Libraries Required#
import socket
import threading
from queue import Queue

target = "###.###.#.#"  #The default gateway value you get from ipconfig in cmd prompt#
queue = Queue()
open_ports = []

def postScan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        return True
    except:
        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if postScan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

#Using multi-threading#
port_list = range(1,1024)
fill_queue(port_list)
thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are ", open_ports)

#Without using multi-threading#
#for port in range(1,1024):
    #result = postScan(port)
    #if result:
        #print("Port {} is open!".format(port))
    #else:
        #print("Port {} is closed".format(port))
