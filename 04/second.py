def hasProperDouble(n):
    m = n % 10
    n //= 10
    inTripple = False
    while n > 0:
        if m == n % 10:
            if n < 10 and not inTripple:  # at the end
                return True
            elif m == (n // 10) % 10:  # even next digit
                inTripple = True
            elif not inTripple:
                return True
        elif inTripple:
            inTripple = False
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
        if isIncreasing(n) and hasProperDouble(n):
            print(n)
            count += 1
    return count


def main(lower, upper):
    return solve(lower, upper)


if __name__ == "__main__":
    lower = 147981
    upper = 691423
    print(main(lower, upper))
