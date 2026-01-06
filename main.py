from random import randint
from time import sleep

def intinputvalidate(prompt):
    while True:
        cmd = input(prompt)
        try:
            cmd = int(cmd)
            break
        except:
            print("Invalid input")
    return cmd


# 1 = Addition/Subtraction, 2 = Multiplication/Division
mechanics = [1, 2]
mech1 = ['+', '-']
mech2 = ['*', '/']

allmechlist = []
for mechanic in mechanics:
    match mechanic:
        case 1:
            allmechlist.extend(mech1)
        case 2:
            allmechlist.extend(mech2)

# Max/min digits
# Addition
addmin = 1
addmax = 999
# Subtraction
minuendmin = 100
minuendmax = 999
subtrahendmin = 1
subtrahendmax = 999
# Multiplication
multmin = 1
multmax = 30
# Division
dividendmin = 1
dividendmax = 999
divisormin = 1
divisormax = 50

score = 0
scoregoal = intinputvalidate("Input score goal:\n")
scoregoalflag = True
cmd = 0
result = None

run = True
while run:

    if scoregoalflag:
        print(f"Goal: {scoregoal}")
    else:
        print("Endless Mode")
    print(f"Score: {score}")

    chosenmechanic = allmechlist[randint(0, len(allmechlist)-1)]

    match chosenmechanic:
        case '+':
            value1 = randint(addmin, addmax)
            value2 = randint(addmin, addmax)
            result = str(value1 + value2)

            cmd = input(f"{value1} + {value2} = ")

        case '-':
            minuend = randint(minuendmin, minuendmax)
            subtrahend = randint(subtrahendmin, subtrahendmax)
            if minuend-subtrahend < 0:
                minuend, subtrahend = subtrahend, minuend
            result = str(minuend - subtrahend)

            cmd = input(f"{minuend} - {subtrahend} = ")

        case '*':
            value1 = randint(multmin, multmax)
            value2 = randint(multmin, multmax)
            result = str(value1 * value2)

            cmd = input(f"{value1} x {value2} = ")

        case '/':
            dividend = randint(dividendmin, dividendmax)
            divisor = randint(divisormin, divisormax)
            while dividend % divisor != 0: # Loop until the division has no remainder
                dividend -= 1
                if dividend <= divisor: # If dividend is lower or equal
                    dividend = randint(dividendmin, dividendmax) # Re randomise
            result = str(dividend // divisor)

            cmd = input(f"{dividend} / {divisor} = ")

        case '_':
            cmd = 0
            result = None

    if cmd == result: # If correct
        score += 1
        print("Correct!\n")
    else:
        print(f"Incorrect, the correct answer was {result}\n")

    if score >= scoregoal and scoregoalflag:
        print("Congratulations!")
        scoregoalflagconfirm = input("Would you like to continue playing? Leave empty if no\n")
        if scoregoalflagconfirm == '':
            run = False
        else:
            scoregoalflag = False
            print("Goal has been removed. Good luck\n")