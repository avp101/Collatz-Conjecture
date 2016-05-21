#python_solution
n = input("What's the number?")
step = 0
while n>1:
    if n%2==0:
        n = n/2
        x+=1
    else:
        n=n*3+1
        x+=1
print(x)
