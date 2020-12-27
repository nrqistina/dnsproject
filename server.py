import socket
import time
import colorama
from colorama import Fore, Style

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = ''
port = 8888

s.bind((host,port))

colorama.init()
print(Style.BRIGHT)
print(Fore.CYAN)
print('Waiting for connection...\n')

file = open('history.txt','a')
while True:

	data, addr = s.recvfrom(1024)

	if data == b'end':
		False
		print(Style.BRIGHT)
		print('\nHistory')
		file = open('history.txt','r')
		print(file.read())
		time.sleep(1)
		print('Connection ended...\n')
		time.sleep(1)
		break

	if data != b'end' and data != b'history' and data != b'':
		print('Connected to ', addr)
		try:
			ipaddr = socket.gethostbyname(data)
			print(data.decode('utf-8'),'\n')
			message = (ipaddr).encode('utf-8')
			s.sendto(message,addr)
			file_data = data
			file.write(str(file_data) + '\n')
		except:
			print('Wrong domain\n')
			s.sendto(b'Not a proper domain',addr)


file.close()
s.close()
