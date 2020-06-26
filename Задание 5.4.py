with open("text_4.txt", "r", encoding="utf-8") as read, open("translate", "w", encoding="utf-8") as wr:
    element = ""
    for index in read:
        for i in index.split(" "):
            if i == "One":
                i = "Один"
            elif (i == "Two"):
                i = "Два"
            elif (i == "Three"):
                i = "Три"
            elif (i == "Four"):
                i = "Четыре"
            element = element + " " + i
        wr.write(element)
        element = ""
