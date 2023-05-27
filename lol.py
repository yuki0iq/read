import time, codecs, os
i, b = map(int, input().split())
f = codecs.open("out" + str(i) + ".txt", "r", "utf-8")
L = f.readlines()
for i in range(b, len(L)):
	length = len(L[i])
	print("\x1b[1J" + str(i)+"\t"+L[i][:-1])
	time.sleep(0.4 + 0.4 * length / 40)
