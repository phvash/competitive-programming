def f(num):
    global count
    count += 1
    if num == 0:
        return 0
    sum_of_digits = sum(map(int, str(num)))
    f(num - sum_of_digits)


global count
count = 0

num = int(input())
f(num)
    
print(count)
