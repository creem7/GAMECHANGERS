import time

userInput = int(
    input('Please Choose the number to find if its Prime or not: '))

flag = False

for i in range(2, userInput + 1):
    if userInput % i == 0:
        flag = True
        break

if flag:
    print(f'{userInput} is not prime')
else:
    print(f'{userInput} is Prime')

choice = 'none'

while choice not in ['Y', 'N']:
    choice = input(
        f'want to display all prime numbers between {userInput} (y,n): ').upper()

listOfPrimes = [2, ]

if choice == 'Y':
    for num in range(2, userInput + 1):
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                listOfPrimes.append(num)
                break
else:
    time.sleep(1)
    print('Good Bye')

print(listOfPrimes)