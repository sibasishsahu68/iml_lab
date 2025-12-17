a=int(input("enter a number :"))
b=int(input("enter a number :"))
c=int(input("enter a number :"))
d=int(input("enter a number :"))
e=int(input("enter a number :"))
f=int(input("enter a number :"))
g=int(input("enter a number :"))

mean = (a+b+c+d+e+f+g)/7
print("Mean is :",mean)


nums = [a, b, c, d, e, f, g]


for i in range(7):
    for j in range(6 - i):
        if nums[j] > nums[j + 1]:    
            nums[j], nums[j + 1] = nums[j + 1], nums[j]


median = nums[3]


mode = nums[0]
max_count = 0

for i in range(7):
    count = 0
    for j in range(7):
        if nums[i] == nums[j]:     
            count += 1
    if count > max_count:
        max_count = count
        mode = nums[i]


print("Median =", median)
print("Mode =", mode)
