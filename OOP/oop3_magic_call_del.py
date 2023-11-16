class Summator:
    def __init__(self) -> None:
        self.values = []

    def __call__(self, value: int) -> int:
        self.values.append(value)
        return sum(self.values)

    def __str__(self):
        return ', '.join(f'{v}' for v in self.values)

    def __del__(self):
        print('Summator was deleted')


if __name__ == '__main__':
    summator = Summator()
    # del summator
    print(summator(5))
    print(summator(5))
    print(summator(5))
    print(summator)