
choice = 0
while choice != 9:
        rows = int(input("Enter the # of rows: "))
        symbol = input("Enter the symbol to be printed: ")
        choice = int(input("""\n1- Right-Angled triangle.
2- Inverted Right-Angled triangle.
3- Pyramid.
4- Inverted Pyramid.
5- Diamond.
6- Hallow square.
7- Hallow pyramid.
8- Hourglass.
9- quit.
Enter the pattern that you you want to draw:
"""))
        print()
        if choice == 9:
            print()
            print()
            print("You quit the program!")
        if choice == 1:
            for i in range(1, rows + 1):
                for j in range (i):
                    print(symbol, end="")
                print()

        elif choice == 2:
            for i in range (rows , 0, -1):
                for j in range(i):
                    print(symbol, end = "")
                print()

        elif choice == 3:
            for i in range(1, rows + 1):
                for j in range(rows - i):
                    print(" ", end = "")
                for k in range (2 * i - 1):
                    print(symbol)
                print()

        elif choice == 4:
            for i in range(rows, 0, -1):
                for j in range(rows - i):
                    print(" " , end = "")
                for k in range(2 * i - 1):
                    print(symbol, end = "")
                print()
        elif choice == 5:
            for i in range(1, rows + 1):
                for j in range(rows - i):
                    print(" ", end = "")
                for k in range (2 * i - 1):
                    print(symbol, end = "")
                print()
            for i in range(rows - 1, 0, -1):
                for j in range(rows - i):
                    print(" ", end = "")
                for k in range(2 * i - 1):
                    print(symbol, end = "")
                print()
        elif choice == 6:
            for i in range(rows):
                for j in range (rows):
                    if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                        print(symbol, end = "")
                    else:
                        print(" ", end = "")
                print()
        elif choice == 7:
            for i in range(1, rows + 1):
                for j in range(rows - i):
                    print(" ", end = "")
                for k in range(2 * i - 1):
                    if k == 0 or k == 2 * i - 2 or i == rows:
                        print(symbol, end = "")
                    else:
                        print(" ", end = "")
                print()
        elif choice == 8:
            for i in range(rows, 0, -1):
                for j in range(rows - i):
                    print(" ", end="")
                for k in range(2 * i - 1):
                    print(symbol, end="")
                print()
            for i in range(2, rows + 1):
                for j in range(rows - i):
                    print(" ", end="")
                for k in range(2 * i - 1):
                    print(symbol, end="")
                print()