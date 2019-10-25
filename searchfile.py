# 扫描当前目录和所有子目录并显示大小

import os
import sys
try:
	directory = sys.argv[1] #sys.args[]:实则为列表,里面的项为用户输入的参数
except IndexError:
	sys.exit("Must provide an argument.")

dir_size = 0
fsizedicr = {
	'Bytes': 1,
	'Kilobytes': float(1)/1024,
	'Megabytes': float(1)/(1024*1024),
	'Gigabytes': float(1)/(1024*1024*1024)
}

for (path, dirs, files) in os.walk(directory):
	#path:表示当前文件夹所在地址
	#dirs:list,表示当前文件夹中所有的目录的名字
	#files:list,表示当前文件夹中所有的文件
	for file in files:
		filename = os.path.join(path, file)
		dir_size += os.path.getsize(filename)
		# print(filename)

fsizeList = [str(round(fsizedicr[key] * dir_size, 2)) + " " + key for key in fsizedicr]

if dir_size==0:
	print('File Empty')
else:
	for units in sorted(fsizeList[::-1]):
		print('Foler Size: ' + units)