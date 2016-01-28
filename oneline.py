import sys

onelinePre = '|:> compressed with oneline https://github.com/Heestand/oneline <:|:> '
onelinePost = ' <:|'

path = sys.argv[1]

file = open(path, 'r')
content = file.read()
file.close()

if int(sys.argv[2]):
	content = onelinePre + content.replace('\n', '[n]').replace('\t', '[t]').replace('    ', '[t]') + onelinePost
	print('oneline compressed')
else:
	content = content.replace(onelinePre, '').replace('[n]', '\n').replace('[t]', '\t').replace(onelinePost, '')
	print('oneline uncompressed')

file = open(path, 'w')
file.write(content)
file.close()
