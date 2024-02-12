def sing_bottles_of_beer():
    for bottles in range(99, 0, -1):
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print(f"Take it down and pass it around, te.... oh man!  All the beer is gone!!\n")
        elif bottles == 2:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles-1} bottle of beer on the wall.\n")
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles-1} bottles of beer on the wall.\n")

sing_bottles_of_beer()

