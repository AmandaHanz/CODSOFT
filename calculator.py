print("------Calculator------")

int_1 = int(input('\nEnter first integer: '))
print('1. +\n2. -\n3. *\n4. /')
option = int(input('Select an option above: '))
int_2 = int(input('Enter second integer: '))

if int_2 == 0 and option == 4:
    print("Cannot divide by 0!")
else:
    print('Program is running...')

if option == 1:
    answer_1 = int_1 + int_2
    print(answer_1)
elif option == 2:
    answer_2 = int_1 - int_2
    print(answer_2)
elif option == 3:
    answer_3 = int_1 * int_2
    print(answer_3)
elif option == 4:
    answer_4 = int_1 / int_2
    print(answer_4)
else:
    print("Invalid option entered!")
