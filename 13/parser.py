from pathlib import Path


data = Path("test-input.txt").read_text().splitlines()


class Token:
    pass


class Array(Token):
    value: list[Token]

    def __init__(self, value: list[Token]) -> None:
        super().__init__()
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


class Int(Token):
    value: int

    def __init__(self, value: int) -> None:
        super().__init__()
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)


def parse(s: str) -> Token:
    val, _ = parseNext(s, 0)
    return val


def parseNext(s: str, i: int) -> tuple[Token, int]:
    if s[i] == "[":
        return parseArray(s, i + 1)
    else:
        return parseInt(s, i)


def parseArray(s: str, i: int) -> tuple[Array, int]:
    result = []
    if s[i] == "]":
        return (Array(result), i + 1)
    while True:
        value, i = parseNext(s, i)
        result.append(value)
        if s[i] == "]":
            break
        if s[i] == ",":
            i += 1

    return (Array(result), i + 1)


def parseInt(s: str, i: int) -> tuple[Int, int]:
    start = i
    while s[i] != "," and s[i] != "]":
        i += 1
    return (Int(int(s[start:i])), i + 1 if s[i] == ',' else i)


for i, line in enumerate(data):
    if line and i > 2:
        print(parse(line))
