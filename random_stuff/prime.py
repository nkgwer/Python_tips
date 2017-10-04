primes = [2]
import matplotlib.pyplot as plt
for i in range(3,10000):
    flag = True
    for prime in primes:
        if i%prime == 0:
            flag = False
            break
    if flag:
        primes.append(i)

plt.hist(primes, bins=30)
plt.show()


