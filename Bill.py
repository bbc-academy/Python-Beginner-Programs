print("Hello, I am a Bill Generator")
print("I have been developed by BBC Academy!")

print("Enter any 5 Product's name : ")
prod1=input("")
prod2=input("")
prod3=input("")
prod4=input("")
prod5=input("")

print("Enter the Cost of these 5 products : ")
cost1=int(input())
cost2=int(input())
cost3=int(input())
cost4=int(input())
cost5=int(input())

print("Enter the Quantity purchased for each product : ")
qty1=int(input())
qty2=int(input())
qty3=int(input())
qty4=int(input())
qty5=int(input())

t1=cost1*qty1
t2=cost2*qty2
t3=cost3*qty3
t4=cost4*qty4
t5=cost5*qty5

gt=t1+t2+t3+t4+t5

print("-----------------------------------------------------------------------------------")
print("\t\t\tBBC Shop")
print("-----------------------------------------------------------------------------------")

print("Prod\t\tCost\tQty\tTotal")
print(prod1,"\t\t",cost1,"\t",qty1,"\t",t1)
print(prod2,"\t\t",cost2,"\t",qty2,"\t",t2)
print(prod3,"\t\t",cost3,"\t",qty3,"\t",t3)
print(prod4,"\t\t",cost4,"\t",qty4,"\t",t4)
print(prod5,"\t\t",cost5,"\t",qty5,"\t",t5)
print("Grand Total :",gt)