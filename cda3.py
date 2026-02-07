def collatz(n):
    #Even
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    #Odd
    else:
        print(3 * n + 1)
        return 3 * n + 1


number = int(input("Enter a number: "))

while number != 1:
    number = collatz(number)
