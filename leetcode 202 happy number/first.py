n = 19 #### solved but not optimal
data = set()
while n not in data:
    data.add(n)
    string = str(n)
    add = 0
    for x in string:
        add = add + (int(x)*int(x))
    n = int(add)
    # print("True")
    if n == 1:
        # return True
        print("True")
# return False