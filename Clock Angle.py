def count_cake(n):
    if n==2  or n==4 or n==6 or n==8 or n==10:
        return 'yes'
    if n==1 or n==3 or n==5 or n==7 or n==9:
        return 'no'
    if n==n+1:
        return 'not possible'
print(count_cake(4))
