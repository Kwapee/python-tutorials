#This is the break loop
num = int(input('Please enter a number: '))
for i in range(0,6):
    if i==num:
        break
    print(i,' ',end=' ')
print('Done')
