my_dict = {}
with open("text_6.txt", encoding="utf-8") as file:
    for line in file:
        name, hour = line.split(":")
        name_sum = sum(map(int, "".join([i for i in hour if i == " " or ("0" <= i <= "9")]).split()))
        my_dict[name] = name_sum
print(f"{my_dict}")
