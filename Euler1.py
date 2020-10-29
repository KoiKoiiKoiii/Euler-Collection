def multipleList():
  multiples = []
  for i in range(1, 10000):
    if (i % 3 == 0 or i % 5 == 0):
      multiples.append(i)
  return multiples

def sumOf():
  new = []
  for i in multipleList():
    if (i < 1000):
      new.append(i)
    else:
      break
  print(sum(new))

sumOf()
