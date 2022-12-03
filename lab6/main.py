from bst import BinaryNode, BinarySearchTree


def main() -> None:
    # inicjalizacja drzewa
    drzewo = BinarySearchTree(BinaryNode(8))

    # min() przed dodaniem
    print(drzewo.root.min().value)

    # dodawanie elementow z listy
    drzewo.insert_list([3, 10, 14, 6, 7, 1, 4, 13, 2, 5, 9, 15])

    # min() po dodaniu
    print(drzewo.root.min().value)

    # czy zawiera 1 (True)
    print(drzewo.contains(1))

    # czy zawiera 15 (True)
    print(drzewo.contains(15))

    # usuwanie 2, 5, 9, 15
    drzewo.remove(2)
    drzewo.remove(5)
    drzewo.remove(9)
    drzewo.remove(15)

    # czy zawiera 15 (False)
    print(drzewo.contains(15))

    # renderowanie drzewa
    drzewo.show()


if __name__ == '__main__':
    main()
