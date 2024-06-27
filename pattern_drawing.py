size = int(input("Enter the size of the pattern: "))
times = size
while times != 0:
  for i in range (size):
    print("*", end="")
  print("")
  times -=1