import sys
import time
from zipfile import ZipFile 

key = ''

for i in range(128, 0, -1):
	fileName = f'turtles{i}.zip'
	with ZipFile(fileName) as zf:
		try:
			zf.extractall(pwd=b'0')
			key += '0'
		except:
			try:
				zf.extractall(pwd=b'1')
				key += '1'
			except:
				print('[!] Error extracting:(')
				sys.exit()
	#time.sleep(0.01)

print(key)

"""
key = ed 57 0e 22 d4 58 e2 57 34 fc 08 d8 49 96 1d a9 / ed570e22d458e25734fc08d849961da9
pw  = 3d c9 06 f6 92 8e e8 82 cc b1 b8 bd d1 4a a2 26 / 3dc906f6928ee882ccb1b8bdd14aa226
flag = 66 6c 61 67