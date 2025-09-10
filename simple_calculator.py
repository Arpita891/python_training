#simple calculator
print("Enter the number you want to calulate")
num_1 = input(int())
num_2 = input(int())
print("Choose your operation +,-,* : ",)
op = input()
if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "*":
    print(num_1 * num_2)
else:
    print("Calculation Not Possible")





