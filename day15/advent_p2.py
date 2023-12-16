def calculateHash(data):
    totalSum = 0
    for char in data:
        totalSum += ord(char)
        totalSum *= 17
        totalSum %= 256
    return totalSum

with open('input.txt', 'r') as f:
    datas = f.read().strip().split(',')
    boxes = {}
    for i in range(256):
        boxes[i] = []
    
    for data in datas:
        if '-' in data:
            start = data[:-1]
            hash = calculateHash(start)
            
            for i in range(len(boxes[hash])):
                if start in boxes[hash][i]:
                    del boxes[hash][i]
                    break
        if '=' in data:
            start, end = data.split('=')
            hash = calculateHash(start)
            for i in range(len(boxes[hash])):
                if start in boxes[hash][i]:
                    boxes[hash][i] = start + ' ' + end
                    break
            else:
                boxes[hash].append(start + ' ' + end)
    
    totalSum = 0
    for key, value in boxes.items():
        if len(value) == 0:
            continue

        boxNum = key + 1 # Box number
        i = 1 # Slot number
        for lens in value:
            totalSum += boxNum * i * int(lens.split(' ')[1]) # Box number * Slot number * Focal length
            i += 1
        
    print(totalSum)