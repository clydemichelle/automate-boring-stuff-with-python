#This program implements the collatz sequence
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
        
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

#Ask user to enter a number
try:
    num = int(input('Enter a number of your choice: '))

    while num != 1:
        num = collatz(num)
except ValueError as ve:
    print(' Enter an integer value. ')
