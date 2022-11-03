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


def prime(n: int, x: int):
    if n == 1:
        return False
    if x == 1:
        return True
    if n % x == 0:
        return False
    else:
        return prime(n, x - 1)


def n_sums(n: int, licz: int, lista=[]):
    if licz > (10 ** n):
        return lista
    temp = [int(x) for x in str(licz)]
    if sum(temp[::2]) == sum(temp[1::2]):
        lista.append(licz)
    return n_sums(n, licz + 1, lista)


def remove_duplicates(txt: str) -> str:
    if len(txt) == 1:
        return txt[0]
    if txt[0] != txt[1]:
        return txt[0] + remove_duplicates(txt[1:])
    else:
        return remove_duplicates(txt[1:])


def main() -> None:
    numbers(10)
    print(fib(10))
    print(power(3, 3))
    print(reverse('Bomba'))
    print(factorial(5))
    print(prime(17, 16))
    print(n_sums(3, 100))
    print(remove_duplicates("AAAAAAAAAAAALLLLLLEEE       LLLLIIPPPAAAA!!!"))


main()
