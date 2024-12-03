lr=int(input('enter a upper range:'))
ur=int(input('enter a lower range:'))

print('prime number between',lr,'and',ur,'are:')

for num in range(lr,ur +1):
    if num > 1:
        for i in range(2,num):
            if (num % i)==0:
                break
            else:
                 print(num)    