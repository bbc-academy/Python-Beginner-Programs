i=1
n=int(input("Enter the range for loop : "))

sumEven = sumOdd = 0

while i<=n:
    print(i)
    if i%2==0:
        sumEven+=i
    else:
        sumOdd+=i
    i+=1

print("The sum of All Even Numbers is :",sumEven,"and Odd Numbers is :",sumOdd)