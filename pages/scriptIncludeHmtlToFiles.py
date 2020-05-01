count = 1;

while count < 401:
	print('Processing file ' + str(count))
	fileName = str(count) + '.txt'
	file = open(fileName, 'r+')
	lines = file.readlines()
	paragraph = '<p id="h' + str(count) +'" hidden>\n'
	lines.insert(0, paragraph)
	lines.insert(len(lines), '\n</p>')
	file.seek(0)
	file.writelines(lines)
	file.close()
	count = count + 1