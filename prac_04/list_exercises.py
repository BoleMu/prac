def main_1():
    numbers = []
    for n in range(1, 6):
        number = int(input("Number: "))
        numbers.append(number)
    average = sum(numbers) / len(numbers)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the number is {average}")

def main_2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    username = input("Enter your username: ").lower()
    if username in usernames:
        print("Access granted")
    if username not in usernames:
        print("Access denied")

# main_1()
main_2()