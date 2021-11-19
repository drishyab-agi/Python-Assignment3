def rec_fact(n):
    if n==1:
        return n
    else:
        return n*rec_fact(n-1)
num=4
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of ",num,"is ",rec_fact(num))