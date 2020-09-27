import math
def fact (n):
    if n >= 0:
        if n == 0 or n == 1 :
            return 1
        else:
            f = 1
            for i in range(2 ,n+1):
                f = f * i
            return f
    else:
        return math.nan             


def permut(n , k):
    return fact (n) / (fact (n - k))

def combition(n , k):
    #return fact (n) / (fact (k) * fact (n-k))
    return permut(n , k) / fact (k)


if __name__ == '__main__':
    print(fact (1))
    print(fact (5))
    print(fact (-7))
    print(fact (0))