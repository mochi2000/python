import random
answer = random.randint(1,10)

print("your number?", end="")
num = int(input())

if answer == num:
    print("Bingo")
elif answer > num:
    print("mooo")
else:
    print("none")

print("[Ansewer: %i]" %answer)