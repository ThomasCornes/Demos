# def main():
#     incomes = []
#     Months_of_operation = int(input("How many months? "))
#
#     for month in range(1, Months_of_operation + 1):
#         income = float(input("Enter income for month " + str(month)))
#         incomes.append(income)
#
#     print("\nIncome Report\n-------------")
#     total = 0
#     for month in range(1, Months_of_operation + 1):
#         income = incomes[month - 1]
#         total += income
#         print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
# main()

# FILENAME = "subject_data.txt"
#
#
# def main():
#     data = get_data()
#     print(data)
#
#
# def get_data():
#     input_file = open(FILENAME)
#     for line in input_file:
#         print(line)
#         print(repr(line))
#         line = line.strip()
#         parts = line.split(',')
#         print(parts)
#         parts[2] = int(parts[2])
#         print(parts)
#         print("----------")
#     input_file.close()
#
#
# main()
# numbers = []
# max_numbers = 5
# option_number = 0
# option = 0
# def main():
#     while max_numbers <= 5:
#         option = option_number + 1
#         option = float(input("what number would you like to add to list"))
#         numbers.append(option)
#     else:
#         print("Your list of numbers is",numbers)
#         print("Your first number is",numbers.len[1])
#         print("Your last number is",number.len[5])
#         print("smallest number is",number.min)
#         print("largest number is",numbers.max)
#         print("Average number is",numbers.sum/ max_numbers)
# main()
# usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# username = float(input("Please enter your username"))
# if username != usernames:
#     print("Access denied")
# else:
#     print("Access Granted")