
import socket
def ip_tester():
    
    
    remoteServer    = input('Enter a remote host to scan: ')
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print ('-' * 60)
    print ('Please wait, scanning remote host', remoteServerIP)
    print ('-' * 60)
    
            
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ('Port {}: 	 Open'.format(port))
            ret = sock.recv(port)
            print('SERVICE:',str(ret))
