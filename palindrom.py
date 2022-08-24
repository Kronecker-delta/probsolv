def palindrome_check(num):
    return str(num) == str(num)[::-1]


def step_to_pal(num):
    count = 0
    while not palindrome_check(num):
        num += int(str(num)[::-1])
        count += 1
        print(count,num)    
    return count
# max = 0
# for num in range(200):
#     current = step_to_pal(num)
#     print(num,current)
#     if max < current:
#         max = current

# print(max)

print(step_to_pal(196))