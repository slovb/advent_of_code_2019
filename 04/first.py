def hasDouble(n):
    m = n % 10
    n //= 10
    while n > 0:
        if m == n % 10:
            return True
        m = n % 10
        n //= 10
    return False


def isIncreasing(n):
    m = n % 10
    n //= 10
    while n > 0:
        if m < n % 10:
            return False
        m = n % 10
        n //= 10
    return True


def solve(lower, upper):
    count = 0
    for n in range(lower, upper):
        if isIncreasing(n) and hasDouble(n):
            print(n)
            count += 1
    return count


def main(lower, upper):
    return solve(lower, upper)


if __name__ == "__main__":
    lower = 147981
    upper = 691423
    print(main(lower, upper))
