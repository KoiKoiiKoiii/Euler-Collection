def Palindromatic():
  lists = []
  newest = []
  for x in range(100, 1000000):
    for i in str(x):
      lists.append(i)
    oldlist = lists.copy()
    lists.reverse()
    if (lists == oldlist):
      newest.append(x)
    lists.clear()
    oldlist.clear()
  return(newest)





def multiplePal():
  high = 0
  current = 0
  for x in Palindromatic():
    for i in range(1, 999):
      high = int(x / i)
      if (x % i == 0 and len((str(int(high)))) == 3):
        current = x / i
        currenti = i
  print(f"{int(current)} * {int(currenti)} are the largest 3 digit multiples of a palindrome. ({int((current) * currenti)})")


Palindromatic()
multiplePal()