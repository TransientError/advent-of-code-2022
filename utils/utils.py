from typing import Generator, Sequence, TypeVar


T = TypeVar("T")


def chunks(arr: Sequence[T], size: int) -> Generator[Sequence[T], None, None]:
    return (arr[i : i + size] for i in range(0, len(arr), size))


if __name__ == "__main__":
    print(list(chunks((range(25)), 5)))
    print(list(chunks((range(25)), 6)))
