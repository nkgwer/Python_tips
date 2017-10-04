import matplotlib.pyplot as plt
from tqdm import tqdm
primes = [2]

for i in tqdm(range(3,300000)):
    flag = True
    for prime in primes:
        if i%prime == 0:
            flag = False
            break
    if flag:
        primes.append(i)

plt.hist(primes, bins=100)
plt.show()


