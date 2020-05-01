count = 1;
compileFile = open('compiledHistories.txt', 'w')

while count < 401:
	print('Processing file ' + str(count))
	fileName = str(count) + '.txt'
	file = open(fileName, 'r')
	lines = file.readlines()
	breakLine = '\n'
	lines.insert(0, breakLine)
	compileFile.writelines(lines)
	file.close()
	count = count + 1
	
compileFile.close()