indexUpdated = open('indexUpdated.html', 'r+')
file = open('compiledHistories.txt', 'r')
lines = file.readlines()
breakLine = '\n'
lines.insert(0, breakLine)
indexUpdated.seek(164)
indexUpdated.writelines(lines)
file.close()	
indexUpdated.close()