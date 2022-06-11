num = int(input("enter your number"))
def is_int(num):
    isint = isinstance(num , int)
    if isint == True:
        print(f'{int(num)} is an integer')
    else:
        print(f'{num} is not an integer')
is_int(num)
