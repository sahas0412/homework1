x=int(input("enter your number ="))
p=0
for i in range(1,x+1):
    if i % 2 == 0:
        p += i
    else:
        continue
print(p)