tasks = ["A","A","A","A","A","B","B","C","C","D","D","E"]
n = 3
rest = 0
while True:
    i = 0
    index = 0
    prev = set()
    while index < len(tasks) and i < n:
        if tasks[index] not in prev:
            prev.add(tasks[index])
            tasks.pop(index)
            i += 1
        index += 1
    if len(tasks) == 0:
        rest += i
        break
    else:
        rest += n
print(rest)

    