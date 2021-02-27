import operator
from pwn import *
import sys

context.log_level = 'error'

# flag{f0ll0w_th3_whit3_r@bb1t}
flag = ''

if len(sys.argv) > 1:
	for i in range(0, 10):
		io = remote('challenges.ctfd.io', 30468)
		io.recv()
		io.send(f'{flag}\n')
		r = str(io.recv(), 'utf-8')
		#print(r)
		try:
			print(r.split('\r\n')[1], r.split('\r\n')[4])
		except:
			print("[!] Error\n" + r)

	sys.exit()

while True:
	if flag.endswith('}'):
		print('Flag: ' + flag)
		sys.exit()

	keys = set()
	while len(keys) < 3:
		try:
			io = remote('challenges.ctfd.io', 30468)
			io.recv()
			io.send(f'{flag}\n')
			r = str(io.recv(), 'utf-8')
		except:
			continue

		try:
			keys.add(r.split('\r\n')[4])
		except:
			continue

	chars = {}
	for i in (keys):
		for j in (0x10, 0x77, 0x02):
			c = str(xor(int(i, 16), j), 'ascii')
			if not c.isprintable():
				continue
			if c in chars:
				chars[c] += 1
			else:
				chars[c] = 1
	
	print(flag)		
	#print(chars)
	#print(keys)
	
	if len(chars) == 0:
		continue
	c = max(chars.items(), key=operator.itemgetter(1))[0]
	if c.isprintable():
		flag += c

	


"""
Remote: 159.203.148.124

f = 0x76, 0x11, 0x64 = 0x10, 0x77, 0x02
l = 0x6e, 0x7c, 0x1b = 0x02, 0x10, 0x77
a = 0x16, 0x63, 0x71
g = 0x77, 0x10, 0x65
{ = 0x79, 0x6b, 0x0c
f = 0x76, 0x64, 0x11
?? = 0x47, 0x20, 0x32

- Changing local IP makes no difference!


"""