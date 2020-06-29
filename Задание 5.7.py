import json
with open("text_7.txt.json", "w", encoding="utf-8") as j_file:
    with open("text_7.txt", encoding="utf-8") as my_file:
        company = {}
        pribl = {}
        a, b = 0, 0
        line = my_file.read().split("\n")
        for i in line:
            i = i.split()
            profit = int(i[2]) - int(i[3])
            company[i[0]] = profit
            if profit > 0:
                a += profit
                b += 1
            pribl["Средняя прибыль"] = a / b
        all_list = [company, pribl]
    json.dump(all_list, j_file, ensure_ascii=False, indent=4)
print(f"Информация о фирмах:\n{line}\n\nФинансовый отчет:\n{all_list}")



