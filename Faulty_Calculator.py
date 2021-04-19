"""FAULTY CALCULATOR"""
#PROJECT 2: MAKE A FAULTY CALCULATOR THAT GIVES SOME WRONG CALCULATIONS ON SPECIFIES VALUES
#OBJECTIVES:
#Use This Calculations to made fault 555 * 2 = 45, 56 + 4 = 75 , 56/7 = 2
#design a program that takes operator and 2 numbers then print answer but when user use above calculations he got wrong answer

print("Enter 1st Number")
n1 = int(input())
print("Enter 2nd Number")
n2 = int(input())
print("Enter The Operator You Wanna Use")
op=input()

if n1 ==555 and n2 == 2 and op=='*':
    print("45")
elif n1 == 56 and n2 == 4 and op=="+":
    print("75")
elif n1 == 56 and n2 == 7 and op=="/":
    print("2")
else:
    if op=="+":
        ans=n1+n2
    elif op=="-":
        ans=n1-n2
    elif op=="*":
        ans=n1*n2
    else:
        ans==n1/n2
print(ans)
