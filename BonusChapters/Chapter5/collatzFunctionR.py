#Recursive version of the collatz function I did on chapter 4

def collatzFunction(num):
    num = abs(num)
    if num <= 1:
        print(num)
        return
    else:
        if num % 2 == 0:
            print(num, end=" ")
            return collatzFunction(num // 2)
        else:
            print(num, end=" ")
            return collatzFunction(num * 3 + 1)

myNum = -10
collatzFunction(myNum)
