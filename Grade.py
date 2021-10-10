print("Enter your marks in 5 subjects : ")

sub1, sub2, sub3, sub4, sub5 = int(input()), int(input()), int(input()), int(input()), int(input())

total = sub1+sub2+sub3+sub4+sub5
per=total/5

if per >= 85:
    print("Your grade : A")
elif per >= 70:
    print("Your Grade : B")
elif per >= 60:
    print("Your Grade : C")
elif per >= 50:
    print("Your Grade : D")
else:
    print("Your Grade : Fail.")
    print("Chullu Bhar Paani Me Doob Maro..........!!!!!!!!!!")