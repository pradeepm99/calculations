
list = [2, 1, 3, 8, 12, 45, 12]

def median(list):
    list.sort()

    if len(list) % 2 == 1:
        med = list[len(list)//2]

    else:
        high = list[len(list)//2]
        low = list[len(list)//2 - 1]
        med = (high + low) / 2

    return med


print(median(list))
