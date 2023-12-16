with open('input.txt', 'r') as f:
    datas = f.read().strip().split(',')
    totalSum = 0
    for data in datas:
        temp = 0
        for char in data:
            temp += ord(char)
            temp *= 17
            temp %= 256
        totalSum += temp
    print(totalSum)