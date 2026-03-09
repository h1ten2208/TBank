r = True
a = int(input())
b = int(input())
x = 1
x1 = 0
while x < b:
  Sx = x + x1
  x1 = x
  x = Sx
  if x >= a and x <= b:
    r = False
    print(x)
if r:
  print("В заданном диапазоне нет чисел Фибоначчи")
