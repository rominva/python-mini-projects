# "input" will get data from users
# num1 & num2 are strings but they souldn't!
# "int" or "float" to change it from a string to number

while True:
    num1 = float(input("\n💜 Enter your first number: "))
    num2 = float(input("💛 Enter your second number: "))
    oper = input("🧡 Enter the operation: ")
    print(f"💚 the resault of <<{num1} {oper} {num2}>> is:")

    if oper == "+":
        print(num1 + num2)
    elif oper == "-":
        print(num1 - num2)
    elif oper == "*":
        print(num1 * num2)
    elif oper == "/":
        print(num1 / num2)
    elif oper == "^":
        print(num1 ** num2)

    else:
        print("wrong data!")
