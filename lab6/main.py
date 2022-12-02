from bst import BinaryNode, BinarySearchTree


def main() -> None:
    # implementacja drzewa
    drzewo = BinarySearchTree(BinaryNode(8))

    # min() przed dodaniem
    print(drzewo.root.min().value)

    # drzewo.insert_list() -> insert() -> _insert()
    drzewo.insert_list([3, 10, 14, 1, 6, 7, 4, 13, 15])

    # min() po dodaniu
    print(drzewo.root.min().value)

    # czy zawiera 1 (False)
    print(drzewo.contains(1))

    # czy zawiera 15 (True)
    print(drzewo.contains(15))

    # usuwanie 15
    drzewo.remove(15)

    # usuwanie 25 (drzewo.contains(25) == False)
    drzewo.remove(25)

    # czy zawiera 15 (wywalilo to False)
    print(drzewo.contains(15))

    # renderowanie drzewa
    drzewo.show()


if __name__ == '__main__':
    main()
