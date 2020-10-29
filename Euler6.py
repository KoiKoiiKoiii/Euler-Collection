def  firstHundredNatural():
  nums = []
  sqrnums = []
  for x in range(1, 101):
    y = (x * x)
    nums.append(y)
    sqrnums.append(x)
  print((sum(sqrnums) * sum(sqrnums)) - sum(nums))

firstHundredNatural()