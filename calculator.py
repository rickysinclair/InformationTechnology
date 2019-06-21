# prompt user for input
num1 = int(input("Enter a number: "))
oper = input("Enter the operator: ")
num2 = int(input("Enter a number: "))

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

# display results
print(num1, oper, num2, "=", ans)
