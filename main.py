from parser import tokenize
from validator import validate

from syntax_tree import (
    build_tree,
    print_tree,
    preorder,
    postorder,
    count_nodes,
    count_leaf_nodes,
    tree_depth
)

print("==================================")
print("HTML VALIDATOR SYSTEM")
print("==================================")

while True:
    print("1. Input HTML Manual")
    print("2. Baca File HTML")
    print("3. Keluar")

    pilihan = input("Pilihan: ")

    print("Pilihan Anda:", pilihan)

    if pilihan == "1":

        print("\n=== INPUT HTML MANUAL ===")

        html = input("Masukkan HTML:\n")

        tokens = tokenize(html)

        result, message = validate(tokens)

        print("\n" + message)

        if result:

            root = build_tree(tokens)

            print("\n=== Syntax Tree ===")
            print_tree(root)

            print("\n=== Preorder Traversal ===")
            preorder(root)

            print("\n\n=== Postorder Traversal ===")
            postorder(root)

            print("\n\n=== Statistik HTML ===")
            print("Jumlah Node      :", count_nodes(root))
            print("Jumlah Leaf Node :", count_leaf_nodes(root))
            print("Kedalaman Tree   :", tree_depth(root))
            
    elif pilihan == "2":

        print("\n=== BACA FILE HTML ===")

        nama_file = input("Masukkan nama file: ")

        try:

            with open(f"test/{nama_file}", "r") as file:
                html = file.read()

            tokens = tokenize(html)

            result, message = validate(tokens)

            print("\n" + message)

            if result:

                root = build_tree(tokens)

                print("\n=== Syntax Tree ===")
                print_tree(root)

                print("\n=== Preorder Traversal ===")
                preorder(root)

                print("\n\n=== Postorder Traversal ===")
                postorder(root)

                print("\n\n=== Statistik HTML ===")
                print("Jumlah Node      :", count_nodes(root))
                print("Jumlah Leaf Node :", count_leaf_nodes(root))
                print("Kedalaman Tree   :", tree_depth(root))

        except FileNotFoundError:

            print("File tidak ditemukan.")

    elif pilihan == "3":
        print("Terima kasih")
        break