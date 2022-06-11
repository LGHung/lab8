import math
num = int(input("enter your number"))
def sumdivi(num):
    global sum
    sum = 0
    for i in range (1 , num+1):
        facti = math.factorial(i)
        divi = facti / i
        sum = sum + divi
sumdivi(num)
print(sum)
