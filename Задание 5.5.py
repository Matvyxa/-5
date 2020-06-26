inf = open("text_5.txt", "r", encoding="utf-8")
A = inf.read().split()
inf.close()
s = 0
for i in A:
    s += int(i)
B = open("Задание5.5.txt", "w", encoding="utf-8")
B.write(str(s) + "\n")
B.close()
