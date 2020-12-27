import socket
import time
import colorama
from colorama import Fore, Style

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = '192.168.43.30'
port = 8888

c.connect((host,port))

colorama.init()
print(Fore.YELLOW + Style.BRIGHT)
print('\n***DOMAIN RESOLVER APPLICATION***\n')

file = open('history.txt','w')
while True:
	print(Fore.YELLOW)
	msg = input('\nEnter a Domain | history | \'end\' to exit: ')
	c.sendto(msg.encode('utf-8'),(host,port))

	if msg == "end":
		print('\nConnection ended...')
		False
		time.sleep(1)
		break

	if msg != 'history' and msg != '':
		data, addr  = c.recvfrom(1024)

		if data.decode('utf-8') != 'Not a proper domain':
			print('Resolve to : ', data.decode('utf-8'))
			file.write(msg + ' resolve to ' + data.decode('utf-8') + '\n')
		else:
			print(Fore.RED)
			print(data.decode('utf-8'))

	elif msg == 'history':
		print('\n*****History*****')
		file = open('history.txt','r')
		print(file.read())
		file = open('history.txt','a')

file.close()
c.close()
