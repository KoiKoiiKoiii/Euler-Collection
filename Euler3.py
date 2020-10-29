def primeCheck():
    var = True
    primeList = [2, 3, 5, 7, 11]
    num = 2
    for i in range(2, 20000):
        if (num % i != 0):
            var = False
            print(int(1 / i))
        else:
            if (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0):
                var = False
            else:
                primeList.append(i)
        num = num + 1
    return primeList

def primeNum(num):
    prime = []
    if (num >= 2):
        if (num in primeCheck()):
            print("That's a prime number.")
        else:
            print("The prime factors are:")
            for i in primeCheck():
                if (num % i == 0):
                    num = num / i
                    prime.append(int(i))
                    print(f"{i}", end = "; ")
            print(f"\n\nmaking {prime[-1]} the largest prime factor.")
    else:
        print("Nice try, the number must be larger than 2.")


while True:
    try:
        primeNum(int(input("Please input the number you want the largest prime factor of: ")))
    except ValueError:
        print("Please enter a number.")
        continue
    else:
        break