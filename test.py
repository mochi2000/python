import random
answer = random.randint(1,10)
count = 0




while True:
  print("your number?", end="")
  num = int(input())
  count += 1

  if answer == num:
      print("Bingo ok %i" %count )
      break
  elif answer > num:
      print("mooo")
  else:
      print("none")

print("[Ansewer: %i]" %answer)