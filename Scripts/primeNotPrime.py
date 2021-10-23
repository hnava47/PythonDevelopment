import math

print('''The following program determines if a number is prime or not
To quit just press enter''')

while True:
    number = (input('What is the value you want to test?: '))
    if len(number) == 0:
        break
    number = int(number)
    if number % 2 == 0:
        print('Not a prime!')
    else:
        for i in range(3, 1 + int(math.sqrt(number)), 2):
            if number % i == 0:
                print('Not a prime!')
                break
            else:
                print('Number is prime')
