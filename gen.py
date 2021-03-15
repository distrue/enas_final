import random

"""
print("[", end="")
for idx in range(91, 80, -1):
    print("0."+str(idx), end=", ")
print("]")

print("[", end="")
for idx in range(91, 80, -1):
    flutter = random.randrange(-7, 7)    
    print(idx*2 -40 + flutter, end=", ")
print("]")

"""

fro = [0.89, 0.88, 0.87, 0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.74, 0.72, 0.60, 0.54]

val = map(lambda x: x-0.1, fro)

print(list(val))
