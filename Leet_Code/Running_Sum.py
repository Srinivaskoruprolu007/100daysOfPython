nums = list(map(int, input("Enter the list values: ").split(" ")))
print(nums)
r_nums = []
total = 0
for i in nums:
    total += i
    r_nums.append(total)

print(r_nums)