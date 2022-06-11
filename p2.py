
from pickle import FALSE, TRUE


def check_prime_number(num):
    pri = TRUE
    if (num <2):
        pri = FALSE
        return pri
    for p in range(2, num):
        if num % p == 0:
            pri = FALSE
            break
        else:
            pri = TRUE
    return pri

num = int(input("enter your number"))


check = check_prime_number(num)
if check == TRUE:
    print(num," is prime")
else:
    print(num,"is not prime")