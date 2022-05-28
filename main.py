
import random
t = int(input("Enter input:"))
n=random.randint(0,100)
if t > n:
  print("too low guess higher")
if t < n:
  print("too high guess again")
if t == n:
  print("spot on,rock on!")
