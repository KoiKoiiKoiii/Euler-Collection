def primeCheck():
    primeList = [1, 2, 3, 5, 7, 11]
    false = 0
    for i in range(2, 104743):
      false = 0
      for x in primeList:
        if (i % 2 == 0):
          continue;
        if (i % x == 0):
          false = false + 1
          continue;
        if (len(primeList) == 10001):
          break;
      if (false == 1):
        primeList.append(i)
    print(primeList[10001])


primeCheck()