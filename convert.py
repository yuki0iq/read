import codecs
import re

STRING_LEN = 40

def LineSplit(line):
	# str -> [str (sizes <= 30)]
	line = line + ' '
	sents = []
	i = 0
	while i < len(line):
		v = []
		for c in '?!.':
			j = line.find(c, i, i+STRING_LEN)
			if j != -1:
				v += [j]
		for c in ', ':
			j = i + line[i:i+STRING_LEN].rfind(c)
			if j != -1:
				v += [j]
		v = sorted(v)
		if len(v) == 0:
			v = [-1]
		if v[-1] - i > STRING_LEN:
			print("Long line!")
		j = v[-1]
		#print(v, sents)
		sents += [line[i:j + 1]]
		i = j + 1
	return sents

#print('\n'.join(LineSplit('Кудряш. Вчетвером этак, впятером в переулке где-нибудь поговорили бы с ним с глазу на глаз, так он бы шелковый сделался. А про нашу науку-то и не пикнул бы никому, только бы ходил да оглядывался.')))
#input()

f = codecs.open("in.txt", "r", "utf-8")
L = f.readlines()
LL = [ [] ]
for i in L:
	if i == "#\n":
		LL.append([])
	else:
		LL[-1].append(i[:-1])
for i in range(1, len(LL)):
	LL[i] = LL[0] + LL[i]
LL = LL[1:]
#print(LL)
LinesConverted = []
for Lines in LL:
	LinesConverted.append([])
	for Line in Lines:
		if len(Line) <= STRING_LEN:
			LinesConverted[-1].append(Line)
		else:
			LinesConverted[-1] += LineSplit(Line)
for i in range(len(LinesConverted)):
	codecs.open("out" + str(i) + ".txt", "w", "utf-8").write('\n'.join(LinesConverted[i]))
