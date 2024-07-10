a=int(input('enter 1st number'))
b=int(input('enter 2nd number'))
c=str(input('enter which operation you want to perform?'))
if c=='+':
    res=a+b
    print(res)
elif c=='-':
    res=a-b
    print(res)
elif c=='*':
    res=a*b
    print(res)
elif c=='/':
    res=a/b
    print(res)
else :
    print('wrong input')