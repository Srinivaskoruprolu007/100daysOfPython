def secondLargest(lis: list) -> int:
    mx = max(lis[0], lis[1])
    secondMax = min(lis[0], lis[1])
    length = len(lis)
    for i in range(2, length):
        if lis[i] > mx:
            secondMax = mx
            mx = lis[i]
        elif secondMax < lis[i] != mx:
            secondMax = lis[i]
        elif lis[i] != secondMax == mx:
            secondMax = lis[i]

    return secondMax


input_list = [12, 45, 6, 2, 6, 7, 60]
print(secondLargest(input_list))