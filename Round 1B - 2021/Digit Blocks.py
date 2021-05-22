import sys


class BaseBlockBuilder:
    def __init__(self, n, b):
        self.n = n
        self.b = b
        self.blocks = [[] for _ in range(self.n)]

    def place(self, digit):
        raise NotImplementedError()

    def run_single_step(self):
        digit = int(input())
        to_place = int(self.place(digit))
        if not 0 <= to_place < self.n:
            raise ValueError(f'Unexpected place {to_place}')
        if len(self.blocks[to_place]) >= self.b:
            raise ValueError(f'Block {to_place} already full. {self.blocks[to_place]!r}')
        self.blocks[to_place].append(digit)
        print(to_place + 1, flush=True)

    def run(self):
        for _ in range(self.n * self.b):
            self.run_single_step()
        return sum(int(''.join(map(str, reversed(bs)))) for bs in self.blocks) / (10 ** self.b * self.n)


class RandomBlockBuilder(BaseBlockBuilder):
    def place(self, digit):
        for i in range(self.n):
            if len(self.blocks[i]) < self.b:
                return i


class NaiveBlockBuilder(BaseBlockBuilder):
    def get_low_priority(self):
        for i in range(self.n):
            if len(self.blocks[i]) < self.b - 1:
                return i
        for i in range(self.n):
            if len(self.blocks[i]) < self.b:
                return i

    def get_biggest(self):
        return max(range(self.n), key=lambda i:(len(self.blocks[i]) < self.b, len(self.blocks[i])))

    def place(self, digit):
        if digit != 9:
            return self.get_low_priority()
        return self.get_biggest()


class SemiSmartBlockBuilder(NaiveBlockBuilder):
    def get_almost_full(self):
        for i in range(self.n):
            if len(self.blocks[i]) == self.b - 2:
                return i
        raise ValueError(f'Not blocks are almost full')

    def get_small(self):
        for i in range(self.n):
            if len(self.blocks[i]) < self.b - 2:
                return i
        return self.get_low_priority()

    def place(self, digit):
        if digit == 9:
            return self.get_biggest()
        if digit in (7, 8):
            try:
                return self.get_almost_full()
            except ValueError:
                pass
        return self.get_small()


def main():
    t, n, b, p = map(int, input().split())
    # s = 0
    for _ in range(t):
        res = SemiSmartBlockBuilder(n, b).run()
    #     s += res
    #     print(res, file=sys.stderr)
    # print('Average: {:5.2f} %'.format(s / t * 100), file=sys.stderr)

if __name__ == '__main__':
    main()
