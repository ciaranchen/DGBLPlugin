import socket  
  
address = ('127.0.0.1', 8003)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
while True:  
    msg = input()
    if not msg:  
        break
    s.sendto(msg.encode("utf-8"), address)  
  
s.close()  