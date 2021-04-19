"""FAULTY CALCULATOR"""
#PROJECT 2: MAKE A FAULTY CALCULATOR THAT GIVES SOME WRONG CALCULATIONS ON SPECIFIES VALUES
#OBJECTIVES:
#Use this calculations to made fault 555 * 2 = 45, 56 + 4 = 75 , 56/7 = 2
#design a program that takes operator and 2 numbers then print answer but when user use above calculations he got wrong answer


print("Enter 1st Number")                   #Ask Your 1st Number

n1 = int(input())                           #Takes Your 1st Number

print("Enter 2nd Number")                   #Ask Your 2nt Number

n2 = int(input())                           #Takes Your 2nd Number

print("Enter The Operator You Wanna Use")   #Ask Your Operator

op=input()                                  #Takes Your operator

if n1 ==555 and n2 == 2 and op=='*':        #Start If Loop And Initialiaze Condition

    print("45")

elif n1 == 56 and n2 == 4 and op=="+":      #Start elIf Loop And Initialiaze Condition

    print("75")

elif n1 == 56 and n2 == 7 and op=="/":      

    print("2")

else:                                       #Start else Loop And Initialiaze Condition of Simple Calculator
    if op=="+":
        ans=n1+n2
    elif op=="-":
        ans=n1-n2
    elif op=="*":
        ans=n1*n2
    else:
        ans==n1/n2

print(ans)                                  #Prints Answer
