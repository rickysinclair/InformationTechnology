# prompt user for input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
oper = input("Enter the operator: ")

# perform calculations
if oper == "*":
    ans = num1 * num2
elif oper == "-":
    ans = num1 - num2
elif oper == "+":
    ans = num1 + num2
elif oper == "/":
    ans = num1 / num2
else:
    print("You have entered an invalid operator")
    exit()

print(num1, oper, num2, "=", ans)
