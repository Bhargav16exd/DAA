def karatsuba(number):

    if  number < 10 :
        return number*number
    
   
    strNum = str(number)
    length = len(strNum)

    mid = length // 2 

    low = int(strNum[:mid])
    high = int(strNum[mid:])

    p1 = karatsuba(low)
    p2 = karatsuba(high)
    p3 = karatsuba(low+high) - p1 - p2 

    return (p1 * 10**(2*(length - mid))) + (p3 * 10**(length-mid) ) + p2


number = input("Enter Number to Square ")
result = karatsuba(int(number))

print(result)