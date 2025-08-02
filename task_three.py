print('hello manya')
table_of=int(input('Enter a number to print its table: '))
i=1
while(i<=10):
    print(f'{table_of} x {i} = {table_of * i}')
    i += 1
    if(i==5):
        break
print('This is the end of the program.')


for i in range(1, 11): 
    if(i%2 == 0):
        continue
    else:
         print(f'{table_of} x {i} = {table_of * i}')
print('This is the end of the program.')