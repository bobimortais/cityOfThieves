count = 1;
pageToChange = open('index.html', 'r+')

while count < 401:
	print('Processing file ' + str(count))
	fileName = str(count) + '.txt'
	file = open(fileName, 'r+')
	lines = file.readlines()
	pageToChange.writelines(lines)
	file.close()
	count = count + 1
	
pageToChange.close()