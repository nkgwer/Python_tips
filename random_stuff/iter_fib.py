class Fib:
    def __init__(self, end):
        self._fib_dic = {0: 1, 1: 1}
        self._end = end
        self._i = 0

    def __iter__(self):
        return self

    def _fib(self, i):
        if i in self._fib_dic:
            return self._fib_dic[i]
        else:
            self._fib_dic[i] = self._fib(i-1) + self._fib(i-2)
            return self._fib_dic[i]

    def __next__(self):
        if self._i >= self._end:
            raise StopIteration()
        else:
            val = self._fib(self._i)
            self._i += 1
            return val


for i in Fib(100):
    print(i)  # FAST!

