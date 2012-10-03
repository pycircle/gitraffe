lines = []
for line in open('main_window.py'):
	x = line.split()
	if len(x)==0:
		continue
	if x[0]=='from':
		lines.append(line)
		lines.append("from os.path import dirname\n")
	elif '"icons' in x[0]:
		x[0]=x[0].replace('"icons', 'dirname(__file__) + "/icons')
		lines.append("        "+' '.join(x)+'\n')
	else:
		lines.append(line)
file = open('main_window.py', 'w')
for line in lines:
	file.write(line)
file.close()