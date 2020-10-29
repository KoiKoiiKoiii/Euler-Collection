def Fibonacci():
  lists = [0, 1]
  for i in range(1, 100):
    lists.append(lists[-1] + lists[-2])
    if(lists[-1] >= 4000000):
      break
  return(lists)


def evenValuedSums():
  print(f"The sum of the even values of the Fibonacci sequence:")
  evenvalues = []
  stored = 0
  for i in Fibonacci():
    if (i % 2 == 0):
      evenvalues.append(i)
      print(f"{i} + {stored} = {i + stored}")
      stored = i + stored

evenValuedSums()