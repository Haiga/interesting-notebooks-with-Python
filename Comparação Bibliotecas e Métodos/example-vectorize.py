import time
import numpy as np



evaluated = 6700417
# evaluated = 10
def isPrime(value):
    for i in range(2, value - 1):
        # if (value / i).is_integer():
        if (value / i).is_integer():
            return False

    return True


started = time.time()
f = isPrime(evaluated)
finished = time.time()

print(f)
print(finished - started)

#################


def npIsPrime(value):
    def isDecimal(i):
        return value / (i+2) - np.floor(value / (i+2)) > 0
    return np.all(np.fromfunction(isDecimal, [value - 2]))


started = time.time()
f = npIsPrime(evaluated)
finished = time.time()

print(f)
print(finished - started)


