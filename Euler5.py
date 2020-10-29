def smallestposnum():
  y = 0
  i = 2520
  while (y <= 10):
    for x in range(1, 20):
      if (i % x == 0):
        y = y + 1
      else:
        y = 0
        i = i + 2520
    if (y >= 10):
        print("Number found.")
        break;
  print(i)

smallestposnum()