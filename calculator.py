print("simple calculator ( + and - )")

num1 = float(input("enter first number: "))
op = input('choose an operator (+ or -): ')
num2=float(input("enter second number: "))

if op== "+":
    print("answer:", num1 + num2)
elif op == "-":
    print("answer:", num1 - num2)
else:
    print("invalid operator. please use + or -")
