import time;
with open("input.txt", "r") as f:
    startTime = time.time()
    text = f.readlines()
    numbers = []
    total = 0
    for i in text:
        i = i.replace("twone", "21")
        i = i.replace("oneight", "18")
        i = i.replace("nineight", "98")
        i = i.replace("threeight", "38")
        i = i.replace("eightwo", "82")
        i = i.replace("fiveight", "58")
        i = i.replace("sevenine", "78")
        i = i.replace("eighthree", "83")

        i = i.replace("one", "1")
        i = i.replace("two", "2")
        i = i.replace("three", "3")
        i = i.replace("four", "4")
        i = i.replace("five", "5")
        i = i.replace("six", "6")
        i = i.replace("seven", "7")
        i = i.replace("eight", "8")
        i = i.replace("nine", "9")

        for j in range (0, len(i)):
            if i[j].isdigit():
                num1 = i[j]
                break
        for k in range(len(i)-1, -1, -1):
            if i[k].isdigit():
                num2 = i[k]
                break
        total += (int(num1) * 10) + int(num2)
    print(total)
    print(time.time() - startTime)