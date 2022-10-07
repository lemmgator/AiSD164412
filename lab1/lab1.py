print("Hello world!")


# zad 1)
def imienaz(i, n):
    print(f"{i}. {n}")


imienaz("S", "Minkowski")


# zad 2)
def inicja(i, n):
    print(f"{i[0].title()}. {n.title()}")


inicja("sebastian", "minkowski")


# zad 3)
def liczrok(a, b, wiek):
    rok = int(str(a) + str(b))
    print(rok - wiek)


liczrok(20, 22, 24)


# zad 4)
def zadanie2(i, n, foo):
    foo(i, n)


zadanie2("sebastian", "minkowski", inicja)


# zad 5)
def dziel(a, b):
    if a < 0 or b < 0:
        print("jedna z liczb nie jest dodatnia")
        return
    if b == 0:
        print("nie można dzielić przez 0")
        return
    print(a / b)


dziel(2, 5)


# zad 6)
def podaj():
    n = 0
    while n < 100:
        i = int(input("podaj liczbe do sumowania: "))
        n += i
        print(n)


podaj()


# zad 7)
def listokrotka(lista):
    krotka = tuple(lista)
    return krotka


lista1 = [1, 3, "b"]
print(listokrotka(lista1))


# zad 8)
def podajkrotka():
    lista = []
