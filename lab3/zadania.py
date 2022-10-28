def foo() -> None:
    foo()


def numbers(n: int):
    if n < 0:
        return
    print(f'n: {n}')
    numbers(n - 1)


def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    return number * power(number, n - 1)


def reverse(txt: str) -> str:
    if txt == '':
        return ''
    return reverse(txt[1:]) + txt[0]


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return factorial(n - 1) * n

# ???????????  |
# ???????????  |
# ??????????? \ /
# ???????????  V


def prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % n - 1 == 0:
        return


def main() -> None:
    numbers(10)
    print(fib(10))
    print(power(3, 3))
    print(reverse('Bomba'))
    print(factorial(5))
    print(prime(5))


main()
