name = input("Файл: ")
a = open(name, "w", encoding="utf-8")
while True:
    s = input()
    if s == " ":
        break
    a.write(s+"\n")
a.close()
