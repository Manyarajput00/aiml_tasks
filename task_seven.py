my_file=open("seven.txt", "r")

my_text = my_file.read()
print(my_text)

my_text = my_file.readline()
print(my_text)

my_text = my_file.readline()
print(my_text)

my_text = my_file.readlines()
print(my_text)

my_file.close()

with open ('seven.txt','w') as oko:
    oko.write("i am manya i do not msg him anymore you are nou disturbing him he is not the manner he before mind it \n")
    oko.write("npu focus on you you have a lot to do \n")
    oko.write("i --- IGNORE ---\n")

with open ('seven.txt' , 'r') as reddy:
    reddy_text = reddy.read()
    print(reddy_text)