print("Enter any 3 numbers : ")

num1, num2, num3 = int(input()), int(input()), int(input())

if num1>num2 and num1>num3:
    print(num1,"is largest.")
elif num2>num1 and num2>num3:
    print(num2,"is largest.")
else:
    print(num3,"is largest.")

input()