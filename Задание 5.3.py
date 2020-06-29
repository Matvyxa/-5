with open("text_3.txt", "r", encoding="utf-8") as file:
    s_summa = []
    otsev = []
    line = file.read().split("\n")
    for i in line:
        i = i.split()
        if float(i[1]) < 20000:
            otsev.append(i[0])
        s_summa.append(i[1])


print(f"Сотрудники с окладом менее 20 тыс.{otsev}. \n"
      f"Cредняя величина дохода сотрудников: {sum(map(float, s_summa)) / len(s_summa)}")