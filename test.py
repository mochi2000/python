import random
answer = random.randint(1,10)




while True:
  print("your number?", end="")
  num = int(input())
  
  if answer == num:
      print("Bingo")
      break
  elif answer > num:
      print("mooo")
  else:
      print("none")

print("[Ansewer: %i]" %answer)