import socket
from encrypt import reverse_decrypt
from encrypt import caesar_decrypt
from encrypt import rot_decrypt
from encrypt import transposition_decrypt

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   

port = 8080
s.bind(('', port)) 
s.listen(5)
c,addr = s.accept()


recv = c.recv(1024)
fname = recv.decode('utf-8')
print("Filename : ",fname)

recv = c.recv(1024)
pr = recv.decode('utf-8')
print("Ch : ",pr)

recv = c.recv(1024)
ch = recv.decode('utf-8')
print("Choice: ",ch)

recv = c.recv(1024)
msg = recv.decode('utf-8')
print("Message Received : ",msg)

if pr == 'E':
    result = msg
elif pr == 'D':
    if ch == '1':
        result = reverse_decrypt(msg)
    elif ch == '2':
        result = caesar_decrypt(msg)
    elif ch == '3':
        result = rot_decrypt(msg)
    elif ch == '4':
        result = transposition_decrypt(msg)
    print("Decrypted Cipher : ",result)
        


f = open(fname,'w')
f.write(result)
f.close()
c.close()

